from django.urls import path
from stage1 import views

urlpatterns = [
    path('api/stage1', views.details)
]