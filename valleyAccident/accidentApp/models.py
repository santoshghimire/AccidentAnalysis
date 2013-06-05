from django.db import models
from accidentApp.manager import *

# Create your models here.

class Date(models.Model):
	"""stores the date of accident"""
	accident_day = models.IntegerField(null = True)
	accident_month = models.IntegerField(null = True)
	accident_year = models.IntegerField(null = True)
	manager = DateManager()
	

class Place(models.Model):
	"""stores the location of accident """
	place_name_nepali = models.CharField(max_length = 100, blank = True)
	place_name_english = models.CharField(max_length = 100, blank = True)	
	latitude = models.FloatField(null = True)
	longitude = models.FloatField(null = True)
	manager = PlaceManager()
	

class Vehicle(models.Model):
	"""stores the type of vehicle involved in accident"""
	vehicle_name = models.CharField(max_length = 100, blank = True)
	manager = VehicleManager()

class Accident(models.Model):
	
	accident_hour = models.IntegerField(null = True)
	accident_minute = models.IntegerField(null = True)
	death_number = models.IntegerField(null = True)
	injured_number = models.IntegerField(null = True)
	vehicle = models.ForeignKey(Vehicle, blank = True, null= True)
	place = models.ForeignKey(Place, blank= True, null= True)
	accident_date = models.ForeignKey(Date, blank = True, null= True)
	manager = AccidentManager()



	
