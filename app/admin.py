from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(Profile)
admin.site.register(Pgs)
admin.site.register(Booking)
admin.site.register(Payment)