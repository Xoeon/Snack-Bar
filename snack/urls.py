from django.urls import path

from .views import base_views, request_views

app_name = 'snack'

urlpatterns = [
    #base_views.py
    path('', base_views.index, name='index'),

    #request_views.py
    path('snack/request_create/', request_views.request_create,
         name='request_create'),
    path('snack/modify/<int:snack_id>/', request_views.request_modify,
         name='request_modify'),
    path('snack/delete/<int:snack_id>/', request_views.request_delete, 
         name='request_delete'),
]
