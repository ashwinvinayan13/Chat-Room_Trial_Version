from django.urls import path
from chat import views

urlpatterns=[
    path('', views.home, name='home'),
    path('chat/', views.lobby, name='lobby')
]