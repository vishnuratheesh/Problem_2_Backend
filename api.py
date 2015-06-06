from flask import Flask, jsonify, request, json
from werkzeug.datastructures import MultiDict
from flask.ext.cors import CORS
from api_helper import *

app = Flask(__name__)
cors = CORS(app)

# One of the simplest configurations. Exposes all resources matching /api/* to
# CORS and allows the Content-Type header, which is necessary to POST JSON
# cross origin.
CORS(app, resources=r'/api/*', allow_headers='Content-Type')



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
  if request.headers['Content-Type'] == 'application/json':
    print "JSON Message: " + json.dumps(request.json)
    data = request.get_json(force=True)
    print data
    print data['cust_id']
    print data['prob_id']
    print data['status_id']
    print data['comments']

    cust_id = data['cust_id']
    prob_id =  data['prob_id']
    status_id = data['status_id']
    comments = data['comments']
     
    createTicket(cust_id,prob_id,status_id,comments)

    return jsonify(status='New Ticket Created'), 200
  else:
    return jsonify(status='Unsupported Content-Type'), 404

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