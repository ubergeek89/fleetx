from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'fleetxwebsite'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]