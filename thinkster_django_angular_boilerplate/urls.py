from django.conf.urls import patterns, url

#from thinkster_django_angular_boilerplate.views import IndexView
from thinkster_django_angular_boilerplate import views

urlpatterns = patterns(
    '',

    #url(r'^.*$', IndexView.as_view(), name='index'),
    url(r'^(?P<meme_name>\w{0,50})/$', views.get_results, name='get_results')
)
