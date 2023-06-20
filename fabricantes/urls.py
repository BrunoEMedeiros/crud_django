from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('fabricantes/', views.fabricantes, name='fabricantes'),    
    path('fabricantes/details/<int:id>', views.details, name='details'),
    path('fabricantes/add/', views.add, name='add'),
    path('fabricantes/add/addrecord/', views.addrecord, name='addrecord'),
    path('fabricantes/delete/<int:id>', views.delete, name='delete'),
    path('fabricantes/update/<int:id>', views.update, name='update'),
    path('fabricantes/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord')
]