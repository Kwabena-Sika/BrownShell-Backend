from django.urls import path
from . import views

app_name ='customers'

urlpatterns = [
    path('', views.customer_list, name='customer-list'),
    path('<int:id>/', views.customer_detail, name='customer-detail'),
]