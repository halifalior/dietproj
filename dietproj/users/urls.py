from django.conf.urls import url , include
from . import views

urlpatterns = [
    url('accounts/',include("django.contrib.auth.urls")),
    url('profile/', views.edit_profile, name="edit_profile"),
    url('', views.home, name="home"),
]