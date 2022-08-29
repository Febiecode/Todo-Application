from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('update_task/<int:pk>/', views.updatetask, name="updatetask"),
    path('delete/<str:pk>', views.delete, name="deletetask"),
]