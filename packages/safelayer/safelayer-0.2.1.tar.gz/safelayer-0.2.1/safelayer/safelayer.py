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
    def log(
        cls,
        node: Node,
        pipeline: Optional[Pipeline] = None,
        pipeline_done=False,
        data={},
    ):
        node_data = node.__dict__

        pipeline_data = pipeline.__dict__ if pipeline else None
        if pipeline_data is not None:
            pipeline_data["done"] = pipeline_done

        payload = {
            "data": data,
            "time": datetime.datetime.utcnow().isoformat(),
            "node": node_data,
            "pipeline": pipeline_data,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {cls._apiKey}",
        }

        response = requests.post(
            f"{cls._apiUrl}/log", headers=headers, data=json.dumps(payload)
        )

        return response


node = lambda name: Node(name)
pipeline = lambda name: Pipeline(name)
init = Safelayer.init
log = Safelayer.log
