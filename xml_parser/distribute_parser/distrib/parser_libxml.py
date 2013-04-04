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

class ZakupkiXMLParser(object):
    def __init__(self):
        self.tables=dict()
        self.values=dict()
        self.uids=dict()
        self.sql_inserts=[]
        try: 
            uids_file = open('uids.pkl', 'rb')
            self.uids = pickle.load(uids_file)
            uids_file.close()
        except:
            pass
        '''
        if CREATE_TABLES==True:
            try:
                tables_file = open('tables.pkl','rb')
                tables=pickle.load(tables_file)
                tables_file.close()
            except:
                pass
        '''
        self.SCHEMA=schema
        self.PK=['uid']
        self.FK_IS=['uid']
        self.FK=['parent_uid']
        self.INTEGER=['month','year','id','versionNumber','kpp','countryCode']
        self.BIGINTEGER=['inn','regNum','uid','parent_uid']
        self.FLOAT=[]
        self.NUMERIC=['price','sum']#'quantity'] Fond that in contracts it can be text
        self.VARCHAR=['']
        self.UNQUOTED=['parent_uid']
        # If need modify column names in output or modify tablenames in output

        self.COLUMN_MAPPING={
        'placing':'pplacing',
        'order':'"order"',
        'from':'"from"',
        }

        self.TABLES_MAPPING={
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
        '-':'',
        '\.':'',
        }


    def uniq(self,seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if x not in seen and not seen_add(x)]

    def remapColumns(self,columns):
        result=[]
        for i in columns:
            if i in self.COLUMN_MAPPING.keys():
                result.append(self.COLUMN_MAPPING[i])
            else:
                result.append(i)
        return result

    def remapTable(self,table):
        warning=''
        result=''
        wrong_simbols=['-','.']
        for i in self.TABLES_MAPPING.keys():    
            table = re.sub(i, self.TABLES_MAPPING[i], table)
        result=table
        if len(result)>63:
            warning += '--Warning table name too long:' + table + ':'+table[0:63]+'\n'
        if any(s in result for s in wrong_simbols):
            warning += '--Warning wrong simbol in table name:' + result + '\n'
        if len(warning)>0:
            pass
            #sys.stderr.write('\033[93m'+warning+'\033[0m')
        if len(result)>0:
            return result
        else:
            return table



    def handle_element(self,parent,elem):
        #print parent,elem
        if len(elem.xpath("./*"))>0:
            key=parent+'_'+(elem.xpath("local-name()"))
            key=self.remapTable(key)
            if key not in self.tables.keys():
                self.tables[key]=[]
                #tables[parent+'_'+(elem.xpath("local-name()"))]=[]
            if key not in self.values.keys():
                self.values[key]=[]
                #values[parent+'_'+(elem.xpath("local-name()"))]=[]
            #next_element.append(elem)
        else:
            self.tables[parent]+=[elem.xpath("local-name()")]
            column_name=parent+'_'+elem.xpath("local-name()")
            if column_name not in self.values.keys():
                self.values[column_name]=[]
                self.values[column_name]+=[elem.xpath("text()")]
            else:
                self.values[column_name]+=[elem.xpath("text()")]
        for i in elem:
            el = self.remapTable(elem.xpath("local-name()"))
            par=parent+'_'+el
            #par=remapTable(par)
            self.handle_element(par,i)

    def generate_types(self,columns):
        result=[]
        for i in columns:
            if i in self.PK:
                result.append(i+' bigint primary key')
            elif i in self.INTEGER:
                result.append(i+' integer')
            elif i in self.BIGINTEGER:
                result.append(i+' bigint')
            elif i in self.VARCHAR:
                result.append(i+' varchar(2000)')
            elif i in self.FLOAT:
                result.append(i+' float')
            elif i in self.NUMERIC:
                result.append(i+' numeric')
            else:
                result.append(i+' text')
        return result

    def getParent(self,table):
        table_list=table.split('_')
        result=["_"]
        parent="_".join(table_list[0:-1])
        result+=parent
        result="".join(parent)
        return result

    def sortByHierarhy(self,tables_list):
        return tables_list.sort()

    def generate_create_tables(self,tables):
        for i in sorted(self.tables.keys()):
            columns=self.uniq(self.tables[i])
            columns.append(self.PK[0])

            columns=self.remapColumns(columns)
            columns=self.generate_types(columns)

            tab=self.remapTable(i)
            columns=",".join(columns)

            parent = self.getParent(i)
            parent = self.remapTable(parent)

            sql=''
            schema=''

            if len(self.SCHEMA)>0:
                schema=self.SCHEMA+'.'
                if len(parent)==0:
                    sql="create table "+schema + tab +" ("+columns+");"
                else:
                    sql="create table "+schema + tab +" ("+columns+", parent_uid bigint references "+parent+"("+self.FK_IS[0]+")"+" );\n"
                sys.stdout.write(sql)

    def extract_column_for_table(self,table,columns):
        result=[]
        for i in columns:
            prefix = i.split(table)
            if len(prefix)>1 and i not in self.tables.keys():
                if i.split(table)[1][0]=='_' and len(i.split(table)[1].split('_'))-1==1:
                    result+=[i]
        return result

    def extract_column_names(self,raw):
        result=[]
        for i in raw:
            tab = self.getParent(i)
            tmp=i.split(tab)
            result.append(tmp[-1][1:])
        return result

    def print_insert_statements(self,table,columns,values):
        tab=table
        col_names=columns
        curr_val=values
        fields_dict = dict(zip(col_names, curr_val))
        for field in fields_dict.keys():
            if field not in self.NUMERIC or self.INTEGER or self.BIGINTEGER or self.UNQUOTED:
                field_value="".join(fields_dict[field])
                if (field_value != 'NULL') and (field not in self.UNQUOTED):
                    field_value=field_value.replace('\'','\'\'')
                    fields_dict[field]='\''+field_value+'\''
        sql_columns= ",".join(fields_dict.keys())
        sql_values= ",".join(fields_dict.values())
        schema=''
        if len(self.SCHEMA)>0:
            schema=self.SCHEMA+'.'
        sql = 'insert into '+ schema + tab +" ("+sql_columns+") values ("+sql_values+");\n"
        sql = sql.encode('utf-8')
        sys.stdout.write(sql)


    def generate_uids(self,tab):
        uid=1
        parent_uid=None
        if len(self.getParent(tab))>0:
            if tab in self.uids.keys():
                self.uids[tab]+=1
                uid=self.uids[tab]
                parent_uid=self.uids[self.getParent(tab)]
            else:
                self.uids[tab]=1
                parent_uid=self.uids[self.getParent(tab)]
        else:
            if tab in self.uids.keys():
                self.uids[tab]+=1
                uid=self.uids[tab]
            else:
                self.uids[tab]=1
        return uid,parent_uid

    def generate_uids_seq(self,tab):
        parent_uid=None
        if len(self.getParent(tab))>0:
            parent_uid="currval(pg_get_serial_sequence('%s', 'uid'))"%(self.getParent(tab),)
        return parent_uid

    def generate_insert(self,tab,col_names,val):
        curr_val=[]
        for i in val:
            if i:
                curr_val.append(i.pop())
            else:
                curr_val.append('NULL')

        parent_uid=self.generate_uids_seq(tab)

        if parent_uid != None:
            if 'parent_uid' not in col_names:
                col_names.append('parent_uid')
                curr_val.append(str(parent_uid))
            else:
                curr_val.append(str(parent_uid))
        else:
            col_names.append('file_id')
            curr_val.append(str(self.file_id))

        col_names=self.remapColumns(col_names)      # do remap of Columns
        tab = self.remapTable(tab)                 # do remap of Tables
        self.print_insert_statements(tab,col_names,curr_val)


    def generate_insert_statements(self,columns_data):
        tabs=sorted(self.tables.keys())
        columns=sorted(columns_data)
        for tab in tabs:
            col = self.extract_column_for_table(tab,columns) #Get what is columns not nested tables
            col_names = self.extract_column_names(col)   #Get names of this cloumns
            val =[]
            for i in col:
                val.append(columns_data[i])     #Fetch data for columns           
            max_list = [len(j)  for j in val]
            if len(max_list)>1:
                #print max_list
                for i in range(max(max_list)):
                    self.generate_insert(tab,col_names,val)
            else:
                self.generate_insert(tab,col_names,val)


    def save_uids(self):
        output = open('uids.pkl', 'wb')
        pickle.dump(self.uids, output)
        output.close()

#parser = ZakupkiXMLParser()
'''
tree = etree.parse(xml_file)
root = tree.xpath(".")
elements=root[0].xpath("./*")

parser=ZakupkiXMLParser()

for i in elements:
    parser.handle_element('',i)
    if  CREATE_INSERTS:
        print '--Start--',i
        parser.generate_insert_statements(parser.values)
        print '--End--',i
    parser.values=dict()
    
'''

'''
if CREATE_TABLES:
    print '--Start Create Tables-------------------------------------'
    parser.generate_create_tables(parser.tables)
    output = open('tables.pkl', 'wb')
    #pickle.dump(tables, output)
    output.close()
    print '--End Create Tables---------------------------------------'

####### Storing all
'''

