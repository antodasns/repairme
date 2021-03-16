from user import views
from django.urls import path

app_name='user'
urlpatterns = [
	path('loginpage', views.loginpage,name='loginpage'),
	path('signup', views.signup,name='signup'),
	path('logouts', views.logouts,name='logouts'),
	path('home', views.home,name='home'),
	path('store', views.store,name='store'),
	path('store_detail/<int:id>/', views.store_detail,name='store_detail'),
	path('booking/<int:id>/', views.booking,name='booking'),
	path('orders', views.orders,name='orders'),
	path('trackrepair/<int:id>/', views.trackrepair,name='trackrepair'),
	path('estimate_view/<int:id>/', views.estimate_view,name='estimate_view'),
	path('estimate_confirm/<int:id>/<int:cd>/', views.estimate_confirm,name='estimate_confirm'),
]