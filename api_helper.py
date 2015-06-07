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
  cur.execute("select T.id, T.cust_id, C.name, C.mobile, T.prob_id, P.problem_type, T.status_id, S.status, T.comments, T.assigned_to, H.name as csr_name, H.level from tickets T, customers C, problem_types P, status S, csr H where  T.cust_id = C.id and T.prob_id = P.id and T.status_id = S.id and T.assigned_to = H.id")
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

def updateTicket(ticketID,cust_id,prob_id,status_id,comments,assigned_to):
  print 'inside updateTicket'
  query = "UPDATE tickets set cust_id=%s,prob_id=%s,status_id=%s,comments=%s, assigned_to=%s where id=%s"
  print "query: " + query
  data = (cust_id,prob_id,status_id,comments,assigned_to,ticketID)
  res = pgQuery(query,data)

  if res:
    return True
  else:
    return None

#curl -H "Content-type: aplication/json" -X PUT http://127.0.0.1:5000/v1/tickets/1 -d '{"cust_id": 1, "prob_id": 1, "status_id": , "comments": "AAAAAAA", "assigned_to": 3}'



def getAllCSRDetails():
  print 'inside getAllCSRDetails'
  conn = getDBConnection()
  print 'got connection'
  cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
  print 'got cursor'
  cur.execute("select *from csr")
  print 'command executed'
  results = cur.fetchall()
  cur.close()
  conn.close()
  if results:
    return results
  else:
    return None

def getAllStatusDetails():
  print 'inside getAllStatusDetails'
  conn = getDBConnection()
  print 'got connection'
  cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
  print 'got cursor'
  cur.execute("select *from status")
  print 'command executed'
  results = cur.fetchall()
  cur.close()
  conn.close()
  if results:
    return results
  else:
    return None

def getAllCustomerDetails():
  print 'inside getAllCustomerDetails'
  conn = getDBConnection()
  print 'got connection'
  cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
  print 'got cursor'
  cur.execute("select *from customers")
  print 'command executed'
  results = cur.fetchall()
  cur.close()
  conn.close()
  if results:
    return results
  else:
    return None

def getAllProbTypes():
  print 'inside getAllProbTypes'
  conn = getDBConnection()
  print 'got connection'
  cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
  print 'got cursor'
  cur.execute("select *from problem_types")
  print 'command executed'
  results = cur.fetchall()
  cur.close()
  conn.close()
  if results:
    return results
  else:
    return None