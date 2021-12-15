import os
from dotenv import load_dotenv
from supabase_py import create_client, Client
from pycoingecko import CoinGeckoAPI
import requests
import datetime
import time
import requests
import os


load_dotenv() 
cg = CoinGeckoAPI()
ETHERSCAN_APIKEY = os.getenv("ETHERSCAN_API_KEY") 
url: str = "https://lgmimcqspaefngdfzrwq.supabase.co"
key: str = os.getenv("SUPABASE_SECRET_KEY")
supabase: Client = create_client(url, key)





data_res = supabase.table("coin_list").select("*").execute()
addy_res = cg.get_coin_by_id('floki-inu')
data_i = data_res['data']
addy = addy_res['platforms']['ethereum']
#data = data_i['name']




r = requests.get('https://api.ethplorer.io/getTopTokenHolders/0x43f11c02439e2736800433b4594994bd43cd066d?apiKey=freekey')
holder_list = r.json()['holders']


def main():
    for k in data_i:
        c_name = k['name']
        coin_addy = cg.get_coin_by_id(k['name'])
        final_coin_addy = coin_addy['platforms']['ethereum']
        coin_r = requests.get(f'https://api.ethplorer.io/getTopTokenHolders/{final_coin_addy}/?apiKey=freekey')
        print(k['name'])
        print(coin_addy['platforms']['ethereum'])
        holder_arr = [coin_r.json()['holders'][0],coin_r.json()['holders'][1],coin_r.json()['holders'][2],coin_r.json()['holders'][3],coin_r.json()['holders'][4]]
        print(holder_arr)
        data = supabase.table("whales").insert({"name":f"{c_name}", "info":f"{holder_arr}"}).execute()
        assert len(data.get("data", [])) > 0

main()
