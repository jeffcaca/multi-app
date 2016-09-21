from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, 'form/index.html')
def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comments'] = request.POST['comments']
	if 'count' not in request.session:
		request.session['count'] = 1
	else:
		request.session['count'] +=1
	return redirect('/result')
def result(request):


	return render(request, 'form/result.html')