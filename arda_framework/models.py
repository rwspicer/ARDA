# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AssociatedDisorder(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True)  # Field name made lowercase.
    resource = models.ForeignKey('Resource', db_column='RESOURCE_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASSOCIATED_DISORDER'


class Behavior(models.Model):
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True)  # Field name made lowercase.
    resource = models.ForeignKey('Resource', db_column='RESOURCE_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BEHAVIOR'


class Borrower(models.Model):
    first_name = models.CharField(db_column='First_name', primary_key=True, max_length=45)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=45, blank=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_address', max_length=45, blank=True)  # Field name made lowercase.
    reserved = models.IntegerField(db_column='Reserved', blank=True, null=True)  # Field name made lowercase.
    checkout_date = models.DateTimeField(db_column='Checkout_date', blank=True, null=True)  # Field name made lowercase.
    return_date = models.DateTimeField(db_column='Return_date', blank=True, null=True)  # Field name made lowercase.
    library_item_resource = models.ForeignKey('LibraryItem', db_column='LIBRARY_ITEM_RESOURCE_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BORROWER'


class Event(models.Model):
    location = models.CharField(db_column='Location', max_length=100)  # Field name made lowercase.
    resource = models.ForeignKey('Resource', db_column='RESOURCE_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENT'


class LibraryItem(models.Model):
    old_item_id = models.IntegerField(db_column='Old_Item_id')  # Field name made lowercase.
    item_type = models.CharField(db_column='Item_type', max_length=45)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=45, blank=True)  # Field name made lowercase.
    resource = models.ForeignKey('Resource', db_column='RESOURCE_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LIBRARY_ITEM'


class Online(models.Model):
    url = models.TextField(db_column='Url')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.
    resource = models.ForeignKey('Resource', db_column='RESOURCE_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONLINE'


class Resource(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    email = models.CharField(db_column='Email', max_length=100, blank=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_number', max_length=15, blank=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1)  # Field name made lowercase.
    age_range = models.CharField(db_column='Age_range', max_length=5)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESOURCE'


class Therapy(models.Model):
    location = models.CharField(db_column='Location', max_length=100, blank=True)  # Field name made lowercase.
    insuarance_info = models.CharField(db_column='Insuarance_info', max_length=45, blank=True)  # Field name made lowercase.
    resource = models.ForeignKey(Resource, db_column='RESOURCE_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'THERAPY'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
