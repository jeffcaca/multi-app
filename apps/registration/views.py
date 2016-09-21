from django.shortcuts import render, HttpResponse, redirect
from .models import User
from ..enroll.models import Course
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'registration/index.html')
def newuser(request):
	if request.method =='POST':
		res = User.userManager.register(first_name = request.POST['first'], last_name = request.POST['last'], email_address = request.POST['emailadd'], pwhash = request.POST['pw'], pwcheck = request.POST['pwcheck'])
		request.session['name'] = request.POST['first']
	if res['created']:
		newuser = res['newuser']
		request.session['id'] = res['id']
		return redirect(reverse('login:success'))
	else:
		for error in res['errors']:
			messages.error(request, error)
			return redirect(reverse('login:index'))


def login(request):
	if request.method =='POST':
		loginres = User.userManager.login(request.POST)
	if loginres['created']:
		request.session['id'] = loginres['id']
		return redirect(reverse('login:success'))
	else:
		for error in loginres['errors']:
			messages.error(request, error)
		return redirect(reverse('login:index'))

def success(request):
	this_user = User.userManager.get(id = request.session['id'])
	context = {
	'users': User.userManager.all(),
	'name': request.session.get('name'),
	'this_user': this_user

	}
	return render(request, 'registration/success.html', context)

def delete(request, id):
	print id, type(id)
	print request.session['id'], type(request.session['id'])
	if str(request.session['id']) != str(id):
		deleteuser = User.userManager.get(id = id)
		deleteuser.delete()
	return redirect(reverse('login:success'))

def usercourses(request):
	context = {
	'users': User.userManager.all(),
	'courses': Course.objects.all()
	}
	return render(request, 'registration/userscourses.html', context)

def addusertocourse(request):
	print "this printed"
	course = Course.objects.get(id = request.POST['courseid'])
	user = User.userManager.get(id = request.POST['users'])
	course.userlinks.add(user)
	course.save()
	return redirect(reverse('login:usercourses'))
