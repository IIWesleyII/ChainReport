import os

from chains.base import Base
from chains.bitcoin import Bitcoin
from chains.cardano import Cardano
from chains.dogecoin import Dogecoin
from chains.ethereum import Ethereum
from chains.solana import Solana
from chains.tron import Tron
from chains.xrp import XRP

from dotenv import load_dotenv
load_dotenv()

RPC_ETHEREUM_MAINNET_URL = os.getenv("RPC_ETHEREUM_MAINNET_URL")
RPC_SOLANA_MAINNET_URL = os.getenv("RPC_SOLANA_MAINNET_URL")
RPC_BITCOIN_MAINNET_URL = os.getenv("RPC_BITCOIN_MAINNET_URL")
RPC_BASE_MAINNET_URL = os.getenv("RPC_BASE_MAINNET_URL")
RPC_DOGECOIN_MAINNET_URL=os.getenv("RPC_DOGECOIN_MAINNET_URL")
RPC_XRP_MAINNET_URL=os.getenv("RPC_XRP_MAINNET_URL")
RPC_TRON_MAINNET_URL=os.getenv("RPC_TRON_MAINNET_URL")
CARDANO_API_URL=os.getenv("CARDANO_API_URL")

def main():
    print("Select blockchain:")
    print("1. Ethereum")
    print("2. Solana")
    print("3. Bitcoin")
    print("4. Base")
    print("5. Dogecoin")
    print("6. XRP")
    print("7. Tron")
    print("8. Cardano")

    chain_choice = input("Enter a number: ").strip()

    if chain_choice == "1":
        chain = Ethereum(RPC_ETHEREUM_MAINNET_URL)

    elif chain_choice == "2":
        chain = Solana(RPC_SOLANA_MAINNET_URL)

    elif chain_choice == "3":
        chain = Bitcoin(RPC_BITCOIN_MAINNET_URL)

    elif chain_choice == "4":
        chain = Base(RPC_BASE_MAINNET_URL)

    elif chain_choice == "5":
        chain = Dogecoin(RPC_DOGECOIN_MAINNET_URL)

    elif chain_choice == "6":
        chain = XRP(RPC_XRP_MAINNET_URL)

    elif chain_choice == "7":
        chain = Tron(RPC_TRON_MAINNET_URL)

    elif chain_choice == "8":
        chain = Cardano(CARDANO_API_URL)

    else:
        print("Invalid blockchain.")
        return

    print()
    print("Select action:")
    print("1. Get latest block")
    print("2. Get block")
    print("3. Get transaction")
    print("4. Get balance")

    action_choice = input("Enter a number: ").strip()

    if action_choice == "1":
        result = chain.get_latest_block()

        print(f"Latest block: {result}")

    elif action_choice == "2":
        print("Get block")

    elif action_choice == "3":
        print("Get transaction")

    elif action_choice == "4":
        print("Get balance")

    else:
        print("Invalid action.")


if __name__ == "__main__":
    main()

