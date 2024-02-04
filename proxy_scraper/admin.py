from django.contrib import admin
from .models import Proxy
# Register your models here.
class ProxyData(admin.ModelAdmin):
    list_display = ['ip', 'port', 'protocol', 'country', 'uptime']
admin.site.register(Proxy, ProxyData)
