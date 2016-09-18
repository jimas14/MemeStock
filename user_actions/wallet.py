from coinbase.wallet.client import Client
from django.http import HttpResponse
from django.http import HttpRequest
from user_actions.investments import Investments

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
    get.
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