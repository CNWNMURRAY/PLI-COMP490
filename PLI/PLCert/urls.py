from django.urls import path, include
from django.conf.urls import url
from . import views

# ^ means the url will start with nothing and $ means end with nothing 
# views.index  means looks in view.py file for a method called index and we named it index
#? means parameter which is id and \d represents it should be a digit and + 
urlpatterns = [
    url(r'^$', views.index, name ='index'), 
    url(r'^about/$', views.about, name ='about'), 
    url(r'^courses/$', views.courses, name ='courses'),
    url(r'^profile/$', views.profile, name ='profile')

];
