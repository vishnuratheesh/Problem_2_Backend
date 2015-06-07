from flask import Flask, jsonify, request, json
from werkzeug.datastructures import MultiDict
from flask.ext.cors import CORS
from api_helper import *

app = Flask(__name__)


# One of the simplest configurations. Exposes all resources matching /api/* to
# CORS and allows the Content-Type header, which is necessary to POST JSON
# cross origin.
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)



@app.route('/')
def hello_world():
    return 'Problem_2 Backend APIs'

@app.route('/v1/tickets',methods=['GET'])
def getAllTickets():
  print 'inside getAllTicketDetails - GET'
  recs = getAllTicketDetails()
  if recs:
    return jsonify(data=recs)
  else:
    return page_not_found('No Tickets Found')


@app.route('/v1/tickets',methods=['POST'])
def createNewTicket():
  print 'inside createNewTicket - POST'
  #print request
  #if request.headers['Content-Type'] == 'application/json':
  print "JSON Message: " + json.dumps(request.json)
  data = request.get_json(force=True)
  print data
  print data['cust_id']
  print data['prob_id']
  print data['comments']
  print data['assigned_to']

  cust_id = data['cust_id']
  prob_id =  data['prob_id']
  status_id = data['status_id']
  comments = data['comments']
  assigned_to = data['assigned_to']
   
  createTicket(cust_id,prob_id,status_id,comments,assigned_to)

  return jsonify(status='New Ticket Created'), 200
  # else:
  #   return jsonify(status='Unsupported Content-Type'), 404


@app.route('/v1/tickets/',methods=['PUT'])
def updateOneTicket():
  print 'inside updateOneTicket - PUT'
  #print request
  #if request.headers['Content-Type'] == 'application/json':
  print "JSON Message: " + json.dumps(request.json)
  data = request.get_json(force=True)
  print data
  print data['id']
  print data['cust_id']
  print data['prob_id']
  print data['status_id']
  print data['comments']
  print data['assigned_to']

  ticketID = data['id']
  cust_id = data['cust_id']
  prob_id =  data['prob_id']
  status_id = data['status_id']
  comments = data['comments']
  assigned_to = data['assigned_to']
   
  updateTicket(ticketID,cust_id,prob_id,status_id,comments,assigned_to)

  return jsonify(status='Ticket Updated'), 200
  #else:
    #return jsonify(status='Unsupported Content-Type'), 404

#curl -H "Content-type: aplication/json" -X PUT http://127.0.0.1:5000/v1/tickets/ -d '{"id":1, "cust_id": 1, "prob_id": 1, "status_id": 1, "comments": "AAAAAAA", "assigned_to": 1}'


@app.route('/v1/csrs',methods=['GET'])
def getAllCSRs():
  print 'inside getAllCSRs - GET'
  recs = getAllCSRDetails()
  if recs:
    return jsonify(data=recs)
  else:
    return page_not_found('No CSRs Found')


@app.route('/v1/status',methods=['GET'])
def getAllStatus():
  print 'inside getAllStatus - GET'
  recs = getAllStatusDetails()
  if recs:
    return jsonify(data=recs)
  else:
    return page_not_found('No CSRs Found')


@app.route('/v1/customers',methods=['GET'])
def getAllCustomers():
  print 'inside getAllCustomers - GET'
  recs = getAllCustomerDetails()
  if recs:
    return jsonify(data=recs)
  else:
    return page_not_found('No Customers Found')

@app.route('/v1/probtypes',methods=['GET'])
def getAllProblems():
  print 'inside getAllProblems - GET'
  recs = getAllProbTypes()
  if recs:
    return jsonify(data=recs)
  else:
    return page_not_found('No Problem Types Found')


#--- Error Code 
@app.errorhandler(404)
def page_not_found(error):
  print 'inside page_not_found'
  if isinstance(error, basestring):
    return jsonify(status=error), 404
  else:
    return "not found",404

@app.errorhandler(400)
def missing_parameter(error):
  print 'inside missing_parameter'
  print error
  if isinstance(error, basestring):
    return jsonify(status=error), 400
  else:
    return "invalid request", 400 


if __name__ == '__main__':
    app.run()