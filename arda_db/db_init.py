"""
db_init.py
this script will initialize the date base if run from in the django shell

python manage.py shell
>>> from db_init import run
>>> run()

"""

from browser.models import Resource, RLibrary
def run():
    f1 = open('initializeDB1.csv', 'r')
    f2 = open('initializeDB2.csv', 'r')
    
    f1t = f1.read()
    f2t = f2.read()
    
    resource_info = f1t[f1t.find('values ')+len('values '):].split('\r')
    library_info = f2t[f2t.find("\r")+len("\r"):].split('\r')
    
    #~ print resource_info[:5]
    #~ print ""
    #~ print resource_info[-5:]
    #~ print ""
    #~ print library_info[:5]
    #~ print ""
    #~ print library_info[-5:]
    
    for idx in range(len(resource_info)-1):
        res = resource_info[idx].strip(';').strip(',').strip('(').strip(')').replace("\\'","'").split("','") 
        lib = library_info[idx].strip(';').strip(',').strip('(').strip(')').replace("\\'","'").split("','")
        print res, lib
        r = RLibrary(title = res[1].strip("'"), author = lib[2].strip("'"), description = res[0].strip("'"), phys_id = lib[0].strip("'"), item_type=lib[3].strip("'"), catagory=lib[4].strip("'"))
        r.save()
