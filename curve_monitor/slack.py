import logging
from typing import Optional, Union
from os.path import join, dirname
from os import getcwd
from datetime import datetime, timezone, timedelta
import json
from time import time
from math import ceil

from curve_monitor._config import *
from curve_monitor._logger import logged, logger

from slack_sdk import WebClient

# https://slack.dev/python-slack-sdk/web/index.html#messaging

"""
CONSTRUCTING MESSAGE BLOCKS:
https://api.slack.com/reference/block-kit/blocks
https://app.slack.com/block-kit-builder
"""


class TimeDelta(timedelta):
    def to_dhms(self) -> tuple:
        """
        to days, hours, minutes, seconds
        parse the superclass string
        :return tuple: days, hours, min, sec
        """
        s = self.__str__().split(" day, ")
        days = s[0] if len(s) > 1 else 0
        hours, mins, sec = s[-1].split(":")
        try:
            sec = ceil(float(sec))
        except:  # Edge case, leave sec untouched
            pass

        return days, hours, mins, sec


class SlackClient(WebClient):
    def __init__(self, oauth_token: str, workspace_channel: str):
        """
        :param oauth_token:str: Authenticate the bot with slack using the OAuth token
        :param workspace_channel:str: Specify the channel in the workspace to which the bot will post
        """
        super().__init__(token=oauth_token)
        self.token = oauth_token
        self.channel = workspace_channel if "#" in workspace_channel else f"#{workspace_channel}"

    @logged
    def composition_alert(self, network: str, tag: str, pool_data: dict, tokens_data: dict, alert_data: dict) -> None:
        template = self.load_template('composition_alert.txt')
        # print(timedelta(seconds=(proposal.end - proposal.start)).__str__())

        blocks = template.format(
            pool_url=CURVE_POOL_BASEURL.format(network_id=network, pool_id=pool_data['id']),
            pool_name=pool_data['name'],
            pool_address=pool_data['address'],
            network=network,
            tag=tag,
            assets=", ".join([c['symbol'] for c in pool_data['coins']]),
            tvl=f"${int(pool_data['usdTotal']):,}",  # should be string formatted like so: $9,999,999.00
            condition_token=alert_data['condition']['token'],
            condition=f"{alert_data['condition']['operator'].lower()} {alert_data['condition']['target_pct']}%",
            composition_breakdown=self._prepare_composition_breakdown(tokens_data)
        )
        self.chat_postMessage(channel=self.channel, text=f"Curve Composition Alert", blocks=blocks)
        logger.info(f'Composition alert sent to slack workspace "{self.channel}"')

    def _prepare_composition_breakdown(self, tokens_data: dict) -> str:
        output = ""
        template = self.load_template('composition_breakdown.txt')
        for token, data in tokens_data.items():
            output += template.format(
                token_address=data['address'].lower(),
                token_symbol=token,
                supply=f"${int(data['balance_usd']):,}",
                composition_pct=f"{data['composition'] * 100:.1f}",
            )
        return output

    @staticmethod
    def load_template(filename: str) -> str:
        """Load the template for the message blocks"""
        with open(join(dirname(__file__), 'templates', filename), "r", encoding='utf-8') as f:
            return f.read()
