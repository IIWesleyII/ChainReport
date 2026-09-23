from chains.rpc import JsonRpcChain


class Ethereum(JsonRpcChain):

    def get_latest_block(self):
        result = self._rpc("eth_blockNumber")

        return int(result, 16)