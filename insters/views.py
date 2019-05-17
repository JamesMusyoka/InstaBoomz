from django.shortcuts import render, redirect
from  django.http import HttpResponse
import datetime as dt
from .models import *

# Create your views here.

def index(request):
	images = Images.objects.all()
	return render(request, 'index.html',{"images": images})

def image(request):
	date = dt.date.today()
	return render(request, 'image.html')

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day