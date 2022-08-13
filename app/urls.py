from django.urls import re_path
from app import views


urlpatterns = [
    re_path(r'^batch', views.batchApi),
    re_path(r'^specialization', views.specializationApi),
]
