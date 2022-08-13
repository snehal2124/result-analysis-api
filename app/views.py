import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app.models import Batches, Specializations
from app.serializers import BatchSerializer, SpecializationSerializer

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
        batch = Batches.objects.get(id=batch_data['id'])
        batches_serializer = BatchSerializer(batch, data=batch_data)
        if batches_serializer.is_valid():
            batches_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)


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
        batch = Specializations.objects.get(id=specialization_data['id'])
        specialization_serializer = SpecializationSerializer(
            batch, data=specialization_data)
        if specialization_serializer.is_valid():
            specialization_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
