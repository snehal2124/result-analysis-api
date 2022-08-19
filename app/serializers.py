from dataclasses import field
from rest_framework import serializers
from app.models import Batches,  Specializations, Users, Students,Semesters,Subjects,Results
   
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = (
            'id',
            'name',
            'start_year',
            'end_year',
            'code',
            'specialization_id'
        )


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializations
        fields = (
            'id',
            'name',
            'code',
            'no_of_years',
            'no_of_semesters'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'mobile',
            'password',
            'address',
            'type'
        )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'mobile',
            'roll_no',
            'address',
        )

        


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = (
             'id',
             'name',
             'code',
             'total_marks',
             'semester_id',
        )

        
class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = (
            'id',
            'name',
            'code',
            'batch_id',
            'specialization_id',
        )

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = (
            'id', 
            'student_id',
            'batch_id',
            'semester_id',
            'marks_obtained',
        )      