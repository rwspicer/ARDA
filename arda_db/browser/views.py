from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms
from models import Resource
from models import SDemo
from itertools import chain

def home(request):
    resource_list = Resource.objects.order_by('r_id')
    context = {'resource_list': resource_list}
    return render_to_response('index.html', context)

    
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        content = Resource.objects.filter(title=q)
        return render(request, 'results.html', {'content': content, 'query': q})
    else:
        return render(request, 'results.html', {'error': True})


def result(request):
    resource_list = []
    # if 'male' in request.GET:
    #     resource_list = chain(resource_list, (Resource.objects.filter(sdemo__gender_m = True)))
    if 'male' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__gender_m = True)))
    if 'female' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__gender_f = True)))
    if 'age1-3' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__age1to3 = True)))
    if 'age3-18' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__age3to18 = True)))
    if 'age18+' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__age18plus = True)))
    if 'Autism Spectrum Disorder' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__asd = True)))
    if 'Fetal Alcohol Syndrome' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__fas = True)))
    if 'Pervasive Developement Disorder' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__pdd = True)))
    if 'Aspergers Syndrome' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__aspergers = True)))
    if 'Cognative Development Disorder' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__cdd = True)))
    if 'sleep' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__sleep = True)))
    if 'safety home' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__safety_home = True)))
    if 'safety public' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__safety_public = True)))
    if 'safety travel' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__safety_travel = True)))
    if 'repetition' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__repetition = True)))
    if 'aggression' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__aggression = True)))
    if 'communication' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__communication = True)))
    if 'nonverbal' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__nonverbal = True)))
    if 'sensory' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__sensory = True)))
    if 'meltdown' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__meltdown = True)))
    if 'anxiety' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__anxiety = True)))
    if 'change' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__change = True)))
    
    #Removing duplicates -- mysql doesn't support distinct()
    # values_list('shared_note', flat=True).distinct()
    
    # qs.values_list('title', flat=True).distinct()
        
    return render(request, 'results.html', {'content': resource_list})  

def detail(request, r_id):
    try:
        item = Resource.objects.get(pk=r_id)
    except Resource.DoesNotExist:
        raise Http404("resource does not exist")
    return render_to_response("detail.html", {'item': item})
    
