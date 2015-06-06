import psycopg2
import psycopg2.extras
from psycopg2.extras import Json
import os
import urlparse
#from config.appconfig import *

def getDBConnection ():
  print 'inside getDBConnection'
  urlparse.uses_netloc.append('postgres')
  #print os.environ["DATABASE_URL"]
  url = urlparse.urlparse(os.environ["DATABASE_URL"])
  print 'here'
  try:
    return psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
    )
  except Exception, e:
    print "Error: Failed PG Connection - Message: %s "%(e[0])
    return False

def pgQuery(query,data):
  try:
    conn = getDBConnection()
    cur = conn.cursor()
    #print cur.mogrify(query,data)
    cur.execute(query,data)
    conn.commit()
    cur.close()
    conn.close()
    return True
  except Exception, e:
    print "Error: Failed Query - Message: %s "%(e[0])
    return False

def pgFetchOne(query,data):
  try:
    conn = getDBConnection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    #print cur.mogrify(query,data)
    cur.execute(query,data)
    rec = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rec
  except Exception, e:
    print "Error: Failed Query - Message: %s "%(e[0])
    return False

def pgFetchAll(query,data):
  try:
    conn = getDBConnection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    if data:
      #print cur.mogrify(query,data)
      cur.execute(query,data)
    else:
      #print cur.mogrify(query)
      cur.execute(query)
    rec = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rec
  except Exception, e:
    print "Error: Failed Query - Message: %s "%(e[0])
    return False