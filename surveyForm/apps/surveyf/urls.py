from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveyInfo$', views.create),
    url(r'^submit$', views.giveResults),

]
