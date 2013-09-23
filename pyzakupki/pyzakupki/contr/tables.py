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
            fullstr = "/obj/%s/{{record.uid}}/" % str_obj_name
            title = str_obj
            attrs = {"class": "paleblue"}
            exclude = ('uid','parent_uid','file','signature')

        def render_regnum(self,value):
            return mark_safe('''<a href="/obj/%s/regnum/?q=%s">%s</a>'''% (str_obj,value,value))

        def render_inn(self,value):
            return mark_safe('''<a href="/obj/%s/inn/?q=%s">%s</a>'''% (str_obj,value,value))
        def render_notificationnumber(self,value):
            return mark_safe('''<a href="/obj/Notf/notificationnumber/?q=%s">%s</a>'''% (value,value))


    return SimpleTable(obj)

