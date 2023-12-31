from django.urls import path
from .views import home, adicionar

urlpatterns = [
    path('', home, name='home'),
    path('adicionar/', adicionar, name='adicionar'),
]
