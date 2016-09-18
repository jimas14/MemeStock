
from django.conf.urls import patterns, url

#from thinkster_django_angular_boilerplate.views import IndexView
from thinkster_django_angular_boilerplate import views
from thinkster_django_angular_boilerplate.views import indexView, investmentsView, transactionsView

# urlpatterns = patterns(
#    '',
#    #url(r'^.*$', IndexView.as_view(), name='index'),
#    url(r'^(?P<meme_name>\w{0,50})/$', views.get_results, name='get_results')
#    url('^.*$', indexView, name='index'),
#    url('^.*$', InvestmentsView.as_view(), name='invesments')
# )

urlpatterns = [
    url(r'^$', indexView, name='index'),
    url(r'^investments', investmentsView, name='investments'),
    url(r'^transactions', transactionsView, name='transactions'),
	url(r'^(?P<meme_name>\w{0,50})/$', views.get_results, name='get_results')
    #url(r'^login', loginView, name='login'),
    #url(r'^logout', logoutView, name='logout')
]