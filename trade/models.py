from django.db import models
from django.http import HttpResponse
from django.http import HttpRequest
from coinbase.wallet.client import Client

class Investment:
    def __init__(self, name, shares):
        self.name = name
        self.shares = shares
        self.start = 0
        self.current = 0

class User:
    def __init__(self, username):
        self.username = username
        self.investments = {}

    def buy(self, meme, shares):
        if self.investments.has_key(meme):
            self.investments[meme].shares += shares
            self.investments[meme].current = User.calc_value(meme)
        else:
            self.investments[meme] = Investment(meme, shares)
            val = User.calc_value(meme)
            self.investments[meme].start = val
            self.investments[meme].current = val
        return HttpResponse("%d shares added to %s." % (shares, meme))

    def sell(self, meme, shares):
        if self.investments.has_key(meme):
            if self.investments[meme].shares >= shares:
                self.investments[meme].shares -= shares
                if self.investments[meme].shares == 0:
                    del self.investments[meme]
                else:
                    self.investments[meme].current = User.calc_value(meme)
                return HttpResponse("%d shares removed from %s." % (shares, meme))
            else:
                return HttpResponse("Only %d shares of %s are owned." % (shares, meme), status=400)
        else:
            return HttpResponse("No shares of %s are owned." % meme, status=400)

    def current_value(self, meme):
        if self.investments.has_key(meme):
            val = User.calc_value(meme)
            self.investments[meme].current = val
            return val
        else:
            return HttpResponse("No shares of %s are owned." % meme, status=400)

    def calc_value(self, meme, date):
        user_investments = self.investments

        for loop_investment in user_investments:
        	if loop_investment.name == meme:
        		chosen_investment = loop_investment

        # write get_all_investments
        all_investments = get_all_investments()
        ratio = {}
        trend_score = {}
        total_trend_score = 0
        valuation = 0

        for loop_investment in all_investments:
        	if loop_investment.current >= 0 && loop_investment.start >= 0:

        		# call some function update_current(meme, date)

        		# assuming two users can't buy shares in the same exact meme name at once
        		ratio[loop_investment.name] = loop_investment.current / loop_investment.start

        		trend_score[loop_investment.name] = ratios[loop_investment.name] * loop_investment.current

        		total_trend_score += trend_score[loop_investment.name]


        valuation = trend_score[loop_investment] / total_trend_score

        return valuation


class Wallet:
	def __init__(self, investments, values):
	    self.client = Client("TGSWzRvFLeVCsW1W", "wYVR9Zckm2Jb4UFzoBJ6W3cQHLmtl23u")
	    self.account = self.client.create_acount(name="Meme Wallet")
	    self.balance = self.account.balance
	    self.address = self.account.create_address()
	    self.investments = Investments(investments, values)
	    self.values = values

	def invest(self, name, meme, shares, address):
	    cost = self.values[meme] * shares
	    get = HttpRequest()
	    get.method = 'GET'
	    get.build_absolute_uri('https://www.coinbase.com/oauth/authorize?client_id=9c73633f55257dcf698fd49a9159bb9eced' +
	                            '779098abedeaf106bf00674686bc0&redirect_uri=http%3A%2F%2Flocalhost%3A8000' +
	                            '&response_type=code&scope=wallet%3Auser%3Aread')
	    #get.
	    self.investments.buy(name, meme, shares)

	def withdraw(self, name, meme, shares, address):
	    if self.investments.contains_key(name):
	        if self.investments[name].contains_key(meme):
	            if self.investments[name][meme] >= shares:
	                cost = self.values[meme] * shares
	                self.investments.sell(name, meme, shares)
	                return HttpResponse("%s BTC sent to account %s. %d shares of %s taken." % (cost, name, shares, meme))
	            else:
	                return HttpResponse("User %s only owns %d shares of %s." % (name, shares, meme), status=400)
	        else:
	            return HttpResponse("User %s has no shares in %s." % (name, meme), status=400)
	    else:
	        return HttpResponse("Username %s not found." % name, status=400)

