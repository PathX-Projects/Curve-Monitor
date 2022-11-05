import json
from pathlib import Path
from dataclasses import dataclass

from ._config import *
from ._logger import logged


DB_PATH = Path(__file__).parent.joinpath('db', 'composition_alerts.json')


@logged
def add_alert(network_id: str, tag_id: str, pool_address: str, condition: tuple[str, str, float]) -> int:
    """
    :param network_id: str - network ID, use the options shown in ./_config.py
    :param tag_id: str - Tag ID, use the options shown in ./_config.py
    :param pool_address: str
    :param condition: tuple - token_symbol, condition (ABOVE/BELOW), target_pct (e.g. 40 = 40%)
    :return: Alert ID (for retrieval from the database)
    """
    assert network_id in NETWORK_IDS
    assert tag_id in TAG_IDS

    old_alerts = load_alerts()
    _id = max([a['id'] for a in old_alerts]) + 1
    alert = {
        "id": _id,
        "network_id": network_id,
        "tag_id": tag_id,
        "pool_address": pool_address,
        "condition": {
          "token": condition[0],
          "operator": condition[1].lower(),
          "target_pct": float(condition[2])
        }
    }
    old_alerts.append(alert)
    update_alerts(old_alerts)
    return _id


@logged
def del_alert(alert_id: int) -> int:
    """
    :param alert_id: The ID of the corresponding alert in the database
    :return: The alert ID that was removed (if successful)
    """
    alerts = load_alerts()
    for i, alert in enumerate(alerts.copy()):
        if alert['id'] == alert_id:
            del alerts[i]
            update_alerts(alerts)
            return alert_id
    else:
        raise ValueError(f'Could not delete/locate alert with ID: {alert_id}')


@logged
def load_alerts(alert_id: int = None) -> list[dict]:
    """
    :return: list[dict] of alerts from ./db/composition_alerts.json
    """
    with open(DB_PATH, 'r') as f:
        output = json.load(f)

    if alert_id is not None:
        for alert in output:
            if alert['id'] == alert_id:
                return alert
        else:
            raise ValueError(f'Alert not found with ID: {alert_id}')

    return output

@logged
def update_alerts(data: list[dict]) -> None:
    with open(DB_PATH, 'w') as f:
        f.write(json.dumps(data, indent=2))
