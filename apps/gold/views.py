from django.shortcuts import render, redirect, HttpResponse
import random, datetime
from django.core.urlresolvers import reverse

def index(request):
	if 'gold' in request.session:
		return render(request, 'gold/index.html')
	else:
		request.session['gold'] = 0
		request.session['log'] = []
		return render(request, 'gold/index.html')

def process(request):
	if request.POST['building'] == "farm":
		randgold = random.randrange(1, 21)
		request.session['gold'] = request.session['gold'] + randgold
		request.session['log'].append('Earned ' + str(randgold) +  ' from the farm! ' + datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
	

	elif request.POST['building'] == "cave":
		randgold = random.randrange(5, 11)
		request.session['gold'] = request.session['gold'] + randgold
		request.session['log'].append('Earned ' + str(randgold) +  ' from the cave!' + datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
	
	elif request.POST['building'] == "house":
		randgold = random.randrange(2, 6)
		request.session['gold'] = request.session['gold'] + randgold
		request.session['log'].append('Earned ' + str(randgold) +  ' from the house!' + datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))


	elif request.POST['building'] == "casino":
		if random.random() <= .5:
			
			request.session['gold'] = request.session['gold'] + 50
			request.session['log'].append('Earned ' + str(50) +  ' from the casino!' + datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
		else:
			request.session['gold'] = request.session['gold'] - 50
			request.session['log'].append('Lost ' + str(50) +  ' from the casino!' + datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
	return redirect(reverse('ninjagold:index'))
