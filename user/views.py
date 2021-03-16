from django.shortcuts import render,redirect 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from storeadmin.models import Booking,Appliance,StoreDetails,PickUp,Address,Estimate,Delivery
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users
# Create your views here.
@unauthenticated_user
def loginpage(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/user/home')
		else:
			messages.info(request,"Username or Password incorrect")
	return render(request,'user/login.html')
	
@unauthenticated_user
def signup(request):
	if request.method == 'POST':
		user = User(
		email=request.POST['email'],
		username=request.POST['username'],
		)

		user.set_password(request.POST['password'])
		user.save()
		group=Group.objects.get(name="user")
		user.groups.add(group)
		return HttpResponseRedirect('/user/signup')
	return render(request,'user/signup.html')

def logouts(request):
	logout(request)
	return HttpResponseRedirect('/user/loginpage')

@login_required(login_url="/user/loginpage")
@allowed_users(allowed_roles=['user'])
def home(request):
	return render(request,'user/index.html')

@login_required(login_url="/user/loginpage")	
def store(request):
	storedet=StoreDetails.objects.all()
	return render(request,'user/store.html',{'storedet':storedet})

@login_required(login_url="/user/loginpage")
def store_detail(request,id):
	storedet=StoreDetails.objects.get(pk=id)
	return render(request,'user/store_detail.html',{'storedet':storedet})

@login_required(login_url="/user/loginpage")
def booking(request,id):
	if request.method == 'POST':
		add_appliance=Appliance(
			appliance_name=request.POST['aname'],
			appliance_brand=request.POST['abrand'],
			appliance_years=request.POST['ayears'],
			appliance_description=request.POST['adescription'],
			)
		add_appliance.save()
		add_address=Address(
			name=request.POST['name'],
			address=request.POST['address'],
			phone=request.POST['phone'],
			landmark=request.POST['landmark'],
			)
		add_address.save()
		appliance_id=Appliance.objects.values_list('pk', flat=True).latest('appliance_id')	
		address_id=Address.objects.values_list('pk', flat=True).latest('address_id')
		booking=Booking(
			store_id=id,
			user_id=1,
			appliance_id=appliance_id,
			address_id=address_id,
			pickupdateconfirm='no',
			status_codes="order_placed"
			)
		booking.save()

	return redirect('/user/store')

@login_required(login_url="/user/loginpage")
def orders(request):
	booking=Booking.objects.filter(user_id=1)
	storedet=StoreDetails.objects.all()
	appliancedet=Appliance.objects.all()

	pickup_det=PickUp.objects.filter(user_id=1)
	estimate_det=Estimate.objects.filter(user_id=1)
	delivery_det=Delivery.objects.filter(user_id=1)
	return render(request,'user/orders.html',{'booking':booking,'storedet':storedet,'appliancedet':appliancedet,'pickup_det':pickup_det,'estimate_det':estimate_det,'delivery_det':delivery_det})

@login_required(login_url="/user/loginpage")
def estimate_view(request,id):
	estim=Estimate.objects.get(booking_id=id)
	storedet=StoreDetails.objects.get(store_id=estim.store_id)
	userdet=User.objects.get(id=estim.user_id)
	book=Booking.objects.get(booking_id=estim.booking_id)
	appliancedet=Appliance.objects.get(appliance_id=book.appliance_id)
	return render(request,'user/estimate_view.html',{'estim':estim,'storedet':storedet,'userdet':userdet,'appliancedet':appliancedet})

@login_required(login_url="/user/loginpage")
def estimate_confirm(request,id,cd):
	if cd==1:
		Booking.objects.filter(pk=id).update(status_codes='estimate_accept')
		Estimate.objects.filter(booking_id=id).update(estimate_status='done')
		return redirect('/user/orders')
	else:
		Booking.objects.filter(pk=id).update(status_codes='estimate_declined')
		Estimate.objects.filter(booking_id=id).update(estimate_status='cancel')
		return redirect('/user/orders')

@login_required(login_url="/user/loginpage")
def trackrepair(request,id):
	booking=Booking.objects.get(pk=id)
	storedet=StoreDetails.objects.get(store_id=booking.store_id)
	appliancedet=Appliance.objects.get(appliance_id=booking.appliance_id)
	addressdet=Address.objects.get(pk=booking.address_id)
	status=booking.status_codes
	if status=="order_placed":
		return render(request,'user/trackrepair.html',{'booking':booking,'storedet':storedet,'appliancedet':appliancedet,'addressdet':addressdet,'status':status})
	elif status=="pickup_confirmed":
		pickupdet=PickUp.objects.get(booking_id=id)
		return render(request,'user/trackrepair.html',{'booking':booking,'storedet':storedet,'appliancedet':appliancedet,'addressdet':addressdet,'status':status,'pickupdate':pickupdet.pickup_date})
	else:
		deldet=Delivery.objects.get(booking_id=id)
		return render(request,'user/trackrepair.html',{'booking':booking,'storedet':storedet,'appliancedet':appliancedet,'addressdet':addressdet,'status':status,'deldate':deldet.delivery_date})