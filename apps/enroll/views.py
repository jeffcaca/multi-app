from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from ..registration.models import User
from django.core.urlresolvers import reverse

def index(request):
  
	
	context = {
	'courses': Course.objects.all(),
	
	}
	
	return render(request, 'enroll/index.html', context)

def addcourse(request):
	

	if request.method == 'POST':
		Course.objects.create(name = request.POST['name'], description = request.POST['description'])
	return redirect(reverse('courses:index'))

def delete(request, id):

	delcourse = Course.objects.get(id = id)
	
	context = {
    	'courses': delcourse
    }
	delcourse.delete()
	return redirect(reverse('courses:index'))