from django.conf.urls import url
from . import views

urlpatterns = [
    url('add_word$', views.add_word),
    url('clear$', views.clear),
    url(r'$', views.index),
]
