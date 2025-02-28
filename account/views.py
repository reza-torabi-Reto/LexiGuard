from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import CreateUserSerializer, AllUserSerializer

# Create your views here.

class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializers = AllUserSerializer(instance = users, many = True)
        return Response(serializers.data)

    def post(self, request):

        req_data = request.data
        serializer = CreateUserSerializer(data = req_data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        new_user = User(
            username = data['username'],
            email = data['email'],
        )
        new_user.set_password(data['password'])
        new_user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    