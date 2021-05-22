import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()


class Settings:
    github_access_token = os.environ.get("GITHUB_ACCESS_TOKEN")
    github_username = os.environ.get("GITHUB_USERNAME")

    class EnvSettingException(BaseException):
        pass

    def __init__(self):
        if isinstance(self.github_username, type(None)):
            raise EnvironmentError("github_username is None")
        if isinstance(self.github_access_token, type(None)):
            raise EnvironmentError("github_access_token is None")


settings = Settings()


def invite_user_to_organization(user_email: str):
    auth_tuple = (settings.github_username, settings.github_access_token)
    github_api_url = "https://api.github.com"
    org = "pocofarm"
    headers = {
        "content-type": "application/json",
        "accept": "application/vnd.github.v3+json, text/plain, */*",
    }
    data = dict(role="admin", email=user_email)
    url = f"{github_api_url}/orgs/{org}/invitations"
    return requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        auth=auth_tuple,
    )


# use case

email: str = "cjisoo0117@gmail.com"
resp = invite_user_to_organization(user_email=email)

