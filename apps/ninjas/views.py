from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, 'ninjas/index.html')

def four(request):
	image = ['leonardo.jpg', 'raphael.jpg', 'donatello.jpg', 'michelangelo.jpg']
	context = {
	"image": image
	}

	return render(request, 'ninjas/ninja.html', context)

def show_color(request, color):
	image =  []
	context = {
	"image": image
	}
	if color == 'blue':
		image.append('leonardo.jpg')
	elif color == 'red':
		image.append('raphael.jpg')
	elif color == 'purple':
		image.append('donatello.jpg')
	elif color == 'orange':
		image.append('michelangelo.jpg')
	else:
		image.append('notapril.jpg')

	return render(request, 'ninjas/ninja.html', context)