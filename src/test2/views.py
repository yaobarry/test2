'''
@author: xinyaoli
'''
from django.template.loader import get_template
from django.http import HttpResponse,Http404
from django.template import Template,context
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse(r'hello world')

def current_datetime(request):
    n=datetime.datetime.now()
    return render_to_response('current_date.html',{'current_date': n})


def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
#     assert False
    html = "<html><body>In %s hours,it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META
    return render_to_response('button.html',request.META)


