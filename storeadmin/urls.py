from storeadmin import views
from django.conf.urls import url
from django.urls import path

app_name='storeadmin'
urlpatterns = [
	path('demo1', views.demo1,name='demo1'),
		
]