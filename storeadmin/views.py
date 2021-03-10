from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Booking,Appliance,StoreDetails,PickUp,Address
# Create your views here.
def store_home(request):
	return render(request,'store_admin/index.html')

def bookings(request):
	booking_det=Booking.objects.all()
	appliance_det=Appliance.objects.all()
	pickups=PickUp.objects.all()
	return render(request,'store_admin/bookings.html',{'booking_det':booking_det,'appliance_det':appliance_det,'pickups':pickups})

def pickup_date(request,id):
	if request.method == 'POST':
		picking=PickUp(
			booking_id=id,
			store_id=1,
			user_id=1,
			pickup_status="pending",
			pickup_date=request.POST['pickupdate'],
			)
		picking.save()
		Booking.objects.filter(pk=id).update(pickupdateconfirm='yes')
	return redirect('/storeadmin/bookings')

def pickups(request):
	pickup_det=PickUp.objects.filter(store_id=1)
	appliance_det=Appliance.objects.all()
	address_det=Address.objects.all()
	booking_det=Booking.objects.all()
	return render(request,'store_admin/pickups.html',{'pickup_det':pickup_det,'appliance_det':appliance_det,'address_det':address_det,'booking_det':booking_det})

def pickup_confirm(request,id):
	if request.method == 'POST':
		PickUp.objects.filter(pk=id).update(pickup_status='done')
	return redirect('/storeadmin/pickups')

def estimate(request):
	return render(request,'store_admin/estimate.html')

def estimate_status(request):
	return render(request,'store_admin/estimate_status.html')

def declined_delivery(request):
	return render(request,'store_admin/declined_delivery.html')

def repaired_delivery(request):
	return render(request,'store_admin/repaired_delivery.html')

def delivery_status(request):
	return render(request,'store_admin/delivery_status.html')

def delivery(request):
	return render(request,'store_admin/delivery.html')

def payment(request):
	return render(request,'store_admin/payment.html')
