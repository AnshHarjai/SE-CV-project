from django.urls import path
from .views import cv_view

urlpatterns = [
    path('', cv_view, name='cv_root'),
    path('cv/', cv_view, name='cv'),
]
