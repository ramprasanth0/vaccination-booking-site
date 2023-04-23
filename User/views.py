from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from.models import vaccination_centre

# Create your views here.

def user_booking(request):
    return render(request,'user_booking.html')

def user_logout(request):
    auth.logout(request)
    return redirect('/')
