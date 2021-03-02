from django.shortcuts import render,redirect 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from storeadmin.models import StoreDetails,Booking,Appliance
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
	return render(request,'login.html')
	
@unauthenticated_user
def signup(request):
	return HttpResponse("ss")

def logouts(request):
	logout(request)
	return HttpResponseRedirect('/user/loginpage')

@login_required(login_url="/user/loginpage")
@allowed_users(allowed_roles=['user'])
def home(request):
	return render(request,'index.html')

@login_required(login_url="/user/loginpage")	
def store(request):
	storedet=StoreDetails.objects.all()
	return render(request,'store.html',{'storedet':storedet})

@login_required(login_url="/user/loginpage")
def store_detail(request,id):
	storedet=StoreDetails.objects.get(pk=id)
	return render(request,'store_detail.html',{'storedet':storedet})

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
		appliance_id=Appliance.objects.values_list('pk', flat=True).latest('appliance_id')	
		booking=Booking(
			store_id=id,
			user_id=1,
			appliance_id=appliance_id,
			)
		booking.save()

	return HttpResponse("success")

@login_required(login_url="/user/loginpage")
def orders(request):
	booking=Booking.objects.filter(user_id=1)
	storedet=StoreDetails.objects.all()
	appliancedet=Appliance.objects.all()
	return render(request,'orders.html',{'booking':booking,'storedet':storedet,'appliancedet':appliancedet})

@login_required(login_url="/user/loginpage")
def trackrepair(request,id):
	booking=Booking.objects.get(pk=id)
	storedet=StoreDetails.objects.get(store_id=booking.store_id)
	appliancedet=Appliance.objects.get(appliance_id=booking.appliance_id)
	return render(request,'trackrepair.html',{'booking':booking,'storedet':storedet,'appliancedet':appliancedet})
