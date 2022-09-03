from dataclasses import field
from rest_framework import serializers
from app.models import Batches, Specializations, Students, Semesters, Subjects, Results
from app.authmodels import Users


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


class GetResultSerializer(serializers.ModelSerializer):
    batch_id = BatchSerializer(many=False, read_only=True)
    student_id = StudentSerializer(many=False, read_only=True)
    semester_id = SemesterSerializer(many=False, read_only=True)
    subject_id = SubjectSerializer(many=False, read_only=True)
    specialization_id = SpecializationSerializer(many=False, read_only=True)

    class Meta:
        model = Results
        fields = (
            'id',
            'student_id',
            'batch_id',
            'semester_id',
            'marks_obtained',
            'subject_id',
            'specialization_id'
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
            'subject_id',
            'specialization_id'
        )
