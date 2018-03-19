from coinbase.wallet.client import Client
# import coinbase
class Coinbase(object):

	def __init__(self, api_key=None, api_secret=None):
		self.api_key = api_key
		self.api_secret = api_secret
		if self.api_key and self.api_secret:
			self.__client = Client(self.api_key, self.api_secret)
		else:
			self.__client = None

	def __get_client(self):
		if not self.__client:
			self.__client = Client(self.api_key, self.api_secret)
		return self.__client

	def buy_price(self, currency_pair = 'BTC-USD'):
		client = self.__get_client()
		return client.get_buy_price(currency_pair = currency_pair)

	def sell_price(self, currency_pair = 'BTC-USD'):
		client = self.__get_client()
		return client.get_sell_price(currency_pair = currency_pair)

	def spot_price(self, currency_pair = 'BTC-USD'):
		client = self.__get_client()
		return client.get_spot_price(currency_pair = currency_pair)

	def buy_limit(self, limit, currency_pair):
		if not limit or currency_pair:
			raise ValueError('Limit or Currency pair not provided')

		#buy limit logic will go here

	def sell_limit(self, limit, currency_pair):

		if not limit or currency_pair:
			raise ValueError('Limit or Currency pair not provided')

		# sell limit logic will go here

	# TODO: create a thread, service or background process for checking limit
	## allow option to select checking period, like: 0.5s, 1s, 5s, etc.

# user = client.get_current_user()
# user_as_json_string = json.dumps(user)
# print(user_as_json_string)

# accounts = client.get_accounts()
# print(accounts)
#https://github.com/coinbase/coinbase-python