from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('update_task/<str:pk>', update_task, name='update_task'),
    path('delete_task/<str:pk>', delete_task, name='delete_task'),
]
