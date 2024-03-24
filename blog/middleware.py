from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils import timezone

class RequestCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')

        if ip_address in settings.BLOCKED_IPS:
            return HttpResponseForbidden("Seu endereço IP foi bloqueado por medida de segurança.")

        if 'request_count_expiration' in request.session:
            expiration_time_str = request.session['request_count_expiration']
            expiration_time = datetime.datetime.strptime(expiration_time_str, '%Y-%m-%d %H:%M:%S.%f')
            if expiration_time < timezone.now():
                del request.session['request_count']
                del request.session['request_count_expiration']

        request_count = request.session.get('request_count', 0)
        request.session['request_count'] = request_count + 1

        if request_count >= settings.MAX_REQUESTS_PER_IP:
            return HttpResponseForbidden("Você atingiu o limite máximo de solicitações.")

        expiration_time = timezone.now() + settings.REQUEST_COUNT_EXPIRATION
        expiration_time_str = expiration_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        request.session['request_count_expiration'] = expiration_time_str

        response = self.get_response(request)
        return response