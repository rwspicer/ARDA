from django.db import models
# Create your models here.


# types of the resoures in the database
RESOURCE_TYPES = (
        ('0', 'libaray'),
        ('1', 'service'),
        ('2', 'online')
    )


class Resource(models.Model):
    """
        Base Resource model, so that all types have a common numbering system
    """
    #~ r_type = 'none'
    r_id = models.AutoField(primary_key = True)
    #~ r_type = 'none'#models.CharField(max_length=1, choices=RESOURCE_TYPES)
    title = models.CharField(max_length = 90, default='title')
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title + "    " + self.description
    #~ class Meta:
        #~ abstract = True


class RLibrary(Resource):
    """
        Library item database model
    """
    phys_id = models.IntegerField(null=True)
    author = models.CharField(max_length = 60)
    #~ Resource.r_type = 'library'#models.CharField(max_length=1, choices=(('0','library'),), default = '0')
    # TODO: list all the types
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
    # TODO: list all the catagories
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
    library = True
    class Meta:
        verbose_name ='library item'
    

class Borower(models.Model):
    """
        borrower database model
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
    types = (
        ('0', 'video'),
        ('1', 'article'),
        ('2', 'web site')
    )
    otype = models.CharField(max_length = 1, choices=types, verbose_name ="type")
    date = models.DateField()
    url = models.TextField(blank=True)
    online = True
    #~ def __unicode__(self):
        #~ return self.title + self.types[int(self.otype)][-1]+ ' ' + str(self.date) + ' ' + str(self.url) + ' ' + "online" 
    class Meta:
        verbose_name ='online item'

class RService(Resource):
    address = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    url = models.TextField(blank=True)
    service = True
    class Meta:
        verbose_name ='service'

class SDemo(models.Model):
    resource = models.ForeignKey(Resource)
    age1to3 = models.BooleanField(default=False, verbose_name= "Age 1-3")
    age3to18 = models.BooleanField(default=False, verbose_name= "Age 3-18")
    age18plus = models.BooleanField(default=False, verbose_name= "Age 18+")
    gender_m = models.BooleanField(default=False, verbose_name= "Male")
    gender_f = models.BooleanField(default=False,  verbose_name= "Female")
    
    class Meta:
        verbose_name = "Demographics"

class SBehaviour(models.Model):
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
        verbose_name = "Behaviors"

class SDisorder(models.Model):
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
        verbose_name = "Disorders"

class SServices(models.Model):
    resourceLink = models.ForeignKey(Resource)
    diagnostic = models.BooleanField(default=False)
    resource = models.BooleanField(default=False)
    therapy = models.BooleanField(default=False)
    educational = models.BooleanField(default=False)
    referral = models.BooleanField(default=False)
    legal = models.BooleanField(default=False)
    city = models.CharField(max_length = 30)
    
    class Meta:
        verbose_name = "Service Features"

#~ ('2', 'Resources for Professionals & Parents'),
        #~ ('3', 'Couple Relationships'),
        #~ ('4', 'Resources for Teaching Children/School'),
        #~ ('5', 'Support for Siblings'),
        #~ ('6', 'Resources for Older Children, Teens & Adults'),

class SAdditional(models.Model):
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
        verbose_name = "Additional Search optiions"
