from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
]
