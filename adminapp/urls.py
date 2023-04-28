from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('categoryform',views.categoryform,name='categoryform'),
    path('categorytable',views.categorytable,name='categorytable'),
    path('category',views.category,name='category'),
    path('editcategoryform/<int:id>',views.editcategoryform,name='editcategoryform'),
    path('editcategory/<int:id>',views.editcategory,name='editcategory'),
    path('deletecategory/<int:id>',views.deletecategory,name='deletecategory'),
    path('productform',views.productform,name='productform'),
    path('product',views.product,name='product'),
    path('producttable',views.producttable,name='producttable'),
    path('editproductform/<int:id>',views.editproductform,name='editproductform'),
    path('editproduct/<int:id>',views.editproduct,name='editproduct'),
    path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('login_view',views.login_view,name='login_view'),
    path('messages',views.messages,name='messages'),
]