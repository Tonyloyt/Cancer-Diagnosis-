from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('homepage/', views.elixir_dashboard,name="elixir_dashboard"),
    path('login/', views.elixir_login, name="elixir_login"),
    path('logout/', views.logoutUser, name="logoutUser"),

    # path('', views.elixir_login,name='logpage'),
    # path('', views.elixir_dashboard,name='homepage'),
]