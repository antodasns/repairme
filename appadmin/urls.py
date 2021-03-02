from appadmin import views
from django.conf.urls import url
from django.urls import path

app_name='appadmin'
urlpatterns = [
	path('demo', views.demo,name='demo'),
		
]