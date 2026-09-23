from chains.rpc import JsonRpcChain


class Base(JsonRpcChain):
    def get_latest_block(self):
        result = self._rpc("eth_blockNumber")

        return int(result, 16)

    def get_block(self, block_number):
        return self._rpc(
            "eth_getBlockByNumber",
            [hex(block_number), False],
        )
    
    def get_transaction(self, tx_id):
        return self._rpc(
            "eth_getTransactionByHash",
            [tx_id],
        )

    def get_balance(self, address):
        result = self._rpc(
            "eth_getBalance",
            [address, "latest"],
        )

        return int(result, 16) / 10**18