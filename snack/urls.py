from django.urls import path
from . import views

app_name = 'snack'

urlpatterns = [
    path('', views.index, name='index'),
    path('snack/request_create/', views.request_create,
         name='request_create'),
    path('request/modify/<int:snack_id>/', views.request_modify,
         name='request_modify'),
    path('request/delete/<int:snack_id>/', views.request_delete, 
         name='request_delete'),
]
