from django.shortcuts import render
import random
# Create your views here.

def home(request):
	return render(request, 'generator/home.html')


def password(request):
	thepassword = ''
	charecters = list('abcdefghijklmnopqrstyvwxyz')
	if request.GET.get('uppercase'):
		charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		charecters.extend(list('!@#$%^&*'))
	if request.GET.get('number'):
		charecters.extend(list('123456789'))
	length = int(request.GET.get('length'))
	for x in range(length):
		thepassword += random.choice(charecters)

	return render(request, 'generator/password.html', {'password':thepassword})