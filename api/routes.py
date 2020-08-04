from flask import make_response, jsonify, request
from api import app, db
import traceback

from api.models import NationalPark, NationalParkSchema, HikeRoute, HikeRouteSchema

# Schemas for serialisation
national_park_schema = NationalParkSchema()
many_national_parks_schema = NationalParkSchema(many=True)

hike_route_schema = HikeRouteSchema()
many_hike_routes_schema = HikeRouteSchema(many=True)

# Status message descriptions
status_msg_fail = 'fail'
status_msg_success = 'success'

# Routes

@app.route('/api/national_park', methods=['POST'])
def add_national_park():
    try:
        response_object = {'status': status_msg_success }
        request_data = request.get_json()
        national_park = national_park_schema.load(request_data)
        if national_park:
            national_park.save()
            db.session.commit()
            response_object['national_park'] = national_park_schema.dump(national_park)
            response_object['message'] = 'National park added successfully!'
            json_response = jsonify(response_object)
            return make_response(json_response, 200)
        else:
            response_object['status'] = status_msg_fail
            response_object['message'] = 'Request contains incorrect data, check response.'
    except Exception as e:
        traceback.print_exc()
        response_object['status'] = status_msg_fail
        response_object['message'] = 'Something went wrong when trying to add national park'
        db.session.rollback()
        json_response = jsonify(response_object)
        return make_response(json_response, 400)

@app.route('/api/national_park/<int:national_park_id>', methods=['GET'])
def get_national_park(national_park_id):
    response_object = {'status': status_msg_success }
    try:
        national_park = NationalPark.query.get(national_park_id)
        if national_park:
            national_park_object = national_park_schema.dump(national_park)
            response_object['national_park'] = national_park_object
            response_object['message'] = 'National park queried successfully!'
            json_response = jsonify(response_object)
            return make_response(json_response, 200)
        elif task == None:
            response_object['status'] = status_msg_fail
            response_object['message'] = 'Queried national park was not found'
            json_response = jsonify(response_object)
            return make_response(json_response, 404)
    except Exception as e:
        traceback.print_exc()
        response_object['status'] = status_msg_fail
        response_object['message'] = 'Something went wrong when trying to fetch national park'
        json_response = jsonify(response_object)
        return make_response(json_response, 400)

@app.route('/api/national_parks', methods=['GET'])
def get_all_national_parks():
    response_object = {'status': status_msg_success }
    try:
        national_parks = NationalPark.get_all()
        print(national_parks)
        national_parks_object = many_national_parks_schema.dump(national_parks)
        response_object['national_parks'] = national_parks_object
        response_object['message'] = 'National parks queried successfully!'
        json_response = jsonify(response_object)
        return make_response(json_response, 200)
    except Exception as e:
        traceback.print_exc()
        response_object['status'] = status_msg_fail
        response_object['message'] = 'Something went wrong while querying for all national parks'
        json_response = jsonify(response_object)
        return make_response(json_response, 400)

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
        hike_routes = HikeRoute.get_all()
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