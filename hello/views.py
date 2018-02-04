from django.shortcuts import render
from django.http import HttpResponse
import http.client, urllib.parse
import unicodedata

from .models import Greeting

l1=[]
l2=[]
error_count=0

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

def error(request):
    global error_count
    error_count=error_count+1
    qq=""
    for i in l2:
        qq+=i+"\n"
    cc=""
    for i in l1:
        cc+=i+"\n"
    context= {
        'text1':cc,
        'text2':qq,
        'errorc':str(error_count)
    }
    return render(request, 'error.html', context)

def x1(request):
    if request.method=='POST':
        title= request.POST.get('title',False)
        if title!=False:
            l1.append(title)
            subscriptionKey = '0c659fa4493f47c6b72473447b41fd4d'
            host = 'api.microsofttranslator.com'
            path = '/V2/Http.svc/Translate'
            #Hindi
            target = 'hi'
            text = title
            params = '?to=' + target + '&text=' + urllib.parse.quote (text)
            def get_suggestions():
                headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
                conn = http.client.HTTPSConnection(host)
                conn.request ("GET", path + params, None, headers)
                response = conn.getresponse ()
                return response.read ()
            result = get_suggestions ()
            result = result.decode("utf-8", "strict")
            result=str(result)
            if result.index('>')>0:
                result=result[result.index('>')+1:]
            if result.index('<')>0:
                result=result[0:result.index('<')]
            l2.append(result)
            qq=""
            for i in l2:
                qq+=i+"\n"
            cc=""
            for i in l1:
                cc+=i+"\n"
            context= {
                'text1':cc,
                'text2':qq
            }
            return render(request, 'x1.html', context)
    return render(request, 'x1.html')


def x2(request):
    if request.method=='POST':
        title2= request.POST.get('title2',False)
        if title2!=False:
            l2.append(title2)
            subscriptionKey = '0c659fa4493f47c6b72473447b41fd4d'
            host = 'api.microsofttranslator.com'
            path = '/V2/Http.svc/Translate'
            #Hindi
            target = 'en'
            text = title2
            params = '?to=' + target + '&text=' + urllib.parse.quote (text)
            def get_suggestions():
                headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
                conn = http.client.HTTPSConnection(host)
                conn.request ("GET", path + params, None, headers)
                response = conn.getresponse ()
                return response.read ()
            result = get_suggestions ()
            result = result.decode("utf-8", "strict")
            result=str(result)
            if result.index('>')>0:
                result=result[result.index('>')+1:]
            if result.index('<')>0:
                result=result[0:result.index('<')]
            l1.append(result)
            qq=""
            for i in l2:
                qq+=i+"\n"
            cc=""
            for i in l1:
                cc+=i+"\n"
            context= {
                'text1':cc,
                'text2':qq
            }
            return render(request, 'x2.html', context)
    return render(request, 'x2.html')

def x(request):
    l1.clear()
    l2.clear()
    global error_count
    error_count=0
    context= {
        'text1':'',
        'text2':''
    }
    return render(request, 'x.html', context)
