import imp
from django.contrib import admin
from .models import CapturedPacket, ArchivedPacket
# Register your models here.

admin.site.register(CapturedPacket)
admin.site.register(ArchivedPacket)
