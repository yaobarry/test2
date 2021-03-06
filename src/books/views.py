from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from books.models import Book
from books.models import Publisher
from django.views.generic import ListView
# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

def search(request,temp_name1,temp_name2):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Please submit a search item')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response(temp_name2,{'books':books,'query':q})
    return render_to_response(temp_name1,{'errors':errors})

class PublisherList(ListView):
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'
    extra_context= {'book_list': Book.objects.all}
