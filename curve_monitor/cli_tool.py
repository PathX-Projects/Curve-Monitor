import os
import json

from curve_monitor.db_handler import *
from curve_monitor._config import *
from curve_monitor.curve import CurveAPI, PoolNotFound


class CurveMonitorCLI:
    def __init__(self):
        self.api = CurveAPI()

    def run(self):
        while True:
            print('\n')
            usr_inp = input('Enter alerts operation (add, remove, quit): ')
            if usr_inp.lower() == 'add':
                network = input(f'Enter network ID ({", ".join(NETWORK_IDS)}): ')
                tag = input(f'Enter tag ID ({", ".join(TAG_IDS)}): ')
                pool = input(f'Enter pool address: ')
                tok = input(f'Enter condition token symbol: ').upper()
                operator = input(f'Enter condition operator ({", ".join(CONDITIONS)}): ')
                target = float(input(f'Enter condition target % (e.g. 40 = 40%): '))

                try:
                    self.api.getPoolData(pool_address=pool, network_id=network, tag_id=tag)
                except:
                    print('Could not locate curve pool with given data.')
                    continue

                alert_id = add_alert(network, tag, pool, (tok, operator, target))
                print('Added alert to database: ', load_alerts(alert_id))
            elif usr_inp.lower() == 'remove':
                _id = int(input(f'Enter alert ID: '))
                alert = load_alerts(_id)
                del_alert(_id)
                print(f'Deleted alert ({_id}) from database: {alert}')
            elif usr_inp.lower() == 'quit':
                break
            else:
                print('Invalid operation.')