from django.urls import path

from main.views import index, add    

urlpatterns = [
    path('', index, name='home'),
    path('add/', add, name='add')
]
