from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('userindex',views.userindex,name='userindex'),
    path('products',views.products,name='products'),
    path('sortprod/<str:cat>',views.sortprod,name='sortprod'),
    path('contact',views.contact,name='contact'),
    path('loginusers',views.loginusers,name='loginusers'),
    path('register',views.register,name='register'),
    path('login_view_user',views.login_view_user,name='login_view_user'),
    path('create_user',views.create_user,name='create_user'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('productdetails/<int:id>',views.productdetails,name='productdetails'),
    path('cart',views.cart,name='cart'),
    path('cartdata/<int:id>',views.cartdata,name='cartdata'),
    path('cart1',views.cart1,name='cart1'),
    path('cartremove/<int:id>',views.cartremove,name='cartremove'),
    path('my_ajax_view',views.my_ajax_view,name='my_ajax_view'),
    path('checkout',views.checkout,name='checkout'),
    path('checkoutdata',views.checkoutdata,name='checkoutdata'),
    path('contactform',views.contactform,name='contactform'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('search',views.search,name='search'),
]