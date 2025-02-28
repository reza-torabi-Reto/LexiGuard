from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Word
from .serializers import CreateGetWordSerializer, UpdateWordSerializer

# Create your views here.

class WordsView(APIView):

    permission_classes=(IsAuthenticated,)
    def get(self, request, user_id= None):
        
        if user_id == None:
            words = Word.objects.all()
            serializer = CreateGetWordSerializer(instance = words, many= True)
            return Response(serializer.data)
        else:
            words = get_list_or_404(Word, user__id= user_id)
            serializer = CreateGetWordSerializer(instance = words, many= True)
            return Response(serializer.data)


    def post(self, request):
        
        req_data = request.data
        serializer = CreateGetWordSerializer(data = req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def put(self, request, id):
        word_object = get_object_or_404(Word, id=id)
        req_data = request.data
        serializer = UpdateWordSerializer(instance= word_object, data=req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def delete(self, request, id):
        word_delete = get_object_or_404(Word, id=id)
        word_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

