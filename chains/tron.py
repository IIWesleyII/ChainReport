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

    def get_block(self, block_number):
        response = requests.post(
            f"{self.rpc_url}/wallet/getblockbynum",
            json={"num": block_number},
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    def get_transaction(self, tx_id):
        response = requests.post(
            f"{self.rpc_url}/wallet/gettransactionbyid",
            json={"value": tx_id},
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    def get_balance(self, address):
        response = requests.post(
            f"{self.rpc_url}/wallet/getaccount",
            json={
                "address": address,
                "visible": True,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("balance", 0) / 1_000_000
    