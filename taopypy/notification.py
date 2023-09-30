import requests
import json


def notify_to_slack(payload: dict, to: str) -> requests.Response:
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    res = requests.post(
        url=to,
        headers=headers,
        data=json.dumps(payload),
        proxies=None,
    )

    return res
