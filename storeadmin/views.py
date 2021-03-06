from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def store_home(request):
	return render(request,'index.html')

def bookings(request):
	return render(request,'bookings.html')

def pickups(request):
	return render(request,'pickups.html')

def estimate(request):
	return render(request,'estimate.html')

def estimate_status(request):
	return render(request,'estimate_status.html')

def declined_delivery(request):
	return render(request,'declined_delivery.html')

def repaired_delivery(request):
	return render(request,'repaired_delivery.html')

def delivery_status(request):
	return render(request,'delivery_status.html')

def delivery(request):
	return render(request,'delivery.html')

def payment(request):
	return render(request,'payment.html')
