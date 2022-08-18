import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app.models import Batches, Specializations,Users,Students,Semesters
from app.serializers import BatchSerializer, SpecializationSerializer, UserSerializer, StudentSerializer,SemesterSerializer

# Create your views here.


@csrf_exempt
def batchApi(request, id=0):
    if request.method == 'GET':
        batches = Batches.objects.all()
        batches_serializer = BatchSerializer(batches, many=True)
        return JsonResponse(batches_serializer.data, safe=False)
    elif request.method == 'POST':
        batch_data = JSONParser().parse(request)
        batches_serializer = BatchSerializer(data=batch_data)
        if batches_serializer.is_valid(raise_exception=True):
            batches_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        batch_data = JSONParser().parse(request)
        batch = Batches.objects.get(id=id)
        batches_serializer = BatchSerializer(batch, data=batch_data)
        if batches_serializer.is_valid():
            batches_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        batch = Batches.objects.get(id=id)
        batch.delete()
        return JsonResponse("Delete Successfully", safe=False)


@csrf_exempt
def specializationApi(request, id=0):
    if request.method == 'GET':
        specializations = Specializations.objects.all()
        specialization_serializer = SpecializationSerializer(
            specializations, many=True)
        return JsonResponse(specialization_serializer.data, safe=False)
    elif request.method == 'POST':
        specialization_data = JSONParser().parse(request)
        specialization_serializer = SpecializationSerializer(
            data=specialization_data)
        if specialization_serializer.is_valid(raise_exception=True):
            specialization_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        specialization_data = JSONParser().parse(request)
        batch = Specializations.objects.get(id=id)
        specialization_serializer = SpecializationSerializer(
            batch, data=specialization_data)
        if specialization_serializer.is_valid():
            specialization_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        print('sdsdsdsd===================')
        print(id)
        specialization = Specializations.objects.get(id=id)
        specialization.delete()
        return JsonResponse("Delete Successfully", safe=False)

@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid(raise_exception=True):
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        Batch = Users.objects.get(id=user_data['id'])
        users_serializer = UserSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        user = Users.objects.get(id=user_data['id'])
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def studentApi(request, id=0):
    if request.method == 'GET':
        students = Students.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        students_serializer = StudentSerializer(data=student_data)
        if students_serializer.is_valid(raise_exception=True):
            students_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Students.objects.get(id=student_data['id'])
        students_serializer = StudentSerializer(student, data=student_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        student = Students.objects.get(id=student_data['id'])
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def semesterApi(request, id=0):
    if request.method == 'GET':
        semesters = Semesters.objects.all()
        semesters_serializer = SemesterSerializer(semesters, many=True)
        return JsonResponse(semesters_serializer.data, safe=False)
    elif request.method == 'POST':
        semester_data = JSONParser().parse(request)
        semesters_serializer = SemesterSerializer(data=semester_data)
        if semesters_serializer.is_valid(raise_exception=True):
            semesters_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        semster_data = JSONParser().parse(request)
        batch = Semesters.objects.get(id=semester_data['id'])
        semesters_serializer = SemesterSerializer(batch, data=semester_data)
        if semesters_serializer.is_valid():
            semesters_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)


