from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^seeNinja$', views.allNinjas),
    url(r'^seeNinja/(?P<color>.*)$', views.ninja)
]
