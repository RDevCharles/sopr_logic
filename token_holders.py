import os
from dotenv import load_dotenv
from supabase_py import create_client, Client
from web3 import Web3
from pycoingecko import CoinGeckoAPI
import requests


load_dotenv()


cg = CoinGeckoAPI()
INFURA_APIKEY = os.getenv("INFURA_API_KEY")
ETHERSCAN_APIKEY = os.getenv("ETHERSCAN_API_KEY")
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_APIKEY}'))

url: str = os.environ.get("SUPABASE_TEST_URL")
key: str = os.environ.get("SUPABASE_TEST_KEY")
supabase: Client = create_client(url, key)



    #add missing variables
def database_pull():
    data = supabase.table('token_info').get({'token': shitcoin.a,
                                                'address': shitcoin.a,
                                                'price': shitcoin.p,
                                                'total_supply': shitcoin.s,
                                                'supply_balance': shitcoin.b,
                                                'market_activity': shitcoin.m}).execute()

        #assert if insert response is a success
        assert data.get("status_code") in (200, 201)

#manually input holders for more than 30 days

#log transaction of non zero address
#log profit of specific token
#two scripts for logic

#profit/ break even / loss
