from chains.rpc import JsonRpcChain


class Bitcoin(JsonRpcChain):
    
    def get_latest_block(self):
        return self._rpc("getblockcount")