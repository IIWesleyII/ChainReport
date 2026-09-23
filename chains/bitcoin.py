from chains.rpc import JsonRpcChain
import requests

class Bitcoin(JsonRpcChain):
    def get_latest_block(self):
        return self._rpc("getblockcount")

    def get_block(self, block_number):
        block_hash = self._rpc(
            "getblockhash",
            [block_number],
        )

        return self._rpc(
            "getblock",
            [block_hash, 1],
        )

    def get_transaction(self, tx_id):
        response = requests.get(
            f"{self.rpc_url}/api/v2/tx/{tx_id}",
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    def get_balance(self, address):
        response = requests.get(
            f"{self.rpc_url}/api/v2/address/{address}",
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return int(data["balance"]) / 100_000_000