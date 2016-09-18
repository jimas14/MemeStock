from django.http import HttpResponse

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

    def calc_value(self, meme):
        return 0