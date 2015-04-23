"""
models.py
ross spicer
updated 2015-04-09

    contains the database models for the browser
"""
from django.db import models
from django.core.mail import send_mail, mail_admins
from datetime import tzinfo, timedelta, datetime
from threading import Thread 


ZERO = timedelta(0)

class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO

utc = UTC()  
from time import sleep

class Resource(models.Model):
    """
        Base Resource model, so that all types have a common numbering system
    """
    r_id = models.AutoField(primary_key = True) #auto generated
    title = models.CharField(max_length = 160, default='') # title
    description = models.TextField(blank=True) # description
    homepage = models.BooleanField(default = False) # should the resource
                                                    # be shown on the home page
    show_in_browser = models.BooleanField(default = True) # for events 
                                                          # hidden as a user opt
    def __unicode__(self):
        return self.title

from django.core.exceptions import ValidationError
class RLibrary(Resource):
    """
        Library item database model
    """
    phys_id = models.IntegerField(null=True)  #no column in .xls file
    author = models.CharField(max_length = 160) # author col in # .xls
    # these are the types of items in the Physical Library, some have been
    # combined from the .xls file
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
    item_type = models.CharField(max_length=1, choices=types) #Item col in .xls
    # The Catagories for Items in the phyiscal libaray 
    cats = ( #categories in the .xls file
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
    catagory = models.CharField(max_length=1, choices=cats) #category col in xls
   
    # borrower info
    statuses = (
        ('0', 'Available'),
        ('1', 'Reservered'),
        ('2', 'Checked out'),
    )
    status = models.CharField(max_length=1, choices=statuses, default="0")
    borrower_name = models.CharField(max_length = 60, default='', blank = True,
                                                         verbose_name = 'name')
    phone = models.CharField(max_length = 10, default='',blank = True)
    email = models.CharField(max_length = 50, default='',blank = True)
    checkout_date = models.DateTimeField(blank=True, null=True,
                        verbose_name = "Check Out Appointment")
    return_date = models.DateTimeField(blank=True, null=True, 
                        verbose_name = "Return Appointment")
    
    def clean(self):
        if self.status == '0':
            #~ self.checkout_date = self.return_date = ""
            self.email = self.phone = self.borrower_name = "" 
        if self.status == '1' or self.status == '2':
            if self.borrower_name == "":
                raise ValidationError("Enter a borrower's Name, " +\
                                        "to schedule an appointment")
            if self.phone == "" and self.email == "":
                raise ValidationError("Enter a phone number or email, " +\
                                        "to schedule an appointment")
        if self.status == '1':
            try:
                if self.checkout_date < datetime.now(utc):
                    raise TypeError
            except TypeError:
                raise ValidationError('The checkout date has past,' +\
                                    'please update')
            # check for name & contact
            self.email_ar() # start up the admin reminder email thread
            if not self.email == "":
                self.email_cr()
        if self.status == '2':
            try:
                if self.return_date < datetime.now(utc):
                    raise TypeError
            except TypeError:
                raise ValidationError('The return date has past, please update')
            # check for name & contact
            self.email_aco() # start up the admin reminder email thread
            if not self.email == "":
                self.email_cco()
            
    def email_cr(self):
        # send email (perhaps write an email thread)
        #~ print "sending client resevered email"
        subject = "Checkout Appointment Reminder"
        msg = "Dear " + self.borrower_name + ',\n\n' +\
              "You have set up an appointment to check out " + self.title + \
              ". Your appointment is at " + str(self.checkout_date)[11:16] + \
              " on " + str(self.checkout_date)[:10] +\
              ". \nThank you, \n\n The Autism Society of Alaska."
        sender = 'from@example.com'
        send_mail(subject, msg, sender,[self.email], fail_silently=True)
        # claculete time to a date before & sleep
        # send email
        # end thread
        
    def email_ar(self):
        #~ print "sending admin resevered email"
        # send email
        subject = "Checkout Appointment Reminder"
        msg = self.borrower_name + " has set up an appointment to check out " \
              + self.title + ", the Physical ID is " + str(self.phys_id) +\
              ". The appointment is at " + str(self.checkout_date)[11:16] + \
              " on " + str(self.checkout_date)[:10] +\
              ". \nThank you, \n\n The Autism Society of Alaska."
        sender = 'from@example.com'
        mail_admins(subject, msg, fail_silently=True)
        
        # claculete time to a date before & sleep
        # send email
        # end thread
        
    def email_cco(self):
        #~ print "sending client check out email"
        # send email
        subject = "Return Appointment Reminder"
        msg = "Dear " + self.borrower_name + ',\n\n' +\
              "You have checked out " + self.title + \
              " from The Autism Society of Alaska's Library. " +\
              ". Your appointment to return the book is at " + \
              str(self.return_date)[11:16] + \
              " on " + str(self.return_date)[:10] +\
              ". \nThank you, \n\n The Autism Society of Alaska."
        sender = 'from@example.com'
        send_mail(subject, msg, sender,[self.email], fail_silently=True)
        # claculete time to a date before & sleep
        # send email
        # end thread
        
    def email_aco(self):
        #~ print "sending admin check out email"
        # send email
        subject = "Return Appointment Reminder"
        msg = self.borrower_name + 'has checked out ' + self.title + \
              ", the Physincal ID is " + str(self.phys_id) + \
              ". The appointment to return the book is at " + \
              str(self.return_date)[11:16] + \
              " on " + str(self.return_date)[:10] +\
              ". \nThank you, \n\n The Autism Society of Alaska."
        sender = 'from@example.com'
        mail_admins(subject, msg, fail_silently=True)
        # claculete time to a date before & sleep
        # send email
        # end thread
        
    class Meta:
        verbose_name ='Library Item'
    

#~ class Borower(models.Model):
    #~ """
        #~ borrower database model -- TODO merge with Library Item
    #~ """
    #~ types= (
        #~ ('0', 'Available'),
        #~ ('1', 'Reserved'),
        #~ ('2', 'Checked Out'),
    #~ )
    #~ status = models.CharField(max_length=1, choices=types, default="0")
    #~ 
    #~ 
    #~ resource = models.ForeignKey(RLibrary)
    #~ borrower_name = models.CharField(max_length = 50, blank=True)
    #~ phone = models.CharField(max_length = 10)
    #~ email = models.CharField(max_length = 50)
    #~ checkout_date = models.DateField(blank=True, null=True)
    #~ return_date = models.DateField(blank=True, null=True)
    

    
class ROnline(Resource):
    """
    database model for online items 
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
    url = models.URLField(blank=True)
    class Meta:
        verbose_name ='Online Item'
        


class REvent(Resource):
    """
    database model for events
    """
    # add types? fund raiser, meet and great, etc. 
    date_time = models.DateTimeField()
    location = models.TextField(blank=True)
    archive = models.BooleanField(default = False, verbose_name="Archive Event")
    # what else?
    
    def clean(self):
        #~ self.show_in_browser = '1'
        now = datetime.now(utc)
        self.show_in_browser = True
        self.save()
        if  (self.date_time < now) and not self.archive:
            raise ValidationError("The date & time for the event must be in"+\
            "the future, or the event must be archived")
        if self.archive:
            self.show_in_browser = False
            self.save()
            return
        t = Thread(target = self.hide)
        t.start()
    
    def hide(self):
        now = datetime.now(utc)
        #~ print (self.date_time-now).seconds + 2*60*60
        sleep((self.date_time-now).seconds + 2*60*60)
        #~ print "false"
        self.show_in_browser = False
        #~ print self.show_in_browser
        self.save()
        
    class Meta:
        verbose_name ='Event'
    


class RService(Resource):
    """
    database model for services
    """
    address = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    url = models.URLField(blank=True)
    class Meta:
        verbose_name ='Service'



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
    safety_home = models.BooleanField(default=False, verbose_name="Safety Home")
    safety_public = models.BooleanField(default=False, 
                                            verbose_name="Safety Public")
    safety_travel = models.BooleanField(default=False,
                                            verbose_name="Safety Travel")
    repetition = models.BooleanField(default=False)
    aggression = models.BooleanField(default=False)
    communication = models.BooleanField(default=False)
    nonverbal = models.BooleanField(default=False)
    sensory = models.BooleanField(default=False)
    meltdown = models.BooleanField(default=False)
    anxiety = models.BooleanField(default=False)
    change = models.BooleanField(default=False)
    nutrition = models.BooleanField(default=False)
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
                            verbose_name= "Asperger Syndrome")
    cdd = models.BooleanField(default=False,
                            verbose_name= "Cognitive Development Disorder")
    
    class Meta:
         verbose_name_plural = verbose_name = "Disorders"



class SServices(models.Model):
    """
    service search related item Database model
    """
    cities = (
        ('0', 'State Wide'),
        ('1', 'Anchorage'),
        ('2', 'Fairbanks'),
        ('3', 'Juno'),
    )
    
    resourceLink = models.ForeignKey(Resource)
    diagnostic = models.BooleanField(default=False)
    resource = models.BooleanField(default=False)
    therapy = models.BooleanField(default=False)
    educational = models.BooleanField(default=False)
    referral = models.BooleanField(default=False)
    legal = models.BooleanField(default=False)
    city = models.CharField(max_length = 1, choices=cities)
    
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
