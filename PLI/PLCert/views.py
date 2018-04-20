from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .models import Module

# Create your views here.
def index(request):

    courses =  Course.objects.all()
    #variable set equal to Course from models to get all courses. 
    #next pass course object into template using context
    context = {
        'title': 'Courses',
        'courses':courses
    }

    return render(request, 'PLCert/index.html', context)

def about(request):
    return render(request, 'PLCert/about.html')

def courses(request):
    courses =  Course.objects.all()
    #variable set equal to Course from models to get all courses. 
    #next pass course object into template using context
    context = {
        'title': 'Courses',
        'courses':courses
    }

    return render(request, 'PLCert/courses.html', context)

def events(request):
    return render(request, 'PLCert/events.html')

def logout(request):
    return render(request, 'PLCert/logout.html')

def login(request):
    return render(request, 'PLCert/login.html')

def register(request):
    return render(request, 'PLCert/register.html')

def profile(request):
    return render(request, 'PLCert/profile.html')

def poll(request, question_id):
    return render(request, 'PLCert/poll.html')

def results(request):
    return render(request, 'PLCert/results.html')

def courselist(request):
    courses =  Course.objects.all()
    #variable set equal to Course from models to get all courses. 
    #next pass course object into template using context
    context = {
        'title': 'Courses',
        'courses':courses
    }
    return render(request, 'PLCert/courselist.html', context)