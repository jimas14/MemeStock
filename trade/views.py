from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from pytrends.request import TrendReq
import data
import json


def get_results(request, meme_name, num_days):
	google_username = 'memestocks9000'
	google_password = 'memesrule1'

	pytrend = TrendReq(google_username, google_password, custom_useragent=None)

	payload = {
		'q' : meme_name,
		'date': 'today '+num_days+'-d'
	}

	output = pytrend.trend(payload)

	info = output['table']['rows'][0]['c'][1]['f']

	return HttpResponse(json.dumps(info), content_type="application/json")

def login_info(request):

	# print request.POST
	# print request.body


	# print("\n\n\n\n\n\nfdf\n\n\n\n")
	username = ""

	if request.method == "POST":
		#data = request.data
		#username = request.body["user"]
		#username = data.user
		#user_data = username
		print("first if")
		#Data.add_user(user_data)
	elif request.method == "GET":
		#print("second if")
	 	return HttpResponse(json.dumps(username), content_type="application/json")

	#print("alll the way down")
	return HttpResponse(json.dumps(username), content_type="application/json")

def buy_sell(request):
	data = request.data
	username = data.user
	memename = data.meme
	date = data.date
	num_shares = data.shares

	return HttpResponse(json.dumps(username), content_type="application/json")

	#if data.method == 'buy':
    	#do_something()
	#elif data.method == 'sell':
    	#do_something_else()

def get_user_stocks(request, username):
	print("aiwioawd\n\n")
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
