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

    @property
    def user_business_association(self) -> str:
        return {"Staging": "33", "Prod": "37"}.get(self.environment)

    def create_or_update_business(self, business_id, properties):
        business = self.get_business(business_id)

        if len(business):
            hubspot_record_id = business[0]["id"]
            return self.update_business(
                hubspot_record_id=hubspot_record_id, properties=properties
            )
        else:
            return self.create_business(properties)

    def create_or_update_user(self, user_id, properties):
        user = self.get_user(user_id)

        if len(user):
            hubspot_record_id = user[0]["id"]
            return self.update_user(
                hubspot_record_id=hubspot_record_id, properties=properties
            )
        else:
            return self.create_user(properties)

    def associate_user_business(self, user_id, business_id):
        user = self.get_user(user_id)
        business = self.get_business(business_id)
        if not len(user):
            raise Exception(f"User with ID {user_id} not found on hubspot.")
        user = user[0]

        if not len(business):
            raise Exception(f"Business with ID {business_id} not found on hubspot.")
        business = business[0]

        resp = requests.put(
            "{}objects/{}/{}/associations/{}/{}".format(
                self.base_url,
                self.user_object_id,
                user["id"],
                self.business_object_id,
                business["id"],
            ),
            headers=self.headers,
        )
        return resp

    def get_business(self, business_id):
        resp = requests.post(
            f"{self.base_url}objects/{self.business_object_id}",
            headers=self.headers,
            data=json.dumps(
                {
                    "filterGroups": [
                        {
                            "filters": [
                                {
                                    "propertyName": "businessid",
                                    "operator": "EQ",
                                    "value": business_id,
                                }
                            ]
                        }
                    ]
                }
            ),
        )
        return resp.json()["results"]

    def update_business(self, hubspot_record_id, properties):
        resp = requests.patch(
            f"{self.base_url}objects/{self.business_object_id}/{hubspot_record_id}?properties=isactive&idProperty=businessid",
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

    def get_user(self, user_id):
        resp = requests.post(
            f"{self.base_url}objects/{self.user_object_id}",
            headers=self.headers,
            data=json.dumps(
                {
                    "filterGroups": [
                        {
                            "filters": [
                                {
                                    "propertyName": "user_id",
                                    "operator": "EQ",
                                    "value": user_id,
                                }
                            ]
                        }
                    ]
                }
            ),
        )
        return resp.json()["results"]

    def create_user(self, properties):
        resp = requests.post(
            f"{self.base_url}objects/{self.user_object_id}",
            headers=self.headers,
            data=json.dumps({"properties": {**properties}}),
        )
        return resp

    def update_user(self, hubspot_record_id, properties):
        resp = requests.patch(
            f"{self.base_url}objects/{self.user_object_id}/{hubspot_record_id}",
            headers=self.headers,
            data=json.dumps({"properties": {**properties}}),
        )
        return resp
