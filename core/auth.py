from core.models import Person, SClass, Subject
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


# Create your views here.

@api_view(['POST'])
def register_user(request):
    data = request.data
    s_classes_all = SClass.objects.all()
    subjects_all = Subject.objects.all()
    try:
        user = User.objects.create_user(
            username=data['username'], password=data['password'],
            email=data['email'], first_name=data['first_name'],
            last_name=data['last_name']
        )
        user.save()
        token = RefreshToken.for_user(user)
        person = Person.objects.create(
            user=user, roll_no="SMS_" + data['roll_no'], image=data['image'],
            email=data['email'], phone=data['phone'], address=data['address'],
            type=data['type']
        )
        for classes in s_classes_all:
            if classes.title in data['s_classes']:
                person.s_classes.add(classes)

        for subject in subjects_all:
            if subject.title in data['subjects']:
                person.subjects.add(subject)

        person.save()
        return Response({
            'message': 'User created successfully',
            'user': user.username,
            'roll_no': person.roll_no,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'address': user.address,
            'type': person.type.title,
            's_classes': [s_class.title for s_class in person.s_classes.all()],
            'subjects': [subject.title for subject in person.subjects.all()],
            'access': str(token.access_token),
            'refresh': str(token.refresh_token)
        }, status=HTTP_200_OK)

    except Exception as error:
        return Response({"error": str(error)}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    data = request.data
    user = data['username']
    password = data['password']
    for usr in User.objects.all():
        if usr.username == user:
            if usr.check_password(password) == True:
                token = RefreshToken.for_user(usr)
                person = Person.objects.get(user=usr)
                return Response({
                    'message': 'User logged in successfully',
                    'image': person.image.url,
                    'user': user,
                    'roll_no': person.roll_no,
                    'first_name': usr.first_name,
                    'last_name': usr.last_name,
                    'email': person.email,
                    'phone': person.phone,
                    'address': person.address,
                    'type': person.type.title,
                    's_classes': [s_class.title for s_class in person.s_classes.all()],
                    'subjects': [subject.title for subject in person.subjects.all()],
                    'access': str(token.access_token),
                    'refresh': str(token)
                }, status=HTTP_200_OK)
            else:
                return Response({"error": "Invalid password"}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid username"}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_user(request):
    data = request.data
    token = data['token']
    try:
        token = RefreshToken(token)
        token.blacklist()
        return Response({"message": "User logged out successfully"}, status=HTTP_200_OK)
    except Exception as error:
        return Response({"error": str(error)}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def delete_token(request):
    data = request.data
    token = data['token']
    try:
        token = RefreshToken(token)
        token.blacklist()
        return Response({"message": "Token deleted successfully"}, status=HTTP_200_OK)
    except Exception as error:
        return Response({"error": str(error)}, status=HTTP_400_BAD_REQUEST)


