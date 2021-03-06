from storeadmin import views
from django.conf.urls import url
from django.urls import path

app_name='storeadmin'
urlpatterns = [
	path('store_home', views.store_home,name='store_home'),
	path('bookings', views.bookings,name='bookings'),
	path('pickups', views.pickups,name='pickups'),
	path('estimate', views.estimate,name='estimate'),
	path('estimate_status', views.estimate_status,name='estimate_status'),
	path('declined_delivery', views.declined_delivery,name='declined_delivery'),
	path('repaired_delivery', views.repaired_delivery,name='repaired_delivery'),
	path('delivery_status', views.delivery_status,name='delivery_status'),
	path('delivery', views.delivery,name='delivery'),
	path('payment', views.payment,name='payment'),

		
]