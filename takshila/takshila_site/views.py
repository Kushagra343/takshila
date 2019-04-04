# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    context = {}
    return render(request, "index.html", context)


def team(request):
    context = {}
    return render(request, "team.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def courses(request):
    context = {}
    return render(request, "courses.html", context)


def courses_detail(request):
    context = {}
    return render(request, "courses-detail.html", context)    


def login_web(request):
	if request.method == 'POST':
		print request.POST
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		context = {"authenticate": True, "name":username}
	else:
		context = {"authenticate": False}

	return render(request, "index.html", context)   