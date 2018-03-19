from Coinbase import Coinbase
import os 

api_key = os.environ.get('api_key')
api_secret = os.environ.get('api_secret')
coinbase = Coinbase(api_key, api_secret)
# print(coinbase.buy_price('BTC-USD'))
# print(coinbase.buy_price('ETH-USD'))
# print(coinbase.buy_price('LTC-USD'))

# print(coinbase.spot_price('BTC-USD'))
# print(coinbase.spot_price('ETH-USD'))
print(coinbase.spot_price('LTC-USD'))
# coinbase.buy_limit()

coinbase2 = Coinbase()
coinbase2.api_key = api_key
coinbase2.api_secret = api_secret
print(coinbase2.buy_price('BTC-USD'))
# print(coinbase2.buy_price('ETH-USD'))
# print(coinbase2.buy_price('LTC-USD'))