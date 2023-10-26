import requests
import json
from .response import SuccessResponse


class GroupRobot:
    def __init__(self, webhook: str):
        self.webhook = webhook

    def send(self, data):
        response = requests.post(
            self.webhook, headers={"Content-Type": "application/json"}, data=json.dumps(data), timeout=10
        )
        return SuccessResponse(data=response.json())
