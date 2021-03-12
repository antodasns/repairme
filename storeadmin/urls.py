from storeadmin import views
from django.conf.urls import url
from django.urls import path

app_name='storeadmin'
urlpatterns = [
	path('store_home', views.store_home,name='store_home'),
	path('bookings', views.bookings,name='bookings'),
	path('pickup_date/<int:id>/', views.pickup_date,name='pickup_date'),
	path('pickups', views.pickups,name='pickups'),
	path('pickup_confirm/<int:id>/', views.pickup_confirm,name='pickup_confirm'),
	path('estimate', views.estimate,name='estimate'),
	path('estimate_save/<int:id>/', views.estimate_save,name='estimate_save'),
	path('estimate_status', views.estimate_status,name='estimate_status'),
	path('declined_delivery', views.declined_delivery,name='declined_delivery'),
	path('delivery_date/<int:id>/<int:diff>/', views.delivery_date,name='delivery_date'),
	path('repaired_delivery', views.repaired_delivery,name='repaired_delivery'),
	path('delivery_status', views.delivery_status,name='delivery_status'),
	path('delivery', views.delivery,name='delivery'),
	path('delivery_confirm/<int:id>/', views.delivery_confirm,name='delivery_confirm'),
	path('payment', views.payment,name='payment'),		
]