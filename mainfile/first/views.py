from django.shortcuts import render
import pytumblr
import httplib, urllib, base64, urllib2, json
import requests
import json
# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request): 
	a = request.GET['sUrl']
	context = {
		'data' : a,
	}
	return render(request , 'first/index.html' ,context)


