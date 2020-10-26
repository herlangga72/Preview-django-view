from .views import *
from django.urls import path, include
urlpatterns = [
    path('karyawan', karyawan_all)
]
