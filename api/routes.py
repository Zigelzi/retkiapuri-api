from flask import make_response, jsonify, request
from api import app, db

# Status message descriptions
status_msg_fail = 'fail'
status_msg_success = 'success'

# Routes

@app.route('/api/ping')
def ping():
    response_object = {'status': status_msg_success }
    json_response = jsonify(response_object)
    return make_response(json_response, 200)