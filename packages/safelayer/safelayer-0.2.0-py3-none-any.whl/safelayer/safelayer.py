from typing import Optional

import os
import uuid
import json
import requests
import datetime


class Node:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name


class Pipeline:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name


class Safelayer:
    _apiKey = os.environ.get("SAFELAYER_API_KEY")
    _apiUrl = (
        os.environ.get("SAFELAYER_API_URL") or "https://api.repllabs.com/v1/safelayer"
    )

    @classmethod
    def init(cls, apiKey: Optional[str] = None):
        if apiKey:
            cls._apiKey = apiKey

        if not cls._apiKey:
            raise ValueError("API key is missing.")

    @classmethod
    def log(cls, data={}, node=Node, pipeline=Optional[Pipeline], pipeline_done=False):
        timestamp = datetime.datetime.now().isoformat()

        payload = {
            "data": data,
            "timestamp": timestamp,
            "node": node.__dict__,
            "pipeline": pipeline.__dict__ if pipeline else None,
            "pipeline_done": pipeline_done,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {cls._apiKey}",
        }

        response = requests.post(cls._apiUrl, headers=headers, data=json.dumps(payload))

        return response


node = lambda name: Node(name)
pipeline = lambda name: Pipeline(name)
init = Safelayer.init
log = Safelayer.log
