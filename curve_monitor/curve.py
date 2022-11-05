import requests
from requests import Response
from requests.exceptions import RequestException
from ratelimit import limits, sleep_and_retry

from curve_monitor._config import *


class PoolNotFound(Exception):
    pass


class CurveAPI:
    def getPoolData(self, pool_address: str, network_id: str, tag_id: str) -> dict:
        """
        :param pool_address: The address of the pool
        :param network_id: The corresponding network ID as shown in _config.py
        :param tag_id: The corresponding tag ID as shown in _config.py
        :return:
        """
        r = self.__call__(self._getURL(network_id, tag_id))
        if r.status_code != 200:
            raise RequestException(f'{r.status_code} - {r.text}')

        for pool in r.json()['data']['poolData']:
            if pool['address'].lower() == pool_address.lower():
                return pool

        raise PoolNotFound(f'Could not locate pool "{pool_address}" on "{network_id}" with tag_id "{tag_id}"')

    def _getURL(self, network_id, tag_id: str) -> str:
        """Prepare the endpoint for request to the API"""
        assert network_id.lower() in NETWORK_IDS
        assert tag_id.lower() in TAG_IDS

        return f'{GETPOOLS_BASE_ENDPOINT.format(network_id=network_id.lower(), tag_id=tag_id.lower())}'

    @sleep_and_retry
    @limits(calls=1, period=1)  # 1 call per second default
    def __call__(self, _url: str) -> Response:
        return requests.get(_url)