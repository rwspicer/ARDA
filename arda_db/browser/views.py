from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from models import Resource
from models import REvent

def paginate(request, resource_list):
    results_per_page = 5
    paginator = Paginator(resource_list, results_per_page)
    page = request.GET.get('page', 1)
    
    try:
        resources = paginator.page(page)
    except PageNotAnInteger:
        resources = paginator.page(1)
    except EmptyPage:
        resources = paginator.page(paginator.num_pages)

    return resources


def home(request):
    resource_list = Resource.objects.order_by('r_id')
    context = {
        'resource_list': resource_list
    }
    return render_to_response('index.html', context)

def events(request):
    resource_list = REvent.objects.all()
    context = {
        "content" : paginate(request, resource_list),
        "filter_url_addon" : "",
        "page_url" : "/events/"
    }
    return render_to_response('results.html', context)

def result(request):
    resource_list = []
    filter_url_addon = ""
    if 'male' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__gender_m = True)))
        filter_url_addon += 'male=selected&'
    if 'female' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__gender_f = True)))
        filter_url_addon += 'female=selected&'
    if 'age1-3' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__age1to3 = True)))
        filter_url_addon += 'age1-3=selected&'
    if 'age3-18' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__age3to18 = True)))
        filter_url_addon += 'age3-8=selected&'
    if 'age18+' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdemo__age18plus = True)))
        filter_url_addon += 'age18=selected&'
    if 'Autism Spectrum Disorder' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__asd = True)))
        filter_url_addon += 'Autism+Spectrum+Disorder=selected&'
    if 'Fetal Alcohol Syndrome' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__fas = True)))
        filter_url_addon += 'Fetal+Alcohol+Syndrome=selected&'
    if 'Pervasive Developement Disorder' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__pdd = True)))
        filter_url_addon += 'Pervasive+Develeopment+Disorder=selected&'
    if 'Aspergers Syndrome' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__aspergers = True)))
        filter_url_addon += 'Aspergers+Syndrome=selected&'
    if 'Cognative Development Disorder' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sdisorder__cdd = True)))
        filter_url_addon += 'Cognative+Development+Disorder=selected&'
    if 'sleep' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__sleep = True)))
        filter_url_addon += 'sleep=selected&'
    if 'safety home' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__safety_home = True)))
        filter_url_addon += 'saftey+home=selected&'
    if 'safety public' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__safety_public = True)))
        filter_url_addon += 'safety+public=selected&'
    if 'safety travel' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__safety_travel = True)))
        filter_url_addon += 'saftey+travel=selected&'
    if 'repetition' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__repetition = True)))
        filter_url_addon += 'repetition=selected&'
    if 'aggression' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__aggression = True)))
        filter_url_addon += 'aggression=selected&'
    if 'communication' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__communication = True)))
        filter_url_addon += 'communication=selected&'
    if 'nonverbal' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__nonverbal = True)))
        filter_url_addon += 'nonverbal=selected&'
    if 'sensory' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__sensory = True)))
        filter_url_addon += 'sensory=selected&'
    if 'meltdown' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__meltdown = True)))
        filter_url_addon += 'meltdown=selected&'
    if 'anxiety' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__anxiety = True)))
        filter_url_addon += 'anxiety=selected&'
    if 'change' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sbehaviour__change = True)))
        filter_url_addon += 'change=selected&'
    if 'diagnostic' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sservices__diagnostic = True)))
        filter_url_addon += 'diagnostic=selected&'
    if 'resource' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sservices__resource = True)))
        filter_url_addon += 'resource=selected&'
    if 'therapy' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sservices__therapy = True)))
        filter_url_addon += 'therapy=selected&'
    if 'educational' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sservices__educational = True)))
        filter_url_addon += 'educational=selected&'
    if 'referral' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sservices__referral = True)))
        filter_url_addon += 'referral=selected&'
    if 'legal' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sservices__legal = True)))
        filter_url_addon += 'legal=selected&'
    if 'city' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sservices__city = True)))
        filter_url_addon += 'city=selected&'
    if 'parents' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sadditional__parents = True)))
        filter_url_addon += 'parents=selected&'
    if 'relationships' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sadditional__relationships = True)))
        filter_url_addon += 'relationships=selected&'
    if 'teachers' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sadditional__teachers = True)))
        filter_url_addon += 'teachers=selected&'
    if 'siblings' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sadditional__sibilings = True)))
        filter_url_addon += 'siblings=selected&'
    if 'teens' in request.GET:
        resource_list.extend(list(Resource.objects.filter(sadditional__teens = True)))
        filter_url_addon += 'teens=selected&'
    
    # Delete the last character & 
    filter_url_addon = filter_url_addon[:-1]
    
    # Remove duplicates in the list
    resource_list = list(set(resource_list))    
        
    context = {
        "content": paginate(request, resource_list),
        "filter_url_addon": filter_url_addon,
        "page_url": "/result/"
    }
    
    return render_to_response('results.html', context)  

def detail(request, r_id):
    try:
        item = Resource.objects.get(pk=r_id)
    except Resource.DoesNotExist:
        raise Http404("resource does not exist")
    return render_to_response("detail.html", {'item': item})
    
