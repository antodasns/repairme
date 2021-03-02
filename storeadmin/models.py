from django.db import models

# Create your models here.
class StoreDetails(models.Model):
	store_id=models.AutoField(primary_key=True)
	store_name=models.CharField(max_length=30)
	store_address=models.CharField(max_length=150)
	store_place=models.CharField(max_length=30)
	store_phone=models.CharField(max_length=20)
	store_email=models.CharField(max_length=30)
	store_thumbnail=models.ImageField(upload_to='store/')
	store_bgimg=models.ImageField(upload_to='store/')
	class Meta:
		verbose_name_plural="StoreDetails"
	def __str__(self):
		return str(self.store_id)

class Booking(models.Model):
	booking_id=models.AutoField(primary_key=True)
	store_id=models.CharField(max_length=20)
	user_id=models.CharField(max_length=20)
	appliance_id=models.CharField(max_length=20)
	class Meta:
		verbose_name_plural="Booking"
	def __str__(self):
		return str(self.booking_id)

class Appliance(models.Model):
	appliance_id=models.AutoField(primary_key=True)
	appliance_name=models.CharField(max_length=20)
	appliance_brand=models.CharField(max_length=20)
	appliance_years=models.CharField(max_length=20)
	appliance_description=models.TextField()
	class Meta:
		verbose_name_plural="Appliance"
	def __str__(self):
		return str(self.appliance_id)