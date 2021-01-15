from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fiber/', views.fiber_index, name='fiber_index')
]