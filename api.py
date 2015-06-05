from flask import Flask
from api_helper import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Problem_2 Backend APIs'

@app.route('/v1/tickets',methods=['GET'])
def getAllTickets():
  recs = getAllTicketDetails()
  if recs:
    return jsonify(data=recs)
  else:
    return page_not_found('No Tickets Found')

#--- Error Code 
@app.errorhandler(404)
def page_not_found(error):
  if isinstance(error, basestring):
    return jsonify(status=error), 404
  else:
    return "not found",404

@app.errorhandler(400)
def missing_parameter(error):
  print error
  if isinstance(error, basestring):
    return jsonify(status=error), 400
  else:
    return "invalid request", 400 


if __name__ == '__main__':
    app.run()