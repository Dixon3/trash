
import ftplib
import psycopg2
import sys

class DBConnector(object): 
    def __init__ (self,dbname,dbuser,dbhost,dbpass):
        self.dbname=dbname
        self.dbuser=dbuser
        self.dbhost=dbhost
        self.dbpass=dbpass
        try:
            connstr="dbname='%s' user='%s' host='%s' password='%s'" % (dbname,dbuser,dbhost,dbpass)
            #print connstr
            self.conn=psycopg2.connect(connstr)
            self.curr=self.conn.cursor()
        except Exception,e:
            print "I am unable to connect to the database",e
    def getCursor (self):
        return self.curr

    def commit(self):
        try:
            self.conn.commit
        except Exception,e:
            print "Unable to commit",e
            raise

try:
    db_conn=DBConnector("zakupki","zakupki","localhost","zakupki")
    cur=db_conn.getCursor()
    cur.execute("CREATE TABLE files_list (id serial PRIMARY KEY, path varchar unique, insert_time timestamp);commit;")
    del db_conn 
except Exception,e:
    print "Unable create table:",e



db_conn=DBConnector("zakupki","zakupki","localhost","zakupki")
curr=db_conn.getCursor()

ftp = ftplib.FTP("ftp.zakupki.gov.ru")
ftp.login("free", "free")

files = []

def ftp_walk(ftp):    
    print 'Path:', ftp.pwd()
    dirs = ftp.nlst()
    for item in (path for path in dirs if path not in ('.', '..')):
        try:
            ftp.cwd(item)
            print 'Changed to', ftp.pwd()
            try:
                ftp_walk(ftp)
            finally:
                ftp.cwd('..')
        except Exception, e:
            path=ftp.pwd() + '/'+str(item)
            curr.execute("INSERT into files_list (path) values (%s)", (path,))
            curr.execute("commit;")

ftp_walk(ftp)





'''
try:
    files = ftp.nlst()
except ftplib.error_perm, resp:
    if str(resp) == "550 No files found":
        print "no files in this directory"
    else:
        raise

for f in files:
    print f
'''
