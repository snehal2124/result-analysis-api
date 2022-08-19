from django.urls import re_path
from app import views


urlpatterns = [
<<<<<<< HEAD
    re_path(r'^batches', views.batchApi),
    re_path(r'^specialization', views.specializationApi), 
=======
    re_path(r'^batches$', views.batchApi),
    re_path(r'^batches/([0-9]+)$', views.batchApi),
    re_path(r'^specializations$', views.specializationApi),
    re_path(r'^specializations/([0-9]+)$', views.specializationApi),
>>>>>>> 4edfa78d217cef28b1008028a647931b33faaabb
    re_path(r'^users', views.userApi),
    re_path(r'^students', views.studentApi),
    re_path(r'^semesters', views.semesterApi),
    re_path(r'^subjects', views.subjectApi),
    re_path(r'^results',views.resultApi),
]
