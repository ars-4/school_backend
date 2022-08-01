from rest_framework import serializers
from core.models import Person, SClass, Subject, Type


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'user', 'roll_no', 'image', 'email', 'phone', 'address', 's_classes', 'subjects', 'type']


class SClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SClass
        fields = ['id', 'title']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'title']
