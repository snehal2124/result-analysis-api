from django.contrib import admin
from .models import Results, Subjects, Semesters, Specializations, Students

# Register your models here.
admin.site.register(Results)
admin.site.register(Subjects)
admin.site.register(Semesters)
admin.site.register(Specializations)
admin.site.register(Students)
