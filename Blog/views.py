from django.shortcuts import render
from . import models
from math import ceil
# Create your views here.
from django.http import HttpResponse

def index(request):
    Dbpost =  models.Blogpost.objects.all();
    pdt = []
    odr = []
    for p in Dbpost:
        if getattr(p,'Head_title') == 'Product':
            pdt.append(p)
        if getattr(p,'Head_title') == 'Order':
            odr.append(p)
    Dict_Posts = {"DB":[pdt,odr]}
    print(Dict_Posts)
    return render(request, 'Blog/index.html',Dict_Posts)

def blogpost(request,pid):
    DBpost= models.Blogpost.objects.filter(post_id=pid)
    print(DBpost)
    DBDictict = {'post':DBpost}
    return render(request, 'Blog/blogpost.html',DBDictict)