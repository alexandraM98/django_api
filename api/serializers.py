from rest_framework.serializers import ModelSerializer
from .models import Note
from .models import Weather

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note #we need to first specify the model that we want to serialize
        #then, we specify the fields that we want to serialize
        fields = '__all__' #this will serialize all fields


class WeatherSerializer(ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
