from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
from rest_framework.views import APIView
import logging

logger=logging.getLogger(__name__)

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recieved the responce')
            data = response.json()
        except request.ConnectionError:
            logger.critical('httpbin is ofline')
        return render(request, 'hello.html', {'name': data})

# @cache_page(5*60)
# def say_hello(request):
    
