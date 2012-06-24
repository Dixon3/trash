# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

SCHEMA_NAME = 'vladimirskaja_obl\".\"'

class Contracts(models.Model):
    order_uid = models.BigIntegerField(primary_key=True)
    code = models.TextField()
    name = models.TextField()
    currentcontractstage = models.TextField()
    documentbase = models.TextField()
    month = models.FloatField()
    year = models.FloatField()
    foundation = models.TextField()
    notificationnumber = models.TextField()
    placing = models.TextField()
    singlecustomer = models.TextField()
    id = models.FloatField()
    price = models.FloatField()
    url = models.TextField()
    protocoldate = models.TextField()
    publishdate = models.TextField()
    regnum = models.BigIntegerField()
    signdate = models.TextField()
    versionnumber = models.FloatField()
    number = models.TextField()
    class Meta:
        db_table = SCHEMA_NAME+u'contracts'

class ContractsSuppliers(models.Model):
    order_uid = models.ForeignKey(Contracts, db_column='order_uid')
    participanttype = models.TextField()
    inn = models.FloatField()
    kpp = models.FloatField()
    organizationform = models.TextField()
    organizationname = models.TextField()
    countrycode = models.FloatField()
    countryfullname = models.TextField()
    factualaddress = models.TextField()
    postaddress = models.TextField()
    lastname = models.TextField()
    firstname = models.TextField()
    middlename = models.TextField()
    contactemail = models.TextField()
    contactphone = models.TextField()
    contactfax = models.TextField()
    class Meta:
        db_table = SCHEMA_NAME+u'contracts_suppliers'

class ContractsFinances(models.Model):
    order_uid = models.ForeignKey(Contracts, db_column='order_uid')
    financesource = models.TextField()
    code = models.TextField()
    name = models.TextField()
    month = models.FloatField()
    year = models.FloatField()
    kosgu = models.TextField()
    price = models.FloatField()
    class Meta:
        db_table = SCHEMA_NAME+u'contracts_finances'

class ContractsCustomers(models.Model):
    order_uid = models.ForeignKey(Contracts, db_column='order_uid')
    regnum = models.FloatField()
    fullname = models.TextField()
    inn = models.FloatField()
    kpp = models.FloatField()
    tofk = models.FloatField()
    class Meta:
        db_table = SCHEMA_NAME+u'contracts_customers'

class ContractsProducts(models.Model):
    order_uid = models.ForeignKey(Contracts, db_column='order_uid')
    name = models.TextField()
    countrycode = models.TextField()
    countryfullname = models.TextField()
    okei_code = models.TextField()
    okei_name = models.TextField()
    price = models.FloatField()
    sum = models.FloatField()
    product_uid = models.TextField()
    odkp_code = models.TextField()
    odkp_name = models.TextField()
    qantity = models.FloatField()
    class Meta:
        db_table = SCHEMA_NAME+u'contracts_products'

