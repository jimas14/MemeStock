from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from pytrends.request import TrendReq
import json

def get_results(request, meme_name):
	google_username = 'memestocks9000'
	google_password = 'memesrule1'

	pytrend = TrendReq(google_username, google_password, custom_useragent=None)

	payload = {
		'q' : 'harambe',
		'date': 'today 1-d'
	}

	output = pytrend.trend(payload)

	return HttpResponse(json.dumps(output), content_type="application/json")



# class IndexView(TemplateView):
#     template_name = 'index.html'

#     @method_decorator(ensure_csrf_cookie)
#     def dispatch(self, *args, **kwargs):
#         return super(IndexView, self).dispatch(*args, **kwargs)

# class IndexView(TemplateView):
#     template_name = 'index.html'

#     @method_decorator(ensure_csrf_cookie)
#     def dispatch(self, *args, **kwargs):
#         return super(IndexView, self).dispatch(*args, **kwargs)



# get request - get specific users' investments
# get request - get all investments
# post - to coinbase api