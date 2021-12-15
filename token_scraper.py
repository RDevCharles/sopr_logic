import os
from dotenv import load_dotenv
from supabase_py import create_client, Client
from pycoingecko import CoinGeckoAPI
import requests
import datetime
import time

load_dotenv()


cg = CoinGeckoAPI()
ETHERSCAN_APIKEY = os.getenv("ETHERSCAN_API_KEY")

url: str = "https://lgmimcqspaefngdfzrwq.supabase.co"
key: str = os.getenv("SUPABASE_SECRET_KEY")
supabase: Client = create_client(url, key)


#SUPABASE FUNCTIONS

#SHITCOIN LIST

listdata = supabase.table('coin_list').select('name').execute()
print(listdata)
for h in listdata['data']:
    for j in h:
        gas_price_req = requests.get(
            f'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={ETHERSCAN_APIKEY}')
        gas_price_res = gas_price_req.json()['result']['SafeGasPrice']
        coin_address_req = cg.get_coin_by_id(h[j])
        coin_address_res = coin_address_req['platforms']['ethereum']
        coin_price_req = cg.get_price(
            ids=h[j], vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true')

        total_supply_req = requests.get(
            f'https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress={coin_address_res}&apikey={ETHERSCAN_APIKEY}')
        total_supply_res = total_supply_req.json()['result']

        #SOPR TRANSLATED INTO COLORS
        if 0 > coin_price_req[h[j]]['usd_24h_vol'] / coin_price_req[h[j]]['usd_24h_change']:
            score_color = 'red'
        else:
            score_color = 'green'
        ct = str(datetime.datetime.now())

        #SUPABASE UPLOAD
        data = supabase.table("alts").insert({"name": h[j], "address": coin_address_res, "info": coin_price_req[h[j]],
                                              "supply": total_supply_res, "gas": gas_price_res, "timestamp": ct, "color": score_color}).execute()
        assert len(data.get("data", [])) > 0


#SUBTRACT WHALE MARKETCAP EFFECT
