from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu_index, name="menu_index"),
    path("<int:pk>/", views.menu_detail, name="menu_detail"),
]