from core.models import Person, SClass, Subject, Type
from core.serializers import PersonSerializer, SClassSerializer, SubjectSerializer, TypeSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]


class SClassViewSet(ModelViewSet):
    queryset = SClass.objects.all()
    serializer_class = SClassSerializer
    permission_classes = [IsAuthenticated]


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_students(request):
    students = Person.objects.filter(type__title='Student')
    serializer = PersonSerializer(students, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student(request, pk):
    student = Person.objects.get(id=pk)
    serializer = PersonSerializer(student, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_teachers(request):
    teachers = Person.objects.filter(type__title='Teacher')
    serializer = PersonSerializer(teachers, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_teacher(request, pk):
    teacher = Person.objects.get(id=pk)
    serializer = PersonSerializer(teacher, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    users = Person.objects.all()
    serializer = PersonSerializer(users, many=True)
    return Response(serializer.data, status=HTTP_200_OK)
