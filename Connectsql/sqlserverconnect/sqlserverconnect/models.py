from django.db import models # type: ignore

class sqlserverconn(models.Model):
    Conference=models.CharField(max_length=500)
    CityCountry=models.CharField(max_length=500)
    Deadline=models.CharField(max_length=500)
    Date=models.CharField(max_length=500)
    Website=models.CharField(max_length=500)
    Description=models.CharField(max_length=1000)
    class Meta:
        app_label = 'sqlserverconnect'