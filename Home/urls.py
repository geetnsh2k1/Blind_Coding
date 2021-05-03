from django.urls import path, include
from django.conf.urls import url
from Home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save/<str:username>/', views.save),
]