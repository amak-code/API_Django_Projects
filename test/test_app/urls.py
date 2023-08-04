from . import views
from django.urls import path

urlpatterns = [
    path('first/', views.first)
]
