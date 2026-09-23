from chains.rpc import JsonRpcChain


class Dogecoin(JsonRpcChain):
    def get_latest_block(self):
        return self._rpc("getblockcount")