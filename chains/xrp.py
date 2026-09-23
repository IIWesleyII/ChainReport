from chains.rpc import JsonRpcChain


class XRP(JsonRpcChain):
    def get_latest_block(self):
        result = self._rpc(
            "ledger",
            [{"ledger_index": "validated"}],
        )

        return result["ledger_index"]

    def get_block(self, block_number):
        result = self._rpc(
            "ledger",
            [
                {
                    "ledger_index": block_number,
                    "transactions": False,
                }
            ],
        )

        return result["ledger"]

    def get_transaction(self, tx_id):
        return self._rpc(
            "tx",
            [
                {
                    "transaction": tx_id,
                    "binary": False,
                }
            ],
        )

    def get_balance(self, address):
        result = self._rpc(
            "account_info",
            [
                {
                    "account": address,
                    "ledger_index": "validated",
                }
            ],
        )

        balance = result["account_data"]["Balance"]

        return int(balance) / 1_000_000