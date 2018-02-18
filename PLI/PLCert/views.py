from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .models import Module

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