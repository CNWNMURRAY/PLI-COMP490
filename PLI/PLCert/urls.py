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
    url(r'^profile/$', views.profile, name ='profile'),
    url(r'^events/$', views.events, name ='events'),
    url(r'^courselist/$', views.courselist, name ='courselist'),
    url(r'^register/$', views.register, name ='register'),
    url(r'^login/$', views.login, name ='login'),
    url(r'^logout/$', views.logout, name ='logout'),
    url(r'^poll/$', views.poll, name ='poll'),
    url(r'^PLV/$', views.PLV, name ='PLV'),
    url(r'^emodule/$', views.emodule, name ='emodule'),
    url(r'^results/$', views.results, name ='results')



];
