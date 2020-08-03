from flask import make_response, jsonify, request
from api import app, db
import traceback

from api.models import HikeRoute, HikeRouteSchema

# Schemas for serialisation
hike_route_schema = HikeRouteSchema()
many_hike_routes_schema = HikeRouteSchema(many=True)

# Status message descriptions
status_msg_fail = 'fail'
status_msg_success = 'success'

# Routes

@app.route('/api/hike_route', methods=['POST'])
def add_hike_route():
    try:
        response_object = {'status': status_msg_success }
        request_data = request.get_json()
        hike_route = hike_route_schema.load(request_data)
        if hike_route:
            hike_route.save()
            db.session.commit()
            response_object['hike_route'] = hike_route_schema.dump(hike_route)
            response_object['message'] = 'Hike route added successfully!'
            json_response = jsonify(response_object)
            return make_response(json_response, 200)
        else:
            response_object['status'] = status_msg_fail
            response_object['message'] = 'Request contains incorrect data, check response.'
    except Exception as e:
        traceback.print_exc()
        response_object['status'] = status_msg_fail
        response_object['message'] = 'Something went wrong when trying to add hike route'
        db.session.rollback()
        json_response = jsonify(response_object)
        return make_response(json_response, 400)

@app.route('/api/hike_route/<int:hike_route_id>', methods=['GET'])
def get_hike_route(hike_route_id):
    response_object = {'status': status_msg_success }
    try:
        hike_route = HikeRoute.query.get(hike_route_id)
        if hike_route:
            hike_route_object = hike_route_schema.dump(hike_route)
            response_object['hike_route'] = hike_route_object
            response_object['message'] = 'Hike route queried successfully!'
            json_response = jsonify(response_object)
            return make_response(json_response, 200)
        elif task == None:
            response_object['status'] = status_msg_fail
            response_object['message'] = 'Queried hike route was not found'
            json_response = jsonify(response_object)
            return make_response(json_response, 404)
    except Exception as e:
        traceback.print_exc()
        response_object['status'] = status_msg_fail
        response_object['message'] = 'Something went wrong when trying to fetch hike route'
        json_response = jsonify(response_object)
        return make_response(json_response, 400)

@app.route('/api/hike_routes', methods=['GET'])
def get_all_hike_routes():
    response_object = {'status': status_msg_success }
    try:
        hike_routes = HikeRoute.query.all()
        hike_routes_object = many_hike_routes_schema.dump(hike_routes)
        response_object['hike_routes'] = hike_routes_object
        response_object['message'] = 'Hike routes queried successfully!'
        json_response = jsonify(response_object)
        return make_response(json_response, 200)
    except Exception as e:
        traceback.print_exc()
        response_object['status'] = status_msg_fail
        response_object['message'] = 'Something went wrong while querying for all hike routes'
        json_response = jsonify(response_object)
        return make_response(json_response, 400)