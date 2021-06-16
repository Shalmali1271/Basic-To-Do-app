from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "list"), 
    path('Update_task/<str:pk>/', views.updateTask, name = "Update_task"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete"),
]