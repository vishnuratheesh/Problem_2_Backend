from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Problem_2 Backend APIs'

@app.route('/tickets',methods=['GET'])
def getAllTickets():
  recs = getAllTicketDetails(g.user_id)
  if recs:
    return jsonify(data=recs)
  else:
    return page_not_found('User Not Found')


if __name__ == '__main__':
    app.run()