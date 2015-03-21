from django.shortcuts import render
from django.http import HttpResponse
#~ from django.template import RequestContext, loader
# Create your views here.
from browser.models import Resource


def index(request):
    resource_list = Resource.objects.order_by('r_id')
    #~ template = loader.get_template('browser/index.html')
    #~ context = RequestContext(request, {
        #~ 'resource_list': resource_list,
    #~ })
    #~ return HttpResponse(template.render(context))
    context = {'resource_list': resource_list}
    return render(request, 'browser/index.html', context)

    
    
def detail(request, r_id):
    try:
        item = Resource.objects.get(pk=r_id)
    except Resource.DoesNotExist:
        raise Http404("resource does not exist")
    return render(request, 'browser/detail.html', {'item': item})
