"""
models.py
ross spicer
updated 2015-04-09

    this file manages the admin pages
"""
from django.contrib import admin#, ModelAdmin
from browser.models import Resource, RLibrary, ROnline, RService, \
                           REvent, SDemo, SBehaviour, SDisorder, SServices, \
                           SAdditional
from django.contrib.auth.models import Group, User

# remove Group and users from admin page
admin.site.unregister(Group)
admin.site.unregister(User)

    
class Demo(admin.TabularInline):
    """
    class for demographic search terms
    """
    model = SDemo
    max_num = 1
    

class Behaviour(admin.TabularInline):
    """
    class for behavior search terms
    """
    model = SBehaviour
    max_num = 1


class Disorder(admin.TabularInline):
    """
    class for disorder related search terms
    """
    model = SDisorder
    max_num = 1

 
class Service(admin.TabularInline):
    """
    class for service search terms
    """
    model = SServices
    max_num = 1


class Additional(admin.TabularInline):
    """
    class for Additional search terms
    """
    model = SAdditional
    max_num = 1


# borrower has changed 
#~ class BorowerClass(admin.TabularInline):
    #~ model = Borower
    #~ 
    #~ max_num = 1

admin.ModelAdmin.list_per_page = 20 
class LibraryAdmin(admin.ModelAdmin):
    """
    this class sets up what is displayed for the admin page for library items
    """
    inlines = [Demo, Behaviour, Disorder, Additional]
    search_fields = ['title', 'description']
    list_filter = ['status', 'catagory', 'item_type', ]
    list_display = ('title', 'phys_id', 'status' )
    ordering       = ('phys_id',)

    fieldsets = [
        (None, 			{'fields': ['title','author','phys_id','item_type'
                                                                ,'catagory']}),
        (None,          {'fields': ['description']}),
        ("Browser Options",    {'fields': ["homepage", ]}),
        ("Borrower Info",       {'classes': ('collapse', 'open'),
                                'fields': ['status',
                                           'borrower_name',
                                           'email', 
                                           'phone', 
                                           'checkout_date', 
                                           'return_date',]
                                }
        ),
    ]
    
    
    
class OnlineAdmin(admin.ModelAdmin):
    """
    this class controls what is seen in for the admin of online items
    """
    inlines = [Demo, Behaviour, Disorder, Additional]
    search_fields = ['title', 'description']
    list_filter = ['otype', ]
    list_display = ('title',)
    fieldsets = [
        (None, 			{'fields': ['title','otype','date','url']}),
        (None,          {'fields': ['description']}),
        ("Browser Options",   {'fields': ["homepage", ]}),
    ]


class ServiceAdmin(admin.ModelAdmin):
    """
    this class controls what is seen in for the admin of service items
    """
    inlines = [Service, Demo, Behaviour, Disorder, Additional]
    search_fields = ['title', 'description']
    list_filter = ['sservices__city', ]
    list_display = ('title', )
    fieldsets = [
        (None, 			{'fields': ['title','phone','email','address','url']}),
        (None,          {'fields': ['description']}),
        ("Browser Options",   {'fields': ["homepage", ]}),
    ]


class EventAdmin(admin.ModelAdmin):
    """
    this class controls what is seen in for the admin of event items
    """
    inlines = [Demo, Behaviour, Disorder, Additional]
    search_fields = ['title', 'description']
    list_display = ('title',)
    fieldsets = [
        (None, 			{'fields': ['title','date_time', 'location']}),
        (None,          {'fields': ['description']}),
        ("Browser Options",    {'fields': ["homepage", ]}),#"show_in_browser"]}),
    ]
    


# add resource types to admin page
admin.site.register(RLibrary, LibraryAdmin)
admin.site.register(ROnline, OnlineAdmin)
admin.site.register(RService, ServiceAdmin)
admin.site.register(REvent, EventAdmin)
