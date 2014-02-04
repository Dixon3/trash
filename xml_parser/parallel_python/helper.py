import psycopg2
from settings import DATABASE

class DBConnector(object):

    def __init__ (self,db):
        self.dbname=''
        self.dbuser=''
        self.dbhost=''
        self.dbpass=''
        try:
            self.connstr="dbname='%s' user='%s' host='%s' password='%s'" % (DATABASE[db]["dbname"],DATABASE[db]["dbuser"],DATABASE[db]["dbhost"],DATABASE[db]["dbpass"])
            print "Connecting to database\n ->%s" % (self.connstr)
            self.conn=psycopg2.connect(self.connstr)
            self.curr=self.conn.cursor()
        except Exception,e:
            print e
    def getCursor (self):
        return self.curr
    def getConn(self):
        return self.conn
    def commit(self):
        try:
            self.conn.commit
        except Exception,e:
            print "Unable to commit",e
            raise

