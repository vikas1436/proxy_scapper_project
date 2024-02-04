from django.shortcuts import render
from .models import Proxy

def proxy_list(request):
    proxies = Proxy.objects.all()
    print(proxies)
    context ={
        'proxies': proxies
    }
    return render(request, 'proxy_list.html', context)