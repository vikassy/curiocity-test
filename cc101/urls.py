from django.conf.urls import patterns, url

from cc101 import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)