#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import codecs, sys
import sys, getopt, os.path
import pickle
import re
import collections

xml_file=''
schema=""

CREATE_TABLES=False
CREATE_INSERTS=False

try:
    opts, args = getopt.getopt(sys.argv[1:], "ci", ["help", "output=","stdin","file=","schema="])
except getopt.GetoptError as err:
        # print help information and exit:
    print str(err) # will print something like "option -a not recognized"
    sys.exit(2)
output = None
verbose = False
for o, a in opts:
    if o == "-v":
        verbose = True
    elif o in ("-c",):
        CREATE_TABLES=True
    elif o in ("-i",):
        CREATE_INSERTS=True
    elif o in ("--stdin"):
        xml_file=sys.stdin
    elif o in ("--file"):
        xml_file=a
    elif o in ("--schema"):
        schema=a
    else:
        assert False, "unhandled option"

tree = etree.parse(xml_file)
root = tree.xpath(".")
elements=root[0].xpath("./*")


tables=dict()
values=dict()
uids=dict()
try: 
    uids_file = open('uids.pkl', 'rb')
    uids = pickle.load(uids_file)
    uids_file.close()
    
except:
    pass
if CREATE_TABLES==True:
    try:
        tables_file = open('tables.pkl','rb')
        tables=pickle.load(tables_file)
        tables_file.close()
    except:
        pass

SCHEMA=schema

PK=['uid']
FK_IS=['uid']
FK=['parent_uid']
INTEGER=['month','year','id','versionNumber','kpp','countryCode']
BIGINTEGER=['inn','regNum','uid','parent_uid']
FLOAT=[]
NUMERIC=['price','sum']#'quantity'] Fond that in contracts it can be text
VARCHAR=['']

# If need modify column names in output or modify tablenames in output

COLUMN_MAPPING={
'placing':'pplacing',
'order':'"order"',
'from':'"from"',
}

TABLES_MAPPING={
'protocol[A-Z]{2,}[0-9]|prot[A-Z]{2,}[0-9]':'prtk',
'protocol':'prot',
#'_protocolLot':'_iprotLot',
'application':'app',
'admission':'adm',
'Result':'Res',
'Commission':'Com',
'Member':'Mem',
'Rejected':'Rej',
'Reason':'Reas',
'Participant':'Part',
'Condition':'Cond',
'evaluation':'ev',
'requirement':'req',
'Requirement':'Req',
'Compliance':'Comp',
'attributes':'attr',
'contract':'contr',
'criterion':'crit',
#'protocol':'prot',
'notification[A-Z]{2,}[0-9]?':'notf',
'notification':'notif',
'Feature':'Feat',
'-':'_',
'\.':'_',
}

STABLES_MAPPING={
#FOR NOTIFICATIONS:
'_notificationOK_lots_lot_customerRequirements_customerRequirement':'_notificationOK_lots_lot_custReqs_custReq',
'_notificationOK_lots_lot_customerRequirements_customerRequirement_customer':'_notificationOK_lots_lot_custReqs_custReq_cust',
'_notificationOK_lots_lot_customerRequirements_customerRequirement_guaranteeApp':'_notificationOK_lots_lot_custReqs_custReq_guaranteeApp',
'_notificationOK_lots_lot_customerRequirements_customerRequirement_guaranteeContract':'_notificationOK_lots_lot_custReqs_custReq_guaranteeContract',
'_notificationOK_lots_lot_customerRequirements_customerRequirement_KBK':'_notificationOK_lots_lot_custReqs_custReq_KBK',
'_notificationOK_lots_lot_notificationFeatures_notificationFeature':'_notificationOK_lots_lot_notifFeat',
'_notificationOK_lots_lot_notificationFeatures_notificationFeature_placementFeature':'_notificationOK_lots_lot_notifFeat_placementFeature',
'_notificationOK_competitiveDocumentProvisioning_guarantee_currency':'_notificationOK_competitiveDocProvis_guarantee_cur',
'_notificationOK_lots_lot_notificationFeatures_notificationFeature':'_notificationOK_lots_lot_notifFeat',
'_notificationOK_lots_lot_notificationFeatures_notificationFeature_placementFeature':'_notificationOK_lots_lot_notifFeat_placementFeature',
'_notificationOK_notificationPlacement_notificationFeatures_notificationFeature':'_notificationOK_notifPlacement_notifFeats_notifFeat',
'_notificationOK_notificationPlacement_notificationFeatures_notificationFeature_placementFeature':'_notificationOK_notifPlacement_notifFeats_notiiFeat_placemFeat',
'_notificationZK_lots_lot_customerRequirements_customerRequirement':'_notificationZK_lots_lot_custReqs_custReq',
'_notificationZK_lots_lot_customerRequirements_customerRequirement_customer':'_notificationZK_lots_lot_custReqs_custReq_cust',
'_notificationZK_lots_lot_notificationFeatures_notificationFeature':'_notificationZK_lots_lot_notifFeats_notifFeat',
'_notificationZK_lots_lot_notificationFeatures_notificationFeature_placementFeature':'_notificationZK_lots_lot_notifFeats_notifFeat_placementFeat',
'_notificationZK_lots_lot_customerRequirements_customerRequirement_KBK':'_notificationZK_lots_lot_custReqs_custReq_KBK',
'_notificationZK_lots_lot_customerRequirements_customerRequirement_guaranteeContract':'_notificationZK_lots_lot_custReqs_custReq_guaranteeContract',


'_notificationEF_lots_lot_auctionProducts_auctionProduct_equivalenceParam':'_notificationEF_lots_lot_auctionProducts_auctionProduct_equival',
'_notificationEF_lots_lot_auctionProducts_auctionProduct_productRequirement':'_notificationEF_lots_lot_auctionProducts_auctionProduct_product',
'_notificationEF_lots_lot_customerRequirements_customerRequirement':'_notificationEF_lots_lot_custReqs_custReq',
'_notificationEF_lots_lot_customerRequirements_customerRequirement_customer':'_notificationEF_lots_lot_custReqs_custReq_cust',
'_notificationEF_lots_lot_customerRequirements_customerRequirement_guaranteeApp':'_notificationEF_lots_lot_custReqs_guaranteeApp',
'_notificationEF_lots_lot_customerRequirements_customerRequirement_guaranteeContract':'_notificationEF_lots_lot_custReqs_custReq_guaranteeContract',
'_notificationEF_lots_lot_documentRequirements_documentRequirement':'_notificationEF_lots_lot_docReqs_docReq',
'_notificationEF_lots_lot_lotDocRequirements_docReq-1.1.11':'_notificationEF_lots_lot_lotDocReqs_docReq_1_1_11',
'_notificationEF_lots_lot_lotDocRequirements_docReq-1.1.11_documentRequirement':'_notificationEF_lots_lot_lotDocReqs_docReq_1_1_11_docReq',
'_notificationEF_lots_lot_lotDocRequirements_docReq-1.2.11':'_notificationEF_lots_lot_lotDocReqs_docReq_1_2_11',
'_notificationEF_lots_lot_lotDocRequirements_docReq-1.2.11_documentRequirement':'_notificationEF_lots_lot_lotDocReqs_docReq_1_2_11_docReq',
'_notificationEF_lots_lot_lotDocRequirements_docReq-2.1.11':'_notificationEF_lots_lot_lotDocReqs_docReq_2_1_11',
'_notificationEF_lots_lot_lotDocRequirements_docReq-2.1.11_documentRequirement':'_notificationEF_lots_lot_lotDocReqs_docReq_2_1_11_docReq',
'_notificationEF_lots_lot_notificationFeatures_notificationFeature':'_notificationEF_lots_lot_notifFeat',
'_notificationEF_lots_lot_notificationFeatures_notificationFeature_placementFeature':'_notificationEF_lots_lot_notifFeat_placementFeature',

'_notificationPO_lots_lot_customerRequirements_customerRequirement':'_notificationPO_lots_lot_custReqs_custReq',
'_notificationPO_lots_lot_customerRequirements_customerRequirement_customer':'_notificationPO_lots_lot_custReqs_custReq_cust',
'_notificationPO_lots_lot_customerRequirements_customerRequirement_guaranteeApp':'_notificationPO_lots_lot_custReqs_custReq_guaranteeApp',
'_notificationPO_lots_lot_customerRequirements_customerRequirement_guaranteeContract':'_notificationPO_lots_lot_custReqs_custReq_guaranteeContract',

'_notificationSZ_lots_lot_customerRequirements_customerRequirement':'_notificationSZ_lots_lot_custReqs_custReq',
'_notificationSZ_lots_lot_customerRequirements_customerRequirement_customer':'_notificationSZ_lots_lot_custReqs_custReq_cust',


}

def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def remapColumns(columns):
    result=[]
    for i in columns:
        if i in COLUMN_MAPPING.keys():
            result.append(COLUMN_MAPPING[i])
        else:
            result.append(i)
    return result

def remapTable(table):
    warning=''
    result=''
    wrong_simbols=['-','.']
    #if table in TABLES_MAPPING.keys():
#    print 'Start:'
    for i in TABLES_MAPPING.keys():	
        #result = TABLES_MAPPING[table]
#	print i
        table = re.sub(i, TABLES_MAPPING[i], table)
    #    print result
    result =table
    if len(result)>63:
        warning += '--Warning table name too long:' + table + ':'+table[0:63]+'\n'
    if any(s in result for s in wrong_simbols):
        warning += '--Warning wrong simbol in table name:' + result + '\n'
    if len(warning)>0:
        sys.stderr.write('\033[93m'+warning+'\033[0m')
    if len(result)>0:
        return result
    else:
        return table



def handle_element(parent,elem):
    #print parent,elem
    if len(elem.xpath("./*"))>0:
        key=parent+'_'+(elem.xpath("local-name()"))
	key=remapTable(key)
        if key not in tables.keys():
            tables[key]=[]
            #tables[parent+'_'+(elem.xpath("local-name()"))]=[]
        if key not in values.keys():
            values[key]=[]
            #values[parent+'_'+(elem.xpath("local-name()"))]=[]
        #next_element.append(elem)
    else:
        tables[parent]+=[elem.xpath("local-name()")]
        column_name=parent+'_'+elem.xpath("local-name()")
        if column_name not in values.keys():
            values[column_name]=[]
            values[column_name]+=[elem.xpath("text()")]
        else:
            values[column_name]+=[elem.xpath("text()")]
    for i in elem:
        el = remapTable(elem.xpath("local-name()"))
        par=parent+'_'+el
        #par=remapTable(par)
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

        columns=remapColumns(columns)
        columns=generate_types(columns)

        tab=remapTable(i)
        columns=",".join(columns)

        parent = getParent(i)
        parent = remapTable(parent)

        sql=''
	schema=''

	if len(SCHEMA)>0:
		schema=SCHEMA+'.'
        if len(parent)==0:
            sql="create table "+schema + tab +" ("+columns+");"
        else:
            sql="create table "+schema + tab +" ("+columns+", parent_uid bigint references "+parent+"("+FK_IS[0]+")"+" );\n"
        sys.stdout.write(sql)
        


def extract_column_for_table(table,columns):
    
    result=[]
    #print 'Table:',table
    #print 'Columns:',columns
    #print tables.keys()
    for i in columns:
#	print i
        prefix = i.split(table)
 #       print prefix
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

def print_insert_statements(table,columns,values):
    tab=table
    col_names=columns
    curr_val=values
    fields_dict = dict(zip(col_names, curr_val))
    for field in fields_dict.keys():
        if field not in NUMERIC or INTEGER or BIGINTEGER:
            field_value="".join(fields_dict[field])
            field_value=field_value.replace('\'','\'\'')
            fields_dict[field]='\''+field_value+'\''
    sql_columns= ",".join(fields_dict.keys())
    sql_values= ",".join(fields_dict.values())


    schema=''
    if len(SCHEMA)>0:
        schema=SCHEMA+'.'

    sql = 'insert into '+ schema + tab +" ("+sql_columns+") values ("+sql_values+");\n"
    sql = sql.encode('utf-8')
    sys.stdout.write(sql)


def generate_uids(tab):
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
    else:
        if tab in uids.keys():
            uids[tab]+=1
            uid=uids[tab]
        else:
            uids[tab]=1
    return uid,parent_uid


def generate_insert(tab,col_names,val):
    curr_val=[]
    for i in val:
        if i:
            curr_val.append(i.pop())
        else:
            curr_val.append('None')

    uid,parent_uid=generate_uids(tab)

    if 'uid' not in col_names:
        col_names.append('uid')
        curr_val.append(str(uid))
    else:
        #print col_names,curr_val
        #print col_names.index('uid')
        #curr_val[col_names.index('uid')]=str(uid)
        curr_val.append(str(uid))
    if parent_uid != None:
        if 'parent_uid' not in col_names:
            col_names.append('parent_uid')
            curr_val.append(str(parent_uid))
        else:
            curr_val.append(str(parent_uid))
            #curr_val[col_names.find('parent_uid')]=str(uid)

    col_names=remapColumns(col_names)      # do remap of Columns
    tab = remapTable(tab)                 # do remap of Tables
    print_insert_statements(tab,col_names,curr_val)



def generate_insert_statements(columns_data):
    tabs=sorted(tables.keys())
    columns=sorted(columns_data)
    for tab in tabs:
        col = extract_column_for_table(tab,columns) #Get what is columns not nested tables
        col_names = extract_column_names(col)   #Get names of this cloumns
        val =[]
        for i in col:
            val.append(columns_data[i])     #Fetch data for columns
        
        
        #print tab,"Val:",valA
        #if type(val) is type([])A
        #print val
        max_list = [len(j)  for j in val]

        #if  all(isinstance(n, list) and len(n)>1  for n in val):
        if len(max_list)>1:
            #print max_list
            for i in range(max(max_list)):
                generate_insert(tab,col_names,val)
        else:
            generate_insert(tab,col_names,val)


for i in elements:
    #tables=dict()
    handle_element('',i)
    if  CREATE_INSERTS:
        print '--Start--',i
        generate_insert_statements(values)
        print '--End--',i
        output = open('uids.pkl', 'wb')
        pickle.dump(uids, output)
        output.close()
    values=dict()

if CREATE_TABLES:
    print '--Start Create Tables-------------------------------------'
    generate_create_tables(tables)
    output = open('tables.pkl', 'wb')
    pickle.dump(tables, output)
    output.close()
    print '--End Create Tables---------------------------------------'

####### Storing all




