import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/sendMessage', methods=['GET'])
def home():
    if 'message' in request.args:
        returnMessage = "Server has recieved message: " +  request.args['message'] + " from client"
    else:
        returnMessage = "Server found no message"
    print returnMessage
    return returnMessage
app.run()