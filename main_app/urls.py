from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fiber/', views.fiber_index, name='fiber_index'),
    path('fiber/<int:fiber_id>', views.fiber_show, name="fiber_show"),
    path('fiber/create/', views.FiberCreate.as_view(), name="fiber_create"),
    path('fiber/<int:pk>/update', views.FiberUpdate.as_view(), name="fiber_update"),
    path('fiber/<int:pk>/delete', views.FiberDelete.as_view(), name="fiber_delete"),
]