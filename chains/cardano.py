import requests


class Cardano:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_latest_block(self):
        response = requests.get(
            f"{self.api_url}/tip",
            timeout=10,
        )

        response.raise_for_status()

        return response.json()[0]["block_no"]