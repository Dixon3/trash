#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import codecs, sys

#tree = etree.parse('contract__Vladimirskaja_obl_inc_20110101_000000_20110201_000000_161.xml')
tree = etree.parse(sys.stdin)
#tree = etree.parse('contract__Vladimirskaja_obl_inc_20120701_000000_20120801_000000_234.xml')
root = tree.xpath(".")
elements=root[0].xpath("./*")


tables=dict()
values=dict()
uids=dict()
#Schema related 
SCHEMA='public'
PK=['uid']
FK_IS=['uid']
FK=['parent_uid']
INTEGER=['month','year','id','versionNumber','kpp','countryCode']
BIGINTEGER=['inn','regNum','notificationNumber','uid','parent_uid']
FLOAT=[]
NUMERIC=['price','sum','quantity']
VARCHAR=['']

# IF need modify field name in output
COLUMN_MAPPING={
'placing':'pplacing'
}



def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]


def handle_element(parent,elem):
    #print elem
    #print elem ,parent,":",elem.xpath("text()[normalize-space()]"),elem.xpath("./*"), len(elem.xpath("./*"))
    if len(elem.xpath("./*"))>0:

        key=parent+'_'+(elem.xpath("local-name()"))
        if key not in tables.keys():
            tables[parent+'_'+(elem.xpath("local-name()"))]=[]
        if key not in values.keys():
            values[parent+'_'+(elem.xpath("local-name()"))]=[]
        #next_element.append(elem)
    else:
        tables[parent]+=[elem.xpath("local-name()")]
        column_name=parent+'_'+elem.xpath("local-name()") 
        if column_name not in values.keys():
            values[column_name]=[]
            values[column_name]+=[elem.xpath("text()")]
        else:
            values[column_name]+=[elem.xpath("text()")]
           # print values
       # print values
    for i in elem:
        par=parent+'_'+elem.xpath("local-name()")
        handle_element(par,i)

def generate_types(columns):
    result=[]
    for i in columns:
        if i in PK:
            result.append(i+' bigint primary key') 
        elif i in INTEGER:
            result.append(i+' integer')
        elif i in BIGINTEGER:
            result.append(i+' bigint')
        elif i in VARCHAR:
            result.append(i+' varchar(2000)')
        elif i in FLOAT:
            result.append(i+' float')
        elif i in NUMERIC:
            result.append(i+' numeric')
        else:
            result.append(i+' text')
    return result

def getParent(table):
    table_list=table.split('_')
    result=["_"]
    parent="_".join(table_list[0:-1])
    result+=parent
    result="".join(parent)
    return result

def sortByHierarhy(tables_list):
    return tables_list.sort()    
            

def generate_create_tables(tables):
    for i in sorted(tables.keys()):
        columns=uniq(tables[i])
        columns.append(PK[0])
        columns=generate_types(columns)
        columns=",".join(columns)
        parent = getParent(i)
        #print parent
        sql=''
        if len(parent)==0:
            sql="create table "+SCHEMA+'.'+ i +" ("+columns+");" 
        else:
            sql="create table "+SCHEMA+'.'+ i +" ("+columns+", parent_uid bigint references "+parent+"("+FK_IS[0]+")"+" );"
        print sql


def extract_column_for_table(table,columns):
    result=[]
    for i in columns:
        prefix = i.split(table)
        #print prefix
        if len(prefix)>1 and i not in tables.keys():
            if i.split(table)[1][0]=='_' and len(i.split(table)[1].split('_'))-1==1:
                result+=[i] 
    #print table,result
    return result

def extract_column_names(raw):
    result=[]
    for i in raw:
        tab = getParent(i)
        tmp=i.split(tab)
        result.append(tmp[-1][1:])
    return result

def generate_insert_statements(columns_data):
    tabs=sorted(tables.keys())
    columns=columns_data.keys()
    for tab in tabs:
        col = extract_column_for_table(tab,columns)
        col_names = extract_column_names(col)
        val =[] 
        for i in col:
            val.append(columns_data[i])
        ind=0
        curr_val=[]
        for i in val:
            if i:
                curr_val.append(i.pop())
            else:
                curr_val.append('None') 
    
        uid=1
        parent_uid=None
        if len(getParent(tab))>0:
            if tab in uids.keys():
                uids[tab]+=1
                uid=uids[tab]
                parent_uid=uids[getParent(tab)]
            else:
                uids[tab]=1
                parent_uid=uids[getParent(tab)] 
            col_names.append('uid')
            col_names.append('parent_uid')
            curr_val.append(str(uid))
            curr_val.append(str(parent_uid))
        else:
            if tab in uids.keys():
                uids[tab]+=1
                uid=uids[tab]
            else:
                uids[tab]=1
            col_names.append('uid')
            curr_val.append(str(uid))
        #print tab,getParent(tab),uid,parent_uid 
        fields_dict = dict(zip(col_names, curr_val))
        for field in fields_dict.keys():
            if field not in NUMERIC or INTEGER or BIGINTEGER:
                fields_dict[field]='\''+"".join(fields_dict[field])+'\''
                
        sql_columns= ",".join(fields_dict.keys())
        sql_values= ",".join(fields_dict.values())
        sql = 'insert into '+SCHEMA+'.'+ tab +" ("+sql_columns+") values ("+sql_values+");\n"
        sql = sql.encode('utf-8')
        sys.stdout.write(sql)

    #print columns

for i in elements:
    #tables=dict()
    handle_element('',i)
    print '--Start--',i
#    generate_insert_statements(values)
    values=dict()
    print '--End--',i
    
    #values=dict()
print '--Start Create Tables-------------------------------------'
#print tables
generate_create_tables(tables)
print '--End Create Tables---------------------------------------'
#    print tables

    



