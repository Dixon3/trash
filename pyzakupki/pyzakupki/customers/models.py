from contr.models import ContrCustomer
from django.db import models


# Create your models here.



class CustomersOrgs(models.Model):
    url = models.TextField(blank=True)
    own_spz = models.BigIntegerField(null=True, blank=True)
    polnomochie_org = models.TextField(blank=True)
    full_name = models.TextField(blank=True)
    short_name = models.TextField(blank=True)
    inn = models.BigIntegerField(null=True, blank=True)
    kpp = models.TextField(blank=True)
    org_type = models.TextField(blank=True)
    org_level = models.TextField(blank=True)
    buget_code = models.BigIntegerField(null=True, blank=True)
    buget_name = models.TextField(blank=True)
    admin_prin_spz = models.BigIntegerField(null=True, blank=True)
    admin_prin_name = models.TextField(blank=True)
    upper_org_spz = models.BigIntegerField(null=True, blank=True)
    okopf = models.BigIntegerField(null=True, blank=True)
    okogu = models.BigIntegerField(null=True, blank=True)
    okpo = models.BigIntegerField(null=True, blank=True)
    okved = models.TextField(blank=True)
    ogrn = models.BigIntegerField(null=True, blank=True)
    place = models.TextField(blank=True)
    okato = models.BigIntegerField(null=True, blank=True)
    upoln_organ = models.TextField(blank=True)
    telefon = models.TextField(blank=True)
    fax = models.TextField(blank=True)
    post_adress = models.TextField(blank=True)
    email = models.TextField(blank=True)
    contact_person = models.TextField(blank=True)
    timezone = models.TextField(blank=True)
    innetaddress = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)
    upper_org_name = models.TextField(blank=True)
    id = models.BigIntegerField(primary_key=True)

    def get_admin_parent(self):
        return CustomersOrgs.objects.get(own_spz=self.admin_prin_spz)
    def get_upper_parent(self):
        c= CustomersOrgs.objects.get(own_spz=self.upper_org_spz)
        return c
    def get_admin_childs(self):
        return CustomersOrgs.objects.filter(admin_prin_spz=self.own_spz)
    def get_childs(self):
        childs=CustomersOrgs.objects.filter(upper_org_spz=self.own_spz)
        print childs
        return CustomersOrgs.objects.filter(upper_org_spz=self.own_spz)

    def __unicode__(self):
        return u"ID:%s,%s" %(self.id,self.short_name)
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in CustomersOrgs._meta.fields]
    class Meta:
        db_table = 'customers_orgs'

class CustomerContrAggr(models.Model):
    regnum=models.BigIntegerField()
    inn=models.BigIntegerField()
    kpp=models.BigIntegerField()
    sum=models.DecimalField()                            
    count=models.BigIntegerField()
    def fullname(self):
        c=ContrCustomer.objects.filter(regnum=self.regnum)[0]
	return c.fullname    

    class Meta:
        db_table = 'customers_contr_aggr'


