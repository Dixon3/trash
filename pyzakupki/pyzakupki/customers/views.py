# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from customers.models import CustomersOrgs
from django.db import connection
from contr.models import ContrCustomer
import django_tables2 as tables

import datetime,sys,inspect

def model_factory(string):
    clsmembers = inspect.getmembers(sys.modules['customers.models'], inspect.isclass)
    members = dict(clsmembers)
    return members[string]

def generate_table(object,obj_type='None'):
    print object,obj_type
    print obj_type
    print object.__class__,obj_type.__class__
    class SimpleTable(tables.Table):
        class Meta:
            model = obj_type
            exclude = ('uid','parent_uid','file','signature')
    #childs=getChildObjects(c)
    table = SimpleTable(object)
    return table



def index(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def customer(request,customer_id):
    c=CustomersOrgs.objects.get(id=customer_id)
    c2=CustomersOrgs.objects.filter(id=customer_id)
    generate_table(c2)
    upper_parents=[]
    upper_parent=c.get_upper_parent()
    upper_parents.append(upper_parent)
    while (upper_parent!=c.get_upper_parent()):
        tmp=upper_parent
        upper_parent=tmp.get_upper_parent()
        upper_parents.append(tmp)      
    admin_parents=[]
    admin_parent=c.get_admin_parent()
    admin_parents.append(admin_parent)

    while (admin_parent!=c.get_admin_parent()):
        tmp=admin_parent
        admin_parent=tmp.get_admin_parent()
        admin_parents.append(tmp)
    childs=c.get_childs()       
    admin_childs = c.get_admin_childs()
    return render(request,'customers/customer.html',{'customer':c,'upper_parents':upper_parents,'admin_parents':admin_parents,'childs':childs,'admin_childs':admin_childs})


def customer_contracts(request,customer_id):
    c=CustomersOrgs.objects.get(id=customer_id)
    spz=c.own_spz
    cust_contr=ContrCustomer.objects.filter(regnum=spz)
    contr = [i.parent_uid for i in cust_contr]
    print contr
    return render(request,'contr/contr.html',{'contr':contr_list})

def customers_bybudget(request,budget_id):
    c=CustomersOrgs.objects.filter(buget_code=budget_id).all()
    return render(request,'customers/budget.html',{'customers':c})

def customers_contracts(request,customer_id):
    c=CustomersOrgs.objects.get(id=customer_id)
     

    
