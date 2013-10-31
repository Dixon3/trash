# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from customers.models import CustomersOrgs
from django.db import connection
from contr.models import *
from django_tables2.utils import A 
from django_tables2   import RequestConfig
from utils import *
from forms import *
from tables import *
import django_tables2 as tables

import inspect,sys
import collections
import logging
import os.path

logger = logging.getLogger(__name__)

def generate_table(objects_query,obj_type):
    logger.debug("Object:%s,Object_Type:%s"%(object,obj_type))
    table = create_table(objects_query,obj_type)
    return table


def getChildObjects(object):
    result={}
    obj_list=[]
    links = [rel.get_accessor_name() for rel in object._meta.get_all_related_objects()]
#    print "Object:",object,"Links:",links  
    for link in links:
        #print "link:",link
        objects = getattr(object, link).all()
        if len(objects)>0:
            for obj in objects:
                print link,obj.uid
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
            print "Parent:",parent
            parent.str_name=str(parent).split(" ")[0]
            parents.append(parent)
            obj=parent
            parent = obj.parent_uid
    except AttributeError:
        print "Not Found attr:%s"

    
    print "Parents",parents
    
    parents.reverse()
    

    childs=[]
    childs_model=[]
    main_tree=collections.defaultdict(list)

    def getChildObjects(object):
        result={}
        obj_list=[]
        links = [rel.get_accessor_name() for rel in object._meta.get_all_related_objects()]
        print "Object:",object,"Links:",links  
        for link in links:
            objects = getattr(object, link).all()
            if len(objects)>0:
                chlds=[]
                for obj in objects:
                    childs_model.append(model_factory(str(obj).split(" ")[0]))
                    main_tree[model_factory(str(obj).split(" ")[0])].append(obj)
                    getChildObjects(obj)

    getChildObjects(top_level)   
       
    print "Main tree:",main_tree
    child_tables=[]
    
    for i in main_tree.keys():
        ids = [o.pk for o in main_tree[i]]
        model_string=str(main_tree[i][0]).split(" ")[0]
        mdl=model_factory(model_string)
        objs_query=mdl.objects.filter(pk__in=ids) 
        tab=generate_table(objs_query,mdl)
        tab.str_name=model_string
        print dir(tab.data.data)
        print tab.data.data[0]
        child_tables.append(tab)
    return render(request,'contr/object.html',{'parents':parents,'table':main_table,'child_tables':child_tables})

    
    #print dir(main_table.Meta.model)
#    return render(request,'contr/object.html',{'table':main_table})


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
   

def generate_tables(common_table,table):
    """Generate list of tables between common_table and table"""
    delta_tables = table.replace(common_table,"")
    delta_tables_list = delta_tables.split("_")
    print delta_tables_list
    
    tmp=common_table  
    result=[]    

    for i in delta_tables_list[1:]:
        result.append(tmp+'_'+i)
        tmp = tmp+'_'+i
    result = [common_table]+result
    return result

def generate_join(tables_list):

    tmp=tables_list[0]
    s=[]
   
    for i in tables_list[1:]:
        s.append("%s.uid = %s.parent_uid" % (tmp,i))
        tmp=i

    #result = " and ".join(s)
    result = s 
    print "Generated join:",result

    return result

def get_uniq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def search_obj_by_child(request,obj_type,column):

    obj_type_mdl = model_factory(obj_type)
    q=request.GET.get('q')
    view=request.GET.get('v')
    repr=model_factory(view)
    kwargs = {column:q}
    #print dir(obj_type_mdl._meta.db_table)
    current_table = obj_type_mdl._meta.db_table
    represent_table = repr._meta.db_table
    #obj = obj_type.objects.filter(**kwargs)
    print current_table,represent_table, zip(represent_table,current_table)
    # Root to build join SQL request
    common_table=os.path.commonprefix([current_table,represent_table])

    common_table = "_"+common_table.split("_")[1] 
    tables_to_current=generate_tables(common_table,current_table)
    tables_to_represent = generate_tables(common_table,represent_table)
    
    print "Common table:",common_table
    print "tables_to_current:",tables_to_current
    print "tables_to_represent:",tables_to_represent

    select_from_statement = ",".join(get_uniq(tables_to_current+tables_to_represent))
    print "select from:", select_from_statement
    join_to_repr = generate_join(tables_to_represent)        
    join_to_curr = generate_join(tables_to_current)
    
    joins = " and ".join (join_to_repr+join_to_curr)

    q="select \
       %s.*\
       from \
       %s \
       where \
       %s and %s.%s=%s;" %(represent_table,select_from_statement,joins,current_table,column,q)

    print "Query:",q

    o=repr.objects.raw(q)

    tab=generate_table([dict(i.__dict__) for i in o],repr)
    RequestConfig(request,paginate=True).configure(tab)
    return render(request,'contr/object.html',{'table':tab})


