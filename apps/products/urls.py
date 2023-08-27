from django.urls import path
from .views import product_list,product_new,category_list

urlpatterns = [    
    path('',product_list ,name='product_list'),
    path('new/',product_new,name='product_new'),
    path('category/',category_list,name="category_list")
]