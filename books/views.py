import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from models import *

def home(request):
    return render(request, 'search.html.tpl', {'title' : 'Book Search'})

def search(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        queryset = Book.objects.filter(Q(title__icontains = query) | Q(author__icontains = query))
        return render(request, 'search.html.tpl', {
            'title' : 'Search Results for "%s"' % (query),
            'results' : True,
            'queryset' : queryset[0:50],
            'query' : query,
        })
    else:
        return render(request, 'search.html.tpl', {'title' : 'Search Results for "%s"' % (query), 'results' : True, 'queryset' : []})

def top(request):
    queryset = Book.objects.order_by('-hits')[0:100]
    return render(request, 'top.html.tpl', {'title' : 'Most Popular Books', 'queryset' : queryset})
def latest(request):
    queryset = Book.objects.order_by('-upload_date')[0:100]
    return render(request, 'latest.html.tpl', {'title' : 'Recently Added Books', 'queryset' : queryset})

def hit(request):
    book_id = request.GET.get('id')
    try:
        book = Book.objects.get(id = book_id)
        book.hits += 1
        book.save()
        return redirect(book.get_url())
    except ObjectDoesNotExist as e:
        return HttpResponse("error")

