from rest_framework.serializers import ModelSerializer
from .models import Word

class CreateGetWordSerializer(ModelSerializer):
    class Meta:
        model= Word
        fields = '__all__'


class UpdateWordSerializer(ModelSerializer):
    class Meta:
        model= Word
        fields = ('word_eng', 'word_fa',)