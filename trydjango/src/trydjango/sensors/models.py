from django.db import models

# Create your models here.
class Sensor(models.Model):
	sensorID = models.TextField()
	location = models.TextField()
	sensor_type = models.TextField()
	active = models.TextField(default="this is cool")