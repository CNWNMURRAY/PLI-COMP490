from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .models import Response
from .models import Course
from .models import Module
from .models import Content
from .models import ItemBase
from .models import Text
from .models import File
from .models import Image
from .models import Video
from .models import Organization
from .models import Volunteer

# Create your views here.
def index(request):
    return render(request, 'PLCert/index.html')

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

def emodule(request):
    return render(request, 'PLCert/emodule.html')

def logout(request):
    return render(request, 'PLCert/logout.html')

def login(request):
    return render(request, 'PLCert/login.html')


def profile(request):
    return render(request, 'PLCert/profile.html')

def poll(request, question_id):
    return render(request, 'PLCert/poll.html')

def PLV(request):
    return render(request, 'PLCert/PLV.html')

def research(request):
    return render(request, 'PLCert/research.html')

def privacypolicy(request):
    return render(request, 'PLCert/privacypolicy.html')

def volunteer(request):
    return render(request, 'PLCert/volunteer.html')


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