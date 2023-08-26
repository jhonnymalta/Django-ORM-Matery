from django.urls import path
from .views import customers_list

urlpatterns =[
    path('',customers_list,name='customers_list')
]