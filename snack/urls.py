from django.urls import path

from . import views

app_name = 'snack'

urlpatterns = [
    path('', views.index, name='index'),
    path('snack/request_create/', views.snack_request_create,
         name='snack_request_create'),
]
