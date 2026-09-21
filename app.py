import os
from dotenv import load_dotenv
load_dotenv()

RPC_ETHEREUM_MAINNET_URL = os.getenv("RPC_ETHEREUM_MAINNET_URL")
RPC_SOLANA_MAINNET_URL = os.getenv("RPC_SOLANA_MAINNET_URL")
RPC_BITCOIN_MAINNET_URL = os.getenv("RPC_BITCOIN_MAINNET_URL")
RPC_BASE_MAINNET_URL = os.getenv("RPC_BASE_MAINNET_URL")

BLOCKCHAINS = {
    "1": "eth",
    "2": "sol",
    "3": "bitcoin",
    "4": "base",
    "5": "tron",
    "6": "xrp",
    "7": "dogecoin",
    "8": "cardano",
}




#class Eth

# what do i want
# from terminal i can enter numbers to correspond with actions:
# 1) eth 2) sol 3) bitcoin 4) base 5) tron 6) xrp 7) dogecoin 8) cardano 


# a) transactions b) ......

# make each chain a class and import it? 





if __name__ == '__main__':

    for number, blockchain in BLOCKCHAINS.items():
        print(f"{number}) {blockchain}")

    while True:
        choice = input("Enter a number (1-8): ").strip()
        if choice in BLOCKCHAINS:
            print(BLOCKCHAINS[choice])
            break
        print("Wrong input, please enter a digit from 1 to 8.")
