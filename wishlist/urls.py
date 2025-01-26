from django.urls import path
from .views import wishlist_view, wishlist_add_json, wishlist_del_json, wishlist_json, wishlist_del_view
from store.views import products_page_view

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist_view, name='wishlist_view'),
    path('wishlist/del/<str:id_product>', wishlist_del_view, name='wishlist_del_view'),
    path('product/<slug:page>.html', products_page_view, name="product_page_view"),
    path('product/<int:page>', products_page_view),
    path('api/del/<str:id_product>', wishlist_del_json, name="wishlist_del_json"),
    path('api/add/<str:id_product>', wishlist_add_json, name = "wishlist_add_json"),
    path('api/', wishlist_json, name="wishlist_json"),


]