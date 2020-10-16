from django.urls import path

from . import views

urlpatterns = [
    # path('', views.elixir_login,name='logpage'),
    path('', views.elixir_dashboard,name='homepage')
]