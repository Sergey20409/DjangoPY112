from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from  logic.services import view_in_wishlist, add_to_wishlist, remove_from_wishlist
from django.contrib.auth import get_user
from store.models import DATABASE
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login:login_view')
def wishlist_view(request):
    if request.method == "GET":
        current_user = get_user(request).username
        data = view_in_wishlist(current_user) # TODO получить продукты из избранного для пользователя

        products = [DATABASE[id_prod] for id_prod in data[current_user]['products']]  # Список продуктов
        return render(request, 'wishlist/wishlist.html', context={"products": products})

def wishlist_add_json(request, id_product: str):
    if request.method == "GET":
        result = add_to_wishlist(request, id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в избранное"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в избранное"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})

def wishlist_del_json(request, id_product: str):
    if request.method == "GET":
        result = remove_from_wishlist(request, id_product) # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён в избранное"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление в избранном"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})
@login_required(login_url='login:login_view')
def wishlist_del_view(request, id_product):
    if request.method == "GET":
        result = remove_from_wishlist(request, id_product)
        if result:
            return redirect("wishlist:wishlist_view")
        return HttpResponseNotFound("Неудачное удаление из корзины")

@login_required(login_url='login:login_view')
def wishlist_json(request):

    if request.method == "GET":
        current_user = get_user(request).username  # from django.contrib.auth import get_user
        data = view_in_wishlist(current_user) # TODO получите данные о списке товаров в избранном у пользователя
        if data:
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Пользователь не авторизирован"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})

