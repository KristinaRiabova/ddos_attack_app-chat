import logging
from django.http import JsonResponse
logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Incoming request: {request.method} {request.path}")
        
        response = self.get_response(request)

        logger.info(f"Outgoing response: {response.status_code}")

        return response

class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        error_message = str(exception)

        self.logger.error(error_message)
        return JsonResponse({'error': error_message}, status=500)