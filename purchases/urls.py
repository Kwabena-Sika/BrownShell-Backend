from django.urls import path
from . import views

app_name = 'purchases'

urlpatterns = [
    path('', views.purchase_list, name='purchase_list'),
    path('<int:id>/', views.purchase_detail, name='purchase_detail'),
    path('items/', views.purchase_item_list, name='purchase_item_list'),
    path('<int:id>/', views.purchase_item_detail, name='purchase_item_detail')
]