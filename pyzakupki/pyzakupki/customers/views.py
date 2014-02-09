# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from customers.models import CustomerContrAggr
from contr.models import *
from django.db import connection
from contr.models import *
from contr.tables import *
from contr.utils import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Max

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
    if request.GET.get('order') in ['count','-count','sum','-sum']:
       order = request.GET.get('order')
    else:
       order = '-count'
    customers_list = CustomerContrAggr.objects.all().order_by(order)
    paginator = Paginator(customers_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customers = paginator.page(paginator.num_pages)
    return render(request,'customers/index.html', {"customers": customers,"order":order})
    #return render(request, 'customers/index.html', {'table': table})

def customer(request,regnum):
    if request.GET.get('order') in ['price','-price','signdate','-signdate']:
       order = request.GET.get('order')
    else:
       order = '-signdate'
    customer=CustomersOrgs.objects.get(own_spz=regnum)
    contracts_list = Contr.objects.filter(contrcustomer__regnum=regnum).order_by(order)
    paginator = Paginator(contracts_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contracts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contracts = paginator.page(paginator.num_pages)

    return render(request,'customers/customer.html',{'customer':customer,'contracts':contracts,"order":order})


#def customer_contracts(request,customer_id):
#    c=CustomersOrgs.objects.get(id=customer_id)
#    spz=c.own_spz
#    cust_contr=ContrCustomer.objects.filter(regnum=spz)
#    contr = [i.parent_uid for i in cust_contr]
#    print contr
#    return render(request,'contr/contr.html',{'contr':contr_list})

def customers_bybudget(request,budget_id):
    c=CustomersOrgs.objects.filter(buget_code=budget_id).all()
    return render(request,'customers/budget.html',{'customers':c})

def customers_contracts(request,customer_id):
    c=CustomersOrgs.objects.get(id=customer_id)
     

    
