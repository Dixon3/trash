from django.http import HttpResponse
from django.shortcuts import render
from customers.models import CustomersOrgs
from django.db import connection
from contr.models import *
from django_tables2.utils import A 
from django_tables2   import RequestConfig

import inspect,sys
import collections




def model_factory(string):
    clsmembers = inspect.getmembers(sys.modules['contr.models'], inspect.isclass)
    members = dict(clsmembers)
#    print members
    return members[string]


def model_factory_back(object):
    clsmembers = inspect.getmembers(sys.modules['contr.models'], inspect.isclass)
    members = dict(clsmembers)   
    inv_map = dict((v,k) for k, v in members.items())
#    print inv_map
#    print inv_map[object]
    return inv_map[object]

