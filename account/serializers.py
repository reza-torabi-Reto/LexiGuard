from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class CreateUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class AllUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        # extra_kwargs = {'password': {'write_only': True}}