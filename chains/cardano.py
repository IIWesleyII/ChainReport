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

        return response.json()[0]["block_height"]

    def get_block(self, block_number):
        response = requests.get(
            f"{self.api_url}/blocks",
            params={
                "block_height": f"eq.{block_number}",
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()[0]

    def get_transaction(self, tx_id):
        response = requests.post(
            f"{self.api_url}/tx_info",
            json={
                "_tx_hashes": [tx_id],
                "_inputs": False,
                "_metadata": False,
                "_assets": False,
                "_withdrawals": False,
                "_certs": False,
                "_scripts": False,
                "_bytecode": False,
                "_governance": False,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return data[0] if data else None

    def get_balance(self, address):
        response = requests.post(
            f"{self.api_url}/address_info",
            json={
                "_addresses": [address],
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            return 0

        return int(data[0]["balance"]) / 1_000_000