from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from pytrends.request import TrendReq
from data import Data
import json


# def get_results(request, meme_name):
# 	google_username = 'memestocks9000'
# 	google_password = 'memesrule1'

# 	pytrend = TrendReq(google_username, google_password, custom_useragent=None)

# 	payload = {
# 		'q' : meme_name,
# 		'date': 'today 1-d'
# 	}

# 	output = pytrend.trend(payload)

# 	return HttpResponse(json.dumps(output), content_type="application/json")

def login_info(request):
	data = request.data
	username = data.user

	Data.add_user(username)

def buy_sell(request):
	data = request.data
	username = data.user
	memename = data.meme
	date = data.date
	num_shares = data.shares

	if data.method == 'buy':
    	do_something()
	elif data.method == 'sell':
    	do_something_else()

def get_user_stocks(request, username):
	data = request.data
	username = data.user

	output = Data.get_user_stocks(username)

	return HttpResponse(json.dumps(output), content_type="application/json")

def get_all_stocks(request):
	data = request.data

	output = Data.get_all_stocks()

	return HttpResponse(json.dumps(output), content_type="application/json")

def IndexView(request):
    #request_context = RequestContext(request)

    return render(request,'index.html')

def InvestmentsView(request):
    #request_context = RequestContext(request)

    context = {'investments': True}
    return render(request,'investments.html', context)

def TransactionsView(request):

    context = {'transactions': True}
    return render(request,'transactions.html', context)
