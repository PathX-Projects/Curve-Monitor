from slack_sdk import WebClient

from .curve import CurveAPI


class AlertsProcess:
    def __init__(self):
        self.api = CurveAPI()

    def poll_usdd_test(self):

        usdd_pool_data = self.api.getPoolData(pool_address="0xe6b5CC1B4b47305c58392CE3D359B10282FC36Ea",
                                              network_id="ethereum", tag_id="factory")

        # Get token data
        tokens_usd = {c['symbol']:
                          {'balance_usd': (int(c['poolBalance']) / 10 ** int(c['decimals'])) * c['usdPrice'],
                           'composition': (int(c['poolBalance']) / 10 ** int(c['decimals'])) * c['usdPrice'] / usdd_pool_data['usdTotal']}
                      for c in usdd_pool_data['coins']}


        print("Output:", tokens_usd)
        print(f"USDD Composition: {tokens_usd['USDD']['composition'] * 100:.2f}%")

    def run(self):
        pass