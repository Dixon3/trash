import django_tables2 as tables
import itertools
from django.utils.safestring import mark_safe
from utils import *


def create_table(obj,obj_type):


    str_obj=model_factory_back(obj_type)

    class SimpleTable(tables.Table):   
    
        link=tables.TemplateColumn('<a href="/obj/%s/{{record.uid}}">More</a>'% str_obj)
        class Meta:
            model=obj_type
            str_obj_name = str_obj
            is_map=False
            print str_obj_name.find("Geocode")
            if str_obj_name.find("Geocode") >= 0:
                print "This have map!!!"
                is_map = True           
            print is_map
            fullstr = "/obj/%s/{{record.uid}}/" % str_obj_name
            title = str_obj
            attrs = {"class": "table table-hover table_condensed paleblue"}
            exclude = ('uid','parent_uid','file','signature')

        def render_regnum(self,value):
            return mark_safe('''<a href="/obj/%s/regnum/?q=%s">%s</a>'''% (str_obj,value,value))
        def render_inn(self,value):
            return mark_safe('''<a href="/obj/%s/inn/?q=%s">%s</a>'''% (str_obj,value,value))
        def render_notificationnumber(self,value):
            notif_search=mark_safe('''<a href="/obj/Notf/notificationnumber/?q=%s">n|</a>'''% (value))
            protc_search=mark_safe('''<a href="/obj/Prtk/notificationnumber/?q=%s">p|</a>'''% (value))
            contr_search=mark_safe('''<a href="/obj/ContrFoundationOrder/notificationnumber/sear/?q=\'%s\'&v=Contr">c</a>'''% (value))
            return mark_safe('''<a href="/obj/%s/notificationnumber/?q=%s">%s</a>|'''% (str_obj,value,value))+notif_search+protc_search +contr_search


    return SimpleTable(obj)

