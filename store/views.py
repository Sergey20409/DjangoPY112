from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE


def products_view(request):
    if request.method == "GET":
        ID = request.GET.get('id')
        if ID:
            if ID in DATABASE:
                return JsonResponse(DATABASE[ID], json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4})
            else:
                return HttpResponseNotFound("Данного продукта нет в базе данных")
        else:
            return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                             'indent': 4})


# Create your views here.
from django.http import HttpResponse

def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ

def products_page_view(request, page):
    if request.method == "GET":
        for data in DATABASE.values():
            if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла
                with open(f'store/products/{page}.html', encoding="utf-8") as f:
                    data = f.read()
                return HttpResponse(data)
        # TODO 1. Откройте файл open(f'store/products/{page}.html', encoding="utf-8") (Не забываем про контекстный менеджер with)
        # TODO 2. Прочитайте его содержимое
        # TODO 3. Верните HttpResponse c содержимым html файла

        # Если за всё время поиска не было совпадений, то значит по данному имени нет соответствующей
        # страницы товара и можно вернуть ответ с ошибкой HttpResponse(status=404)
        return HttpResponse(status=404)

def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
           # TODO Вставьте сюда тот код, что был ранее для обработки типа slug в products_page_view
           with open(f'store/products/{page}.html', encoding="utf-8") as f:
               data = f.read()
           return HttpResponse(data)

        elif isinstance(page, int):
            data = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
            if data:  # Если по данному page было найдено значение
                with open(f'store/products/{data["html"]}.html', encoding="utf-8") as f:
                    data = f.read()
                return HttpResponse(data)
                # TODO 1. Откройте файл open(f'store/products/{data["html"]}.html', encoding="utf-8") (Не забываем про контекстный менеджер with)
                # TODO 2. Прочитайте его содержимое
                # TODO 3. Верните HttpResponse c содержимым html файла

        return HttpResponse(status=404)
