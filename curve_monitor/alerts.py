from time import sleep
from slack_sdk import WebClient
from os import getenv

from curve_monitor.curve import CurveAPI
from curve_monitor._config import POLLING_PERIOD
from curve_monitor._logger import logged, logger
from curve_monitor.slack import SlackClient
from curve_monitor.db_handler import load_alerts, del_alert




class AlertsProcess:
    def __init__(self):
        self.api = CurveAPI()
        self.slack = SlackClient(oauth_token=getenv('SLACK_OAUTH_TOKEN'),
                                 workspace_channel=getenv('SLACK_CHANNEL'))

    @logged
    def poll(self):
        for alert in load_alerts():
            pool_data = self.api.getPoolData(pool_address=alert['pool_address'],
                                             network_id=alert['network_id'], tag_id=alert['tag_id'])
            tokens_usd = {c['symbol']:
                              {'balance_usd': (int(c['poolBalance']) / 10 ** int(c['decimals'])) * c['usdPrice'],
                               'composition': (int(c['poolBalance']) / 10 ** int(c['decimals'])) * c['usdPrice'] / pool_data['usdTotal'],
                               'address': c['address']}
                          for c in pool_data['coins']}

            condition_token_composition = tokens_usd[alert['condition']['token']]['composition'] * 100
            if alert['condition']['operator'].lower() == "above" and condition_token_composition >= alert['condition']['target_pct'] \
                    or alert['condition']['operator'].lower() == "below" and condition_token_composition <= alert['condition']['target_pct']:
                self.slack.composition_alert(network=alert['network_id'], tag=alert['tag_id'], pool_data=pool_data,
                                             tokens_data=tokens_usd, alert_data=alert)
                del_alert(alert['id'])

    @logged
    def poll_usdd_test(self):
        """ FOR TESTING ONLY """

        usdd_pool_data = self.api.getPoolData(pool_address="0xe6b5CC1B4b47305c58392CE3D359B10282FC36Ea",
                                              network_id="ethereum", tag_id="factory")

        # Get token data
        tokens_usd = {c['symbol']:
                          {'balance_usd': (int(c['poolBalance']) / 10 ** int(c['decimals'])) * c['usdPrice'],
                           'composition': (int(c['poolBalance']) / 10 ** int(c['decimals'])) * c['usdPrice'] / usdd_pool_data['usdTotal'],
                           'address': c['address']}
                      for c in usdd_pool_data['coins']}
        print('tokens_usd', tokens_usd)

        # print("Output:", tokens_usd)
        # print(f"USDD Composition: {tokens_usd['USDD']['composition'] * 100:.2f}%")
        self.slack.composition_alert(network='ethereum', tag='factory', pool_data=usdd_pool_data, tokens_data=tokens_usd)

    def run(self):
        logger.info('Alerts process started.')

        while True:
            self.poll()
            
            sleep(POLLING_PERIOD)