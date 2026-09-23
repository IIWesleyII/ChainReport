import requests


class JsonRpcChain:
    def __init__(self, rpc_url):
        self.rpc_url = rpc_url

    def _rpc(self, method, params=None):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params or [],
        }

        response = requests.post(
            self.rpc_url,
            json=payload,
            timeout=10,
        )

        data = response.json()

        return data["result"]