from django.shortcuts import render
from django.http import HttpResponse
import http.client, urllib.parse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def x(request):
    subscriptionKey = '0c659fa4493f47c6b72473447b41fd4d'
    host = 'api.microsofttranslator.com'
    path = '/V2/Http.svc/Translate'
    target = 'fr-fr'
    text = 'Hello'
    params = '?to=' + target + '&text=' + urllib.parse.quote (text)
    def get_suggestions():
        headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
        conn = http.client.HTTPSConnection(host)
        conn.request ("GET", path + params, None, headers)
        response = conn.getresponse ()
        return response.read ()
    result = get_suggestions ()
    #print (result.decode("utf-8"))
    return HttpResponse(result)
