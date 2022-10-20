# from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:trilha_id>', views.trilha, name='trilha'),
    path('trilha_add', views.trilha_add, name='trilha_add'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
