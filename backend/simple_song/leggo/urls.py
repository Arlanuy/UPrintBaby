from django.conf.urls import patterns, url
from leggo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
