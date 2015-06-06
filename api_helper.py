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
  cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
  print 'got cursor'
  cur.execute("select T.id, T.cust_id, C.name, C.mobile, T.prob_id, P.problem_type, T.status_id, S.status, T.comments, T.assigned_to from tickets T, customers C, problem_types P, status S where  T.cust_id = C.id and T.prob_id = P.id and T.status_id = S.id")
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