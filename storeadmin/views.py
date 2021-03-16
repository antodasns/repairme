from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from .models import Booking,Appliance,StoreDetails,PickUp,Address,Estimate,Delivery
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
			estimategivenconfirm="pending",
			pickup_date=request.POST['pickupdate'],
			)
		picking.save()
		Booking.objects.filter(pk=id).update(pickupdateconfirm='yes')
		Booking.objects.filter(pk=id).update(status_codes='pickup_confirmed')
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
		book_id=PickUp.objects.get(pk=id)
		Booking.objects.filter(pk=book_id.booking_id).update(status_codes='pickup_success')
	return redirect('/storeadmin/pickups')

def estimate(request):
	pickup_det=PickUp.objects.filter(store_id=1,pickup_status="done")
	appliance_det=Appliance.objects.all()
	booking_det=Booking.objects.all()
	return render(request,'store_admin/estimate.html',{'pickup_det':pickup_det,'appliance_det':appliance_det,'booking_det':booking_det})

def estimate_save(request,id):
	if request.method == 'POST':
		estimate=Estimate(
			booking_id=id,
			store_id=1,
			user_id=1,
			parts=request.POST['complaints'],
			complaints=request.POST['parts'],
			estimate_price=request.POST['price'],
			estimate_status="pending",
			delivery_status="none"
			)
		estimate.save()
		PickUp.objects.filter(booking_id=id).update(estimategivenconfirm='done')
		Booking.objects.filter(pk=id).update(status_codes='estimate_update')
	return redirect('/storeadmin/estimate')

def estimate_status(request):
	estimate_det=Estimate.objects.all()
	appliance_det=Appliance.objects.all()
	booking_det=Booking.objects.all()
	user_det=User.objects.all()
	return render(request,'store_admin/estimate_status.html',{'estimate_det':estimate_det,'appliance_det':appliance_det,'booking_det':booking_det,'user_det':user_det})

def declined_delivery(request):
	estimate_det=Estimate.objects.filter(estimate_status="cancel")
	booking_det=Booking.objects.all()
	appliance_det=Appliance.objects.all()
	return render(request,'store_admin/declined_delivery.html',{'estimate_det':estimate_det,'booking_det':booking_det,'appliance_det':appliance_det})

def repaired_delivery(request):
	estimate_det=Estimate.objects.filter(estimate_status="done")
	booking_det=Booking.objects.all()
	appliance_det=Appliance.objects.all()
	return render(request,'store_admin/repaired_delivery.html',{'estimate_det':estimate_det,'booking_det':booking_det,'appliance_det':appliance_det})

def delivery_date(request,id,diff):
	if diff==1:
		if request.method == 'POST':
			delivery=Delivery(
				booking_id=id,
				store_id=1,
				user_id=1,
				delivery_status="pending",
				delivery_date=request.POST['deliverydate'],
				)
			delivery.save()
			Estimate.objects.filter(booking_id=id).update(delivery_status='pending')
			Booking.objects.filter(pk=id).update(status_codes='deliverysoon')
		return redirect('/storeadmin/declined_delivery')
	else:
		if request.method == 'POST':
			delivery=Delivery(
				booking_id=id,
				store_id=1,
				user_id=1,
				delivery_status="pending",
				delivery_date=request.POST['deliverydate'],
				)
			delivery.save()
			Estimate.objects.filter(booking_id=id).update(delivery_status='pending')
			Booking.objects.filter(pk=id).update(status_codes='deliverysoon')
		return redirect('/storeadmin/repaired_delivery')

def delivery_status(request):
	delivery_det=Delivery.objects.all()
	appliance_det=Appliance.objects.all()
	booking_det=Booking.objects.all()
	user_det=User.objects.all()
	return render(request,'store_admin/delivery_status.html',{'delivery_det':delivery_det,'appliance_det':appliance_det,'booking_det':booking_det,'user_det':user_det})

def delivery(request):
	delivery_det=Delivery.objects.filter(store_id=1)
	appliance_det=Appliance.objects.all()
	address_det=Address.objects.all()
	booking_det=Booking.objects.all()
	return render(request,'store_admin/delivery.html',{'delivery_det':delivery_det,'appliance_det':appliance_det,'address_det':address_det,'booking_det':booking_det})

def delivery_confirm(request,id):
	if request.method == 'POST':
		Delivery.objects.filter(pk=id).update(delivery_status='delivered')
		Del=Delivery.objects.get(pk=id)
		Estimate.objects.filter(booking_id=Del.booking_id).update(delivery_status='delivered')
		Booking.objects.filter(pk=id).update(status_codes='delivered')
	return redirect('/storeadmin/delivery')

def payment(request):
	return render(request,'store_admin/payment.html')
