from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo_list, name="list"),
    path('update_task/<str:pk>/', views.update_task, name="update"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete")
]
