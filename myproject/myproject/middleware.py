from django.http import HttpResponseForbidden

ALLOWED_IPS = [
    '103.39.127.0/24',
    'localhost',
    '127.0.0.1'  # Add your allowed IP addresses here
    # 'localhost',
]

class RestrictIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip not in ALLOWED_IPS:
            return HttpResponseForbidden("Forbidden: You don't have permission to access this resource.")
        return self.get_response(request)
    
# import requests

# response = requests.get('https://api.ipify.org?format=json')
# ip = response.json()['ip']
# print(f'My public IP address is: {ip}')