from chains.rpc import JsonRpcChain


class Solana(JsonRpcChain):
    
    def get_latest_block(self):
        return self._rpc("getSlot")