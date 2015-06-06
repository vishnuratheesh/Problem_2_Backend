import psycopg2
import psycopg2.extras
from db_helper import getDBConnection, pgQuery, pgFetchOne,pgFetchAll
import arrow
import logging
import json

def getAllTicketDetails():
  print 'inside getAllTicketDetails'
  conn = getDBConnection()
  print 'got connection'
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
  print 'got cursor'
  cur.execute("select * from tickets")
  print 'command executed'
  results = cur.fetchall()
  cur.close()
  conn.close()
  if results:
    return results
  else:
    return None


def createTicket(cust_id,prob_id,status_id,comments):
  print 'inside createTicket'
  query = "INSERT INTO tickets (cust_id,prob_id,status_id,comments) values (%s, %s, %s, %s)"
  print "query: " + query
  data = (cust_id,prob_id,status_id,comments,)
  res = pgQuery(query,data)

  if res:
    return True
  else:
    return None