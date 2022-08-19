from django.urls import re_path
from app import views


urlpatterns = [
    re_path(r'^batches', views.batchApi),
    re_path(r'^specialization', views.specializationApi), 
    re_path(r'^users', views.userApi),
    re_path(r'^students', views.studentApi),
    re_path(r'^semesters', views.semesterApi),
    re_path(r'^subjects', views.subjectApi),
    re_path(r'^results',views.resultApi),
]
