from django.contrib import admin
from django.urls import path, include

from main.views import index, edit

urlpatterns = [
    path('', index, name='home'),
    path('edit/<int:post_pk>', edit, name='edit')
]
