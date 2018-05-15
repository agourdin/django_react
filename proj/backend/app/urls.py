from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListModelExample.as_view()),
    path('<int:pk>/', views.DetailModelExample.as_view()),
]
