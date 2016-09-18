from models import User, Investment

class Data:
	def __init__(self):
		self.users_list = {}

	def add_user(self, user):
		self.users_list[user.username] = []

	def add_investment_to_user(self, user, investment):
		user_investments = self.users_list[user.username]

		user_investments.append(investment)

	def get_user_stocks(self, user):
		for loop_user in self.users_list:
			if loop_user.username == user.username:
				return loop_user.investments

	def get_all_stocks(self):
		new_list = []

		for loop_user in self.users_list:
			new_list.append(loop_user.investments)

		return new_list

	def update_current_data(self, days):
		google_username = 'memestocks9000'
		google_password = 'memesrule1'

		pytrend = TrendReq(google_username, google_password, custom_useragent=None)

		payload = {
			'q' : meme_name,
			'date': 'today '+days+'-d'
		}

		output = pytrend.trend(payload)



		return HttpResponse(json.dumps(output), content_type="application/json")