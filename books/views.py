import hashlib
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
        return HttpResponseForbidden("access denied\n")


class api_auth(object):
    def __init__(self, minimum_permissions):
        self.minimum_permissions = minimum_permissions
    def __call__(self, function):
        def authenticated_function(request):
            key = hashlib.sha224(request.POST.get('token', '')).hexdigest()
            try:
                apikey = APIKey.objects.get(key = key)
                if apikey.permissions < self.minimum_permissions:
                    return HttpResponse("access denied\n")
            except ObjectDoesNotExist:
                return HttpResponse("access denied\n")
            return function(request)
        return authenticated_function

@api_auth(1)
def api_verify(request):
    return HttpResponse("done\n")

@api_auth(2)
def api_addbook(request):
    Book(
        user = User.objects.get(id = int(request.POST.get('user_id'))),
        repository = Repository.objects.get(id = int(request.POST.get('repository_id'))),
        path = request.POST.get('path', ''),
        title = request.POST.get('title', ''),
        author = request.POST.get('author', '')
    ).save()
    return HttpResponse("done\n")
