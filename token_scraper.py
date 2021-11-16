import os
from dotenv import load_dotenv
from supabase_py import create_client, Client
from pycoingecko import CoinGeckoAPI
import requests
import datetime;

load_dotenv()


cg = CoinGeckoAPI()
INFURA_APIKEY = os.getenv("INFURA_API_KEY")
ETHERSCAN_APIKEY = os.getenv("ETHERSCAN_API_KEY")


#shitcoin list
shitcoin_list = ['floki-inu', 'shiba-inu', 'saitama-inu']

#all the data being sent to database

#while True:
def main():
    for i in shitcoin_list:
        gas_price_req = requests.get(
            f'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={ETHERSCAN_APIKEY}')
        gas_price_res = gas_price_req.json()['result']['SafeGasPrice']
        coin_address_req = cg.get_coin_by_id(i)
        coin_address_res = coin_address_req['platforms']['ethereum']
        coin_price_req = cg.get_price(
            ids=i, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true')
      
        total_supply_req = requests.get(
            f'https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress={coin_address_res}&apikey={ETHERSCAN_APIKEY}')
        total_supply_res = total_supply_req.json()['result']
        ct = str(datetime.datetime.now())
        url: str = os.getenv("SUPABASE_URL")
        key: str = os.getenv("SUPABASE_SECRET_KEY")
        supabase: Client = create_client(url, key)
        data = supabase.table("alts").insert({"name":i, "address" :coin_address_res, "info" : coin_price_req, "supply":total_supply_res, "gas" : gas_price_res, "timestamp":ct }).execute()
        assert len(data.get("data", [])) > 0

main()
#time.sleep(3)

#manually input holders for more than 30 days
#profit/ break even / loss
