from django.urls import path
from . import views


urlpatterns = [
    path("", views.supplier_list, name="supplier-list"),
    path("stats/", views.supplier_stats, name="supplier-stats"),
    path("<int:id>/", views.supplier_detail, name="supplier-detail")
]