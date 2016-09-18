
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
#from django.template import RequestContext
#from django.contrib.auth.models import User



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