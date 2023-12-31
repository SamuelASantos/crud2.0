from django.urls import path
from .views import home, adicionar, editar, update, deletar

urlpatterns = [
    path('', home, name='home'),
    path('adicionar/', adicionar, name='adicionar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('deletar/<int:id>', deletar, name='deletar'),
]
