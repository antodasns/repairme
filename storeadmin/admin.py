from django.contrib import admin

# Register your models here.
from .models import StoreDetails,Booking
# Register your models here.
admin.site.register(StoreDetails)
admin.site.register(Booking)
