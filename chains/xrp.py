from chains.rpc import JsonRpcChain


class XRP(JsonRpcChain):
    def get_latest_block(self):
        result = self._rpc(
            "ledger",
            [{"ledger_index": "validated"}],
        )

        return result["ledger_index"]