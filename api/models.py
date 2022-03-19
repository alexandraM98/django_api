from django.db import models

class Note(models.Model):

    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #timestamp will only be created when the note is actually created

    def __str__(self):
        return self.body[0:50] #when someone enters text, we only want to save the first 50 characters

    class Meta: 
        ordering = ['-updated'] #the latest updated note will always be at the top of the list when querying our database


#to create a weather object that will display some of the attributes from the weather api
#the attributes that I want are: coord (lat, long), weather (description), main (temp_min and temp_max)

class Weather(models.Model):

    name = models.TextField(max_length=25)
    lat = models.TextField(max_length=25)
    long = models.TextField(max_length=25)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = 'Weather'
