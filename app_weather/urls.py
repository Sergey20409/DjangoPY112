# urls.py in store

from django.urls import path
from .views import my_view5

urlpatterns = [
    path('weather/', my_view5),
]