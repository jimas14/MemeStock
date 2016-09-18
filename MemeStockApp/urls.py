
from django.conf.urls import patterns, url

#from MemeStock.views import IndexView
from trade.views import IndexView, InvestmentsView, TransactionsView

# urlpatterns = patterns(
#    '',
#    #url(r'^.*$', IndexView.as_view(), name='index'),
#    url(r'^(?P<meme_name>\w{0,50})/$', views.get_results, name='get_results')
#    url('^.*$', indexView, name='index'),
#    url('^.*$', InvestmentsView.as_view(), name='invesments')
# )

urlpatterns = [
    url(r'^$', IndexView, name='index'),
    url(r'^investments', InvestmentsView, name='investments'),
    url(r'^transactions', TransactionsView, name='transactions'),
	url(r'^(?P<meme_name>\w{0,50})/$', views.get_results, name='get_results')
    #url(r'^login', loginView, name='login'),
    #url(r'^logout', logoutView, name='logout')
]