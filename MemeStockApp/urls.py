from django.conf.urls import patterns, url
from trade.views import IndexView, InvestmentsView, TransactionsView
from trade import views

urlpatterns = [
    url(r'^$', IndexView, name='index'),
    url(r'^investments', InvestmentsView, name='investments'),
    url(r'^transactions', TransactionsView, name='transactions'),

	url(r'^(?P<meme_name>\w{0,50})/$', views.get_results, name='get_results'),

	url(r'^login_info$', views.save_user, name='save_user'),
	url(r'^buy_sell$', views.buy_sell, name='buy_sell'),

	url(r'^get_user_stocks/(?P<username>\w{0,50})/$', views.get_user_stocks, name='get_user_stocks'),
	url(r'^get_all_stocks$', views.get_all_stocks, name='get_all_stocks')
]