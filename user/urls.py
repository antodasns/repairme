from user import views
from django.urls import path

app_name='user'
urlpatterns = [
	path('loginpage', views.loginpage,name='loginpage'),
	path('logouts', views.logouts,name='logouts'),
	path('home', views.home,name='home'),
	path('store', views.store,name='store'),
	path('store_detail/<int:id>/', views.store_detail,name='store_detail'),
	path('booking/<int:id>/', views.booking,name='booking'),
	path('orders', views.orders,name='orders'),
	path('trackrepair/<int:id>/', views.trackrepair,name='trackrepair'),
		
]