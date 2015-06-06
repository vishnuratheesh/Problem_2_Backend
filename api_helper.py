import psycopg2
import psycopg2.extras
from db_helper import getDBConnection, pgQuery, pgFetchOne,pgFetchAll
import arrow
import logging

def getAllTicketDetails():
  print 'inside getAllTicketDetails'
  conn = getDBConnection()
  print 'got connection'
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  print 'got connection'
  cur.execute("select * from tickets")
  print 'command executed'
  results = cur.fetchone()
  cur.close()
  conn.close()
  if results:
    return results
  else:
    return None