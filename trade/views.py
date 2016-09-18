from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from pytrends.request import TrendReq
import json
#from django.template import RequestContext
#from django.contrib.auth.models import User


def get_results(request, meme_name):
	google_username = 'memestocks9000'
	google_password = 'memesrule1'

	pytrend = TrendReq(google_username, google_password, custom_useragent=None)

	payload = {
		'q' : meme_name,
		'date': 'today 1-d'
	}

	output = pytrend.trend(payload)

	return HttpResponse(json.dumps(output), content_type="application/json")


# get request - get specific users' investments
# get request - get all investments
# post - to coinbase api

#user = User.objects.create_user(username='user')
#user.save()

def indexView(request):
    #request_context = RequestContext(request)

    return render(request,'index.html')

def investmentsView(request):
    #request_context = RequestContext(request)

    context = {'investments': True}
    return render(request,'investments.html', context)

def transactionsView(request):

    context = {'transactions': True}
    return render(request,'transactions.html', context)
