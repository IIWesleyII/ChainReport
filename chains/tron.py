import requests


class Tron:
    def __init__(self, rpc_url):
        self.rpc_url = rpc_url

    def get_latest_block(self):
        response = requests.post(
            f"{self.rpc_url}/wallet/getnowblock",
            json={},
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return data["block_header"]["raw_data"]["number"]