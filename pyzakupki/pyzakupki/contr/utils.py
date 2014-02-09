from django.http import HttpResponse
from django.shortcuts import render
from customers.models import CustomersOrgs
from django.db import connection
from contr.models import *
from django_tables2.utils import A 
from django_tables2   import RequestConfig


from sql import *

import inspect,sys,os,logging
import collections

logger = logging.getLogger(__name__)


def model_factory(string):
    clsmembers = inspect.getmembers(sys.modules['contr.models'], inspect.isclass)
    #clsmembers = inspect.getmembers(sys.modules['customers.models'], inspect.isclass) 
    members = dict(clsmembers)
    logger.debug('Members'+str(members))
    return members[string]


def model_factory_back(object):
    clsmembers = inspect.getmembers(sys.modules['contr.models'], inspect.isclass)
    #clsmembers = inspect.getmembers(sys.modules['customers.models'], inspect.isclass)
    members = dict(clsmembers)   
    inv_map = dict((v,k) for k, v in members.items())
    return inv_map[object]

def generate_tables(common_table,table):
    """Generate list of tables between common_table and table"""
    delta_tables = table.replace(common_table,"")
    delta_tables_list = delta_tables.split("_")
    logger.debug('delta_tables_list:'+str(delta_tables_list))
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
    logger.debug("Generated join:"+str(result))
    return result

def get_uniq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]




class SearchManager(object):

    def __init__(self):
        pass

    def SearchObjects(self,obj_type_mdl,column,q,view):

        repr=model_factory(view)
        kwargs = {column:q}   
        current_table = obj_type_mdl._meta.db_table
        represent_table = repr._meta.db_table
        #obj = obj_type.objects.filter(**kwargs)
        #logger.debug(current_table+represent_table+zip(represent_table,current_table))
        # Root to build join SQL request
        common_table=os.path.commonprefix([current_table,represent_table])
        common_table = "_"+common_table.split("_")[1] 
        tables_to_current=generate_tables(common_table,current_table)
        tables_to_represent = generate_tables(common_table,represent_table)
    
        logger.debug("Common table:"+str(common_table))
        logger.debug("tables_to_current:"+str(tables_to_current))
        logger.debug("tables_to_represent:"+str(tables_to_represent))

        select_from_statement = ",".join(get_uniq(tables_to_current+tables_to_represent))
        logger.info("select from:%s" %(select_from_statement))
        join_to_repr = generate_join(tables_to_represent)        
        join_to_curr = generate_join(tables_to_current)
    
        joins = " and ".join (join_to_repr+join_to_curr)

        q="select \
        %s.*\
        from \
        %s \
        where \
        %s and %s.%s=%s;" %(represent_table,select_from_statement,joins,current_table,column,q)

        logger.debug("Query:"+q)
        o=repr.objects.raw(q)
        return o


    def SearchObjects2(self,obj_type_mdl,column,q,view):

        repr=model_factory(view)
        kwargs = {column:q}          
        current_table = obj_type_mdl._meta.db_table
        represent_table = repr._meta.db_table
        common_table=os.path.commonprefix([current_table,represent_table])
        common_table = "_"+common_table.split("_")[1] 
        tables_to_current=generate_tables(common_table,current_table)
        tables_to_represent = generate_tables(common_table,represent_table)

        logger.info("Common table:%s"%common_table)
        logger.info("tables_to_current:%s"%tables_to_current)
        logger.info("tables_to_represent:%s"%tables_to_represent)

        all_tables=get_uniq(tables_to_current+tables_to_represent)
        
        tables = []
        for i in all_tables:
            tables.append(Table(i))
        
        return 0


