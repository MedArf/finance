import alpaca
import configparser
from alpaca.broker.client import BrokerClient
from alpaca.broker.requests import ListAccountsRequest
from alpaca.broker.enums import AccountEntities



api_key=''
api_secret=''
config_file="/home/mehdi/Projects/finance/AI_Trading_Assistant/api/degiro/config/config.json"
def get_credentials_info():
    global api_key, api_secret
    config=configparser.ConfigParser()
    config.read(config_file)
    api_key=config['apikeys']['APCA-API-KEY']
    api_secret=config['apikeys']['APCA-API-SECRET']
    print('APCA-API-KEY:' + api_key)


get_credentials_info()
broker_client=BrokerClient(api_key, api_secret)
print(broker_client)
#print(broker_client.get_calendar())
#conn=http.client.HTTPSConnection("")
#resp=conn.request("GET","/www.degiro.com/")
#'https://trader.degiro.nl/myracloud-captcha/securimage_neu/securimage_show.php?1d412ff005b0ba04e42348ae450d6b4b'

trading_client = TradingClient(api_key, api_secret)
