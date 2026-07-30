from django.urls import path
from .import views

app_name = 'inventory'

urlpatterns = [
    path('egg_type/', views.egg_type_list, name='egg_type_list')
]