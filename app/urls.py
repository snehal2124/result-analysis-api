from django.urls import re_path
from app import views

urlpatterns = [
    re_path(r'^batches$', views.batchApi),
    re_path(r'^batches/([0-9]+)$', views.batchApi),
    re_path(r'^specializations$', views.specializationApi),
    re_path(r'^specializations/([0-9]+)$', views.specializationApi),
    re_path(r'^users$', views.userApi),
    re_path(r'^users/([0-9]+)$', views.userApi),
    re_path(r'^students$', views.studentApi),
    re_path(r'^students/([0-9]+)$', views.studentApi),
    re_path(r'^subjects', views.subjectApi),
    re_path(r'^bulk-results', views.bulkResultApi),
    re_path(r'^results', views.resultApi),
    re_path(r'^results/([0-9]+)$', views.resultApi),
    re_path(r'^semesters$', views.semesterApi),
    re_path(r'^semesters/([0-9]+)$', views.semesterApi),
    re_path(r'^result-batch', views.batchResult),
    re_path(r'^result-subject', views.subjectResult),
]
