from django.contrib import admin
from browser.models import Resource, Borower, RLibrary, ROnline, RService, SDemo, SBehaviour, SDisorder, SServices

#~ # Register your models here.
#~ admin.site.register(Resource)
#~ class RType(admin.TabularInline):
    #~ model = RLibrary
    #~ extra = 1
    #~ max_num = 1
    
class Demo(admin.TabularInline):
    model = SDemo
    max_num = 1

class Behaviour(admin.TabularInline):
    model = SBehaviour
    max_num = 1

class Disorder(admin.TabularInline):
    model = SDisorder
    max_num = 1
#~ 
class Service(admin.TabularInline):
    model = SServices
    max_num = 1

class BorowerClass(admin.TabularInline):
    model = Borower
    
    max_num = 1



class LibraryAdmin(admin.ModelAdmin):
    inlines = [BorowerClass ,Demo, Behaviour, Disorder]
    list_filter = ['phys_id']
    search_fields = ['title','catagory']
    list_filter = ['catagory', 'item_type']
    list_display = ('title', 'phys_id')
    fieldsets = [
        (None, 			{'fields': ['title','author','phys_id','item_type','catagory']}),
        (None,          {'fields': ['description']}),
        #~ (None,          {'fields': ['r_type']}),
        #~ (None,          {'fields': ['item_type','catagory']}),
    ]
    
class OnlineAdmin(admin.ModelAdmin):
    inlines = [Demo, Behaviour, Disorder]
    fieldsets = [
        (None, 			{'fields': ['title','otype','date','url']}),
        (None,          {'fields': ['description']}),
    ]

class ServiceAdmin(admin.ModelAdmin):
    inlines = [Service, Demo, Behaviour, Disorder]
    fieldsets = [
        (None, 			{'fields': ['title','phone','email','address']}),
        (None,          {'fields': ['description']}),
        #~ (None,          {'fields': ['r_type']}),
        #~ (None,          {'fields': ['item_type','catagory']}),
    ]
    

admin.site.register(RLibrary, LibraryAdmin)
admin.site.register(ROnline, OnlineAdmin)
admin.site.register(RService, ServiceAdmin)