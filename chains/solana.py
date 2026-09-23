from chains.rpc import JsonRpcChain


class Solana(JsonRpcChain):
    def get_latest_block(self):
        return self._rpc("getSlot")

    def get_block(self, block_number):
        return self._rpc(
            "getBlock",
            [
                block_number,
                {
                    "encoding": "json",
                    "transactionDetails": "none",
                },
            ],
        )

    def get_transaction(self, tx_id):
        return self._rpc(
            "getTransaction",
            [
                tx_id,
                {
                    "encoding": "json",
                    "maxSupportedTransactionVersion": 0,
                },
            ],
        )

    def get_balance(self, address):
        result = self._rpc(
            "getBalance",
            [address],
        )

        return result["value"] / 1_000_000_000