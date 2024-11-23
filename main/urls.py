from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.first_page,name="fisrt_page"),
    path('<int:pk>/',views.store_page,name="store_page"),
    path('store_list',views.store_list,name="store_list"),
    path('change/<int:pk>/',views.change,name="change"),
    path('add',views.add,name="add"),
]