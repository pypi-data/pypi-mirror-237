import json
import os

import requests
from requests.structures import CaseInsensitiveDict


class HubSpotClient:
    def __init__(
        self,
        access_token,
        base_url="https://api.hubapi.com/crm/v3/",
        environment=os.environ.get("ENV", "Staging"),
    ):
        self.base_url = base_url
        self.headers = CaseInsensitiveDict(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "authorization": f"Bearer {access_token}",
            }
        )
        self.environment = environment

    @property
    def business_object_id(self) -> str:
        return {"Staging": "2-4781611", "Prod": "2-6132924"}.get(self.environment)

    @property
    def user_object_id(self) -> str:
        return {"Staging": "2-7162134", "Prod": "2-8366049"}.get(self.environment)

    def get_business(self, business_id):
        resp = requests.get(
            f"{self.base_url}objects/{self.business_object_id}/{business_id}",
            headers=self.headers,
        )
        return resp

    def update_business(self, business_id, properties):
        resp = requests.patch(
            f"{self.base_url}objects/{self.business_object_id}/{business_id}?properties=isactive&idProperty=businessid",
            headers=self.headers,
            data=json.dumps({"properties": {**properties}}),
        )
        return resp

    def create_business(self, properties):
        resp = requests.post(
            f"{self.base_url}objects/{self.business_object_id}?properties=isactive&idProperty=businessid",
            headers=self.headers,
            data=json.dumps({"properties": {**properties}}),
        )
        return resp

    def create_or_update_business(self, business_id, properties):
        resp = self.get_business(business_id)

        if resp.status_code == 200:
            return self.update_business(business_id, properties)

        elif resp.status_code == 404:
            return self.create_business(properties)

        else:
            return resp
