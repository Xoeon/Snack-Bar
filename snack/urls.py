from django.urls import path

from . import views

app_name = 'snack'

urlpatterns = [
    path('', views.index, name='index'),
    path('snack/request_create/', views.request_create,
         name='request_create'),
]
