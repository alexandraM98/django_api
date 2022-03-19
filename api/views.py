from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from api import serializers
import requests
import json
from urllib.request import urlopen
from .models import Weather

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint' : '/notes/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of notes'
        },
        {
            'Endpoint' : '/notes/id/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns a single note object'
        },
        {
            'Endpoint' : '/notes/create/',
            'method' : 'POST',
            'body' : {'body' : ""},
            'description' : 'Creates a new note with data sent in the POST request.'
        },
        {
            'Endpoint' : '/notes/id/update/',
            'method' : 'PUT',
            'body' : {'body' : ""},
            'description' : 'Updates an existing note'
        },
        {
            'Endpoint' : '/notes/id/delete/',
            'method' : 'DELETE',
            'body' : None,
            'description' : 'Deletes an existing note'
        },
        {
            'Endpoint' : '/weather/',
            'method' : 'GET', #PUT. Because I am trying to update the current data with the lat and long from the user input in Flutter.
            'body' : None,
            #'lat' : '',
            #'long' : '',
            'description' : 'Calls the weather api.'
        },

        #to create a new route that would have /weather as the endpoint and the data for that will be gathered from 
        #https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=ffb92f5691371697cb699c3a235cc350
    ]

    return Response(routes) 

    #we will need to do some data serialization so that we can display the objects created in JSON format
    #I will user Serializers from the Django REST framework

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True) #the note serializer can either serialize one single object or we can serialize an entire qwery set

    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False) #the note serializer can either serialize one single object or we can serialize an entire qwery set

    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )

    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data

    note = Note.objects.get(id=pk)

    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    
    return Response('Note was deleted.')

@api_view(['GET'])
def getWeather(request):
    lat = '53.2209389'
    long = '-4.1777091'
    url = 'https://api.openweathermap.org/data/2.5/weather?lat='+ lat + '&lon=' + long + '&appid=ffb92f5691371697cb699c3a235cc350'
    with urlopen(url) as response:
        source = response.read()

    data = json.loads(source)

    print('Sky state: ' + data['weather'][0]['description'])
    print(data['main']['temp_min'])
    print(data['main']['temp_max'])
    print(data['main']['feels_like'])

    return Response(data)

