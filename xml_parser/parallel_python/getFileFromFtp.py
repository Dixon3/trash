#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib 
import StringIO
import zipfile
import parser_libxml
import lxml
#from helper import DBConnector
import psycopg2
import datetime

import sys,os,traceback

from helper import DBConnector 

def get_zip_data(filename,callback):
        ftp = ftplib.FTP("ftp.zakupki.gov.ru", "free", "free")
        file = ftp.retrbinary("RETR " +filename, lambda data: callback(data))
        return file      
    

def parse_file_id(file_id,filename):
    zipdata = StringIO.StringIO()
    get_zip_data(filename,zipdata.write)
    try:
        myzipfile = zipfile.ZipFile(zipdata)
    except:
        'Not zip file:' + filename
        return
    finally:
        for name in myzipfile.namelist():
            print "Start work!"
            content=myzipfile.open(name)
            tree = lxml.etree.parse(content)
            root = tree.xpath(".")
            elements=root[0].xpath("./*")
            parser=parser_libxml.ZakupkiXMLParser()
            parser.file_id=str(file_id)
            parser.writeToConsole()
            parser.writeToDb()
            #parser.setDbConn(dbConn_string)
            data = []
            for i in elements:
                parser.handle_element('',i)
                #data+='--Start--',i
                #data+='BEGIN;'
                parser.generate_insert_statements(parser.values)
                #data+='commit;'
                #data+= '--End--',i
            #print data
            parser.save_uids()
            parser.values=dict()
    return

def main():
    
    db_connector = DBConnector('default')   
    curr=db_connector.getCursor()
    conn=db_connector.getConn()
    curr.execute("SELECT id,path FROM files_list where inserted=false and locked=false and pg_try_advisory_lock(tableoid::INTEGER,id) and path like '%contract%' limit 1")
    [(id,path)] = curr.fetchall()

    results=[]
    while id > 0:  
        try:
            dt = datetime.datetime.now()
            curr.execute("update files_list set locked=true ,lock_time=now() where id=%s",(id,))
            conn.commit()
            print "--Try get file" , id , path
            print "--RAISE warning 'Start to read file:%s:%s';" % (id,path)
            dt = datetime.datetime.now()
            parse_file_id(id,path)       
        except Exception as e:
            print "--Poblem!",e
            conn.rollback()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
            print(exc_type, fname, exc_tb.tb_lineno)
            traceback.print_exc()
        finally:
            curr.execute("update files_list set locked=false,inserted=true,insert_time=now() where id=%s; select pg_advisory_unlock(tableoid::INTEGER,id) from files_list where id = %s",(id,id))
            conn.commit()
            curr.execute("SELECT id,path FROM files_list where inserted=false and locked=false and pg_try_advisory_lock(tableoid::INTEGER,id) and path like '%contract%' limit 1")
            [(id,path)] = curr.fetchall()
    print "Seems, there is no more to insert."
    print results

if __name__ == "__main__":
    main()


