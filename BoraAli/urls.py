# from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:trilha_id>', views.trilha, name='trilha'),
    path('trilha_add', views.trilha_add, name='trilha_add'),

    path('trilha_edit/<int:trilha_id>', views.trilha_edit,name="trilha_edit"),
    
    path('trilha/<int:trilha_id>', views.trilha_del, name='trilha_del'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('modificacao', views.modificacao, name='modificacao'),
]
