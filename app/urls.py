from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    url('index$', index),
    url('search$', search_av)
]
