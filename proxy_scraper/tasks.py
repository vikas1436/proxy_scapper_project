
from celery import shared_task
import requests
from .models import Proxy

@shared_task
def scrape_proxy_list():
    url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc'

    try:
        response = requests.get(url)
        response.raise_for_status() 

        proxies_data = response.json().get('data', [])

        proxies = []
        for proxy_data in proxies_data:
            ip = proxy_data.get('ip', '')
            port = str(proxy_data.get('port', ''))
            protocol = proxy_data.get('protocols', [])[0] if 'protocols' in proxy_data else ''
            country = proxy_data.get('country', '')
            uptime = str(proxy_data.get('upTime', ''))

            proxies.append({
                'ip': ip,
                'port': port,
                'protocol': protocol,
                'country': country,
                'uptime': uptime,
            })
        print(proxies)
        # Save proxies to the database
        for proxy_data in proxies:
            Proxy.objects.create(**proxy_data)

    except requests.RequestException as e:
        print(f"Error fetching data: {str(e)}")



