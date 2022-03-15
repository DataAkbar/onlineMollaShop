from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cat/', views.product_catalog, name='cat'),
    path('wishlist/', views.wishlist, name='wishlist'),
    # path('detail/', views.product_detail, name='product-detail'),
    path('category-market/', views.catigory_market, name='category_market'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
]
