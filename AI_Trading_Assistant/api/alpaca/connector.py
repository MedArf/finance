from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
import configparser

ALPACA_ENV=''
def set_env():
    global ALPACA_ENV
    ALPACA_ENV="paper"
#to be replaced with entries in DB

set_env()
config_file="/home/mehdi/Projects/finance/AI_Trading_Assistant/api/alpaca/config.json"
config=configparser.ConfigParser()
config.read(config_file)

api_key=config[ALPACA_ENV+'api_keys']['APCA-API-KEY']
api_secret=config[ALPACA_ENV+'api_keys']['APCA-API-SECRET']

is_simulation = True if ALPACA_ENV == 'paper' else False
trading_client=TradingClient(api_key, api_secret, paper=is_simulation)
print(trading_client.get_account())
