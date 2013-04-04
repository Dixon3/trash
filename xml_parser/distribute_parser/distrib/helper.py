
import psycopg2

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

