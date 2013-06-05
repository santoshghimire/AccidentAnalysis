# Create your views here.
from django.shortcuts import render_to_response
from accidentApp.models import *
from django.http import HttpResponse, HttpResponseRedirect

import json
import csv
import os
# def home(request):
# 	return render_to_response('test.html')


# def home(request):
# 	return render_to_response('test.html')

from scrapedata import *
def home(request):
	return render_to_response('test.html')

def my_data(request):
	data = Accident.manager.all()
	data2 = []
	for each_item in data:
		parameters ={}
		parameters["death_number"] = str(each_item.death_number)
		parameters["injured_number"] = str(each_item.injured_number)
		parameters["lat"] = str(each_item.place.latitude)
		parameters["lon"] = str(each_item.place.longitude)
		parameters["time_hr"] = str(each_item.accident_hour)
		parameters["time_min"] = str(each_item.accident_minute)
		parameters["date"] = str(each_item.accident_date.accident_year)+":"+str(each_item.accident_date.accident_month)+":"+str(each_item.accident_date.accident_day)
		data2.append(parameters)

	return HttpResponse(json.dumps(data2))

def load_data(request):
	my_data = accident_records()
	for data in my_data:
		try:
			date = Date()
			date.accident_day = int(data["day"])
			date.accident_month =int(data["month"])
			date.accident_year = int(data["year"])
			date.save()
			accident = Accident()
			accident.accident_hour = data["hour"]
			accident.accident_minute = data["minute"]
			accident.death_number = data["death"]
			accident.injured_number = data["injury"]
			#vehicle = models.ForeignKey(Vehicle)
			#place = models.ForeignKey(Place)
			accident.accident_date = date
			accident.place = Place.manager.get(place_name_nepali = data["location"])
			Accident.save(accident)
		except:
			pass
	return HttpResponse("saved")

APP_ROOT = os.path.realpath('.')
def place_coordinate(request):
	print APP_ROOT
	newFile = csv.reader(open(APP_ROOT+'/accidentApp/'+'Data_accident.csv','r'))
	count=0
	parameter={}
	print "apple"
	for eachrow in newFile:
		print eachrow
		if count==0:
			count += 1
			continue

		place = Place()
		place.place_name_nepali = eachrow[0]
		place.place_name_english = eachrow[1]
		place.latitude = eachrow[2]
		place.longitude = eachrow[3]
		place.save()
	return HttpResponse("saved")		

def return_data(request):
	data = Accident.manager.all()
	print data
	return HttpResponse(json.dumps(data))