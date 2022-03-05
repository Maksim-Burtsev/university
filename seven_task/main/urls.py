from django.urls import path, include

from main.views import index, test


urlpatterns = [
    path ('', index, name='home'),
    path('test', test, name='test')
]
