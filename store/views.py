from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE
from logic.services import filtering_category

def products_view(request):
    if request.method == "GET":
        id = request.GET.get('id')
        if id:
            for i, values in DATABASE.items():
                if int(id) == values ['id']:
                    return JsonResponse(DATABASE[i], json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")
        category_key = request.GET.get('category')
        data = None
        if ordering_key := request.GET.get("ordering"):  # Если в параметрах есть 'ordering'
            if request.GET.get("reverse") and request.GET.get('reverse').lower()  == 'true':
                data = filtering_category(DATABASE, category_key, ordering_key, reverse=True)
            else:
                data = filtering_category(DATABASE, category_key, ordering_key, reverse=False)
        else:
            data = filtering_category(DATABASE, category_key)
        if data:
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4}, safe=False)
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
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

from logic.services import view_in_cart, add_to_cart, remove_from_cart


def cart_view(request):
    if request.method == "GET":
        data = view_in_cart()  # TODO Вызвать ответственную за это действие функцию
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


def cart_add_view(request, id_product):
    if request.method == "GET":
        result = add_to_cart(id_product) # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def cart_del_view(request, id_product):
    if request.method == "GET":
        result = remove_from_cart(id_product) # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})
