from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    application_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True)
    date = models.TextField(blank=True, null=False)
    applicant = models.TextField(blank=True, null=False)
    status = models.TextField(blank=True, null=False)
    data = models.TextField(blank=True, null=False)
    validator = models.TextField(blank=True, null=False)
    verify_time = models.TextField(blank=True, null=False)
    content = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'application'

    def __str__(self):
        return self.applicant

class Customers(models.Model):#OK
    customer_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True)
    name = models.TextField(blank=True, null=False)
    site = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name

class Groups(models.Model):#OK
    group_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True)
    name = models.TextField(blank=True, null=False)
    caption = models.TextField(blank=True, null=False)
    authority = models.TextField(blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    members = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.name

class Info(models.Model):#OK
    info_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True)
    sn = models.IntegerField(blank=True, null=False)
    func_uid = models.TextField(blank=True, null=False)
    version = models.TextField(blank=True, null=False)
    issued = models.TextField(blank=True, null=False)
    expiration = models.TextField(blank=True, null=False)
    count = models.IntegerField(blank=True, null=False)
    registration = models.TextField(blank=True, null=False)
    type = models.TextField(blank=True, null=False)
    comment = models.TextField(blank=True, null=False)
    contact = models.TextField(blank=True, null=False)
    info = models.TextField(blank = True, null=False)
    class Meta:
        db_table = 'info'

    def __str__(self):
        return self.sn

class Modules(models.Model):#OK
    module_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True) 
    category = models.IntegerField(blank=True, null=False)
    mod_uid = models.TextField(blank=True, null=False)
    caption = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'modules'

    def __str__(self):
        return self.mod_uid

class Products(models.Model):#OK
    product_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True) 
    name = models.TextField(blank=True, null=False)
    caption = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class Region(models.Model):#OK
    region_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True) 
    name = models.TextField(blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'region'

    def __str__(self):
        return self.name

class Sn(models.Model):#OK
    my_id = models.IntegerField(db_column='my_id', unique=True, blank=True, null=False, primary_key=True) 
    sn_id = models.IntegerField(db_column='id',blank=True, null=False) 
    sn = models.IntegerField(blank=True, null=False)
    region = models.TextField(blank=True, null=False)#怪怪的
    user = models.TextField(blank=True, null=False)
    record = models.TextField(blank=True, null=False)
    note1 = models.TextField(blank=True, null=False)
    note2 = models.TextField(blank=True, null=False)
    note3 = models.TextField(blank=True, null=False)
    note4 = models.TextField(blank=True, null=False)
    note5 = models.TextField(blank=True, null=False)

    class Meta:
        db_table = 'sn'

    def __str__(self):
        return self.sn

class Users(models.Model):#OK
    user_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True)
    user = models.TextField(blank=True, null=False)
    password = models.TextField(blank=True, null=False)
    email = models.TextField(blank=True, null=False)
    groups = models.TextField(blank=True, null=False)
    region = models.TextField(blank=True, null=False)
    record = models.TextField(blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.user

class Edit(models.Model):
    id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True)
    user = models.TextField(blank=True, null=False)
    cc = models.TextField(blank=True, null=False)
    data = models.TextField(blank=True, null=False)
    comment = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'edit'

    def __str__(self):
        return self.user
