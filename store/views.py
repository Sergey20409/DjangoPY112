from django.shortcuts import render
from django.http import JsonResponse
from .models import DATABASE


def products_view(request):
    if request.method == "GET":

        return  JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})# Вернуть JsonResponse с объектом DATABASE и параметрами отступов и кодировок,
        # как в приложении app_weather
# Create your views here.
