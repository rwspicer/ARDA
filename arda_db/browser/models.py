"""
models.py
ross spicer
updated 2015-04-01

    contains the databas models for the browser
"""
from django.db import models


class Resource(models.Model):
    """
        Base Resource model, so that all types have a common numbering system
    """
    r_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 90, default='')
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title


class RLibrary(Resource):
    """
        Library item database model
    """
    phys_id = models.IntegerField(null=True)
    author = models.CharField(max_length = 60)
    # these ar the types of items in the Physical Library
    types = (
        ('0', 'Book'),
        ('1', 'DVD'),
        ('2', 'CD'),
        ('3', 'VHS'),
        ('4', 'Binder'),
        ('5', 'Manual'),
        ('6', 'Spiral Notebook'),
        ('7', 'Package(Book, DVD, et. al.)'),
        ('8', 'Cards'),
        ('9', 'Book w/ CD'),
        ('a', 'Activity Book'),
        ('b', 'Kit'),
        ('c', 'Various'),
        ('d', 'Catalogue'),
        ('e', 'Computer Game'),
        ('f', 'Watch/Timer'),
    )
    item_type = models.CharField(max_length=1, choices=types)
    # The Catagories for Items in the phyiscal libaray 
    cats = (
        ('0', 'Sensory Integration'),
        ('1', 'DVD/Software materials'),
        ('2', 'Resources for Professionals & Parents'),
        ('3', 'Couple Relationships'),
        ('4', 'Resources for Teaching Children/School'),
        ('5', 'Support for Siblings'),
        ('6', 'Resources for Older Children, Teens & Adults'),
        ('a', 'Behavior'),
        ('7', "Nonfiction/Novels/Children's Books"),
        ('8', 'Binder/Folder Resources'),
        ('9', 'FASD'),
    )
    catagory = models.CharField(max_length=1, choices=cats)
    # is this needed here
    #~ status = (
        #~ ('0', 'available'),
        #~ ('1', 'reserved'),
        #~ ('2', 'out')
    #~ )
    #~ availablity = models.CharField(max_length=1, choices=status)
    class Meta:
        verbose_name ='library item'
    

class Borower(models.Model):
    """
        borrower database model -- TODO merge with Library Item
    """
    types= (
        ('0', 'available'),
        ('1', 'reservered'),
        ('2', 'checked out'),
    )
    status = models.CharField(max_length=1, choices=types, default="0")
    
    
    resource = models.ForeignKey(RLibrary)
    borrower_name = models.CharField(max_length = 50, blank=True)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    checkout_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    

    
class ROnline(Resource):
    """
    datbase model for online items 
    """
    # types of online resources
    types = (
        ('0', 'video'),
        ('1', 'article'),
        ('2', 'web site')
    )
    otype = models.CharField(max_length = 1, choices=types, 
                                                           verbose_name ="type")
    date = models.DateField()
    url = models.TextField(blank=True)
    class Meta:
        verbose_name ='online item'



class RService(Resource):
    """
    database model for services
    """
    address = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    url = models.TextField(blank=True)
    class Meta:
        verbose_name ='service'



class SDemo(models.Model):
    """
    Demographic search related item Database model
    """
    resource = models.ForeignKey(Resource)
    age1to3 = models.BooleanField(default=False, verbose_name= "Age 1-3")
    age3to18 = models.BooleanField(default=False, verbose_name= "Age 3-18")
    age18plus = models.BooleanField(default=False, verbose_name= "Age 18+")
    gender_m = models.BooleanField(default=False, verbose_name= "Male")
    gender_f = models.BooleanField(default=False,  verbose_name= "Female")
    class Meta:
        verbose_name_plural =  verbose_name = "Demographics"
        


class SBehaviour(models.Model):
    """
    Behavior search related item Database model
    """
    resource = models.ForeignKey(Resource)
    sleep = models.BooleanField(default=False)
    safety_home = models.BooleanField(default=False)
    safety_public = models.BooleanField(default=False)
    safety_travel = models.BooleanField(default=False)
    repetition = models.BooleanField(default=False)
    aggression = models.BooleanField(default=False)
    communication = models.BooleanField(default=False)
    nonverbal = models.BooleanField(default=False)
    sensory = models.BooleanField(default=False)
    meltdown = models.BooleanField(default=False)
    anxiety = models.BooleanField(default=False)
    change = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = verbose_name = "Behaviors"



class SDisorder(models.Model):
    """
    Disorder search related item Database model
    """
    resource = models.ForeignKey(Resource)
    asd = models.BooleanField(default=False,
                            verbose_name= "Autism Spectrum Disorder")
    fas = models.BooleanField(default=False,
                            verbose_name= "Fetal Alcohol Syndrome")
    pdd = models.BooleanField(default=False,
                            verbose_name= "Pervasive Developmental Disorder")
    aspergers = models.BooleanField(default=False,
                            verbose_name= "Aspergers Syndrome")
    cdd = models.BooleanField(default=False,
                            verbose_name= "Cognative Develpoment Disorder")
    
    class Meta:
         verbose_name_plural = verbose_name = "Disorders"



class SServices(models.Model):
    """
    service search related item Database model
    """
    resourceLink = models.ForeignKey(Resource)
    diagnostic = models.BooleanField(default=False)
    resource = models.BooleanField(default=False)
    therapy = models.BooleanField(default=False)
    educational = models.BooleanField(default=False)
    referral = models.BooleanField(default=False)
    legal = models.BooleanField(default=False)
    city = models.CharField(max_length = 30)
    
    class Meta:
        verbose_name_plural = verbose_name = "Service Features"



class SAdditional(models.Model):
    """
    Additional search related item Database model
    """
    resource = models.ForeignKey(Resource)
    parents = models.BooleanField(default = False, 
                                verbose_name = "For Parents & Professionals")
    relationships = models.BooleanField(default = False, 
                                verbose_name = "Relationships")
    teachers = models.BooleanField(default = False, 
                                verbose_name = "For Teachers")
    sibilings = models.BooleanField(default = False, 
                                verbose_name = "For Siblings")
    teens = models.BooleanField(default = False, 
                                verbose_name = "For Teens/Young Adults")
    class Meta:
       verbose_name_plural = verbose_name = "Additional Search options"
