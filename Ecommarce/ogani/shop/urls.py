from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('main/', views.main, name='main'),
    path('shop_details/', views.shop_details, name='shop_details'),
    path('shop_grid/', views.shop_grid, name='shop_grid'),
    path('shoping_cart/', views.shoping_cart, name='shoping_cart'),

    path('base/', views.base, name='base'),
]
