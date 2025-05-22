from django.urls import path
from todo import views

urlpatterns = [
    path("", views.home, name="home"),
    path("filter", views.filter, name="filter"),
    path("task/add", views.add_task, name="add_task"),
    path("task/update/<int:pk>", views.update_task, name="update_task"),
    path("task/delete/<int:pk>", views.delete_task, name="delete_task"),
]
