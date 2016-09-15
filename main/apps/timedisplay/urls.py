from django.conf.urls import url
from . import views           # This line is new!

#controller

urlpatterns = [
    url(r'^$', views.index),
    url(r'^time$', views.index)     # This line has changed!
  ]
