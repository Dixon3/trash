# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.forms.models import modelformset_factory
from customers.models import CustomersOrgs
from django.db import connection
from contr.models import *
from django_tables2.utils import A 
from django_tables2 import RequestConfig
from utils import *
from forms import *
from tables import *
import django_tables2 as tables

import inspect,sys
import collections
import logging
import os.path
import json

logger = logging.getLogger(__name__)

def generate_table(objects_query,obj_type):
    logger.debug("Object:%s,Object_Type:%s"%(object,obj_type))
    table = create_table(objects_query,obj_type)
    return table


def getChildObjects(object):
    result={}
    obj_list=[]
    links = [rel.get_accessor_name() for rel in object._meta.get_all_related_objects()]
    for link in links:
        objects = getattr(object, link).all()
        if len(objects)>0:
            for obj in objects:
                logger.debug(link,obj.uid)
                getChildObjects(obj)
            
    return result

def contr(request,contr_id):
    c = Contr.objects.filter(uid=contr_id) 
    #childs=getChildObjects(c)
    table = SimpleTable(c)
    return render(request,'contr/contr.html',{'table':table})

def object(request,obj_type,obj_id):   
               
    obj_type = model_factory(obj_type)
    obj = obj_type.objects.filter(pk=obj_id)
    main_table=generate_table(obj,obj_type) 
    top_level=obj.get()   
    parents=[]   

    try:    
        parent = obj.get().parent_uid    
        while 1:                       
            logger.info("Parent:"+str(parent))
            parent.str_name=str(parent).split(" ")[0]
            parents.append(parent)
            obj=parent
            parent = obj.parent_uid
    except AttributeError:
        logger.debug("Not Found attr:%s")

    
    logger.debug("Parents:%s"%(parents))
    
    parents.reverse()
    

    childs=[]
    childs_model=[]
    main_tree=collections.defaultdict(list)

    def getChildObjects(object):
        result={}
        obj_list=[]
        links = [rel.get_accessor_name() for rel in object._meta.get_all_related_objects()]
        logger.debug("Object:%sLinks:%s"%(object,links))  
        for link in links:
            objects = getattr(object, link).all()
            if len(objects)>0:
                chlds=[]
                for obj in objects:
                    childs_model.append(model_factory(str(obj).split(" ")[0]))
                    main_tree[model_factory(str(obj).split(" ")[0])].append(obj)
                    getChildObjects(obj)

    getChildObjects(top_level)   
       
    logger.debug("Main tree:"+str(main_tree))
    child_tables=[]
    
    for i in main_tree.keys():
        ids = [o.pk for o in main_tree[i]]
        model_string=str(main_tree[i][0]).split(" ")[0]
        mdl=model_factory(model_string)
        objs_query=mdl.objects.filter(pk__in=ids) 
        tab=generate_table(objs_query,mdl)
        tab.str_name=model_string
        child_tables.append(tab)
    return render(request,'contr/object.html',{'parents':parents,'table':main_table,'child_tables':child_tables})

    

def search(request,obj_type,column): 
    form=SearchForm()
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = SearchForm() # An unbound form

    obj_type = model_factory(obj_type)
    q=request.GET.get('q')
    logger.debug("Search:%s=%s"%(column,q))
    kwargs = {column:q}
    obj= obj_type.objects.filter(**kwargs)
    main_table=generate_table(obj,obj_type)
    RequestConfig(request,paginate=True).configure(main_table)
    return render(request,'contr/object.html',{'form':form,'table':main_table})
   

def search_obj_by_child(request,obj_type,column):
    obj_type_mdl = model_factory(obj_type)
    q=request.GET.get('q')
    view=request.GET.get('v')
    repr=model_factory(view)
    sm=SearchManager()
    o=sm.SearchObjects(obj_type_mdl,column,q,view)    
    o=sm.SearchObjects2(obj_type_mdl,column,q,view)    
    tab=generate_table([dict(i.__dict__) for i in o],repr)
    RequestConfig(request,paginate=True).configure(tab)
    return render(request,'contr/object.html',{'table':tab})

def objects_json(request):
    response_data={}
    q=request.GET.get('q')
    clsmembers = inspect.getmembers(sys.modules['contr.models'], inspect.isclass)
    members = dict(clsmembers).keys()
    #filtered = [i for i in members if i.startswith(q)]
    response_data['objects']=members
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    
def search_by_q(request):
    if request.method == "POST":
        print request
    
    searchform=SearchForm()
    return render(request,'search.html', {"searchform": searchform,})
    
