from flask import Flask, request
from db import db
import json
import dao

app = Flask(__name__)
db_filename = "food.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps({"success":True, "data": data}),code

def failure_response(message, code=404):
    return json.dumps({"success":False, "error": message}),code

@app.route('/api/users/', methods = ['GET'])
def get_users():
    return success_response(dao.get_all_users())


@app.route('/api/users/', methods = ['POST'])
def create_user():
    body = json.loads(request.data)
    try:
        user = dao.create_user(
           first_name = body.get('first_name'),
           last_name = body.get('last_name')
        )
        return success_response(user, 201)
    except:
        return failure_response("User could not be created.")

@app.route('/api/users/<int:user_id>/', methods = ['GET'])
def get_user_by_id(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route('/api/users/<int:user_id>/', methods = ['POST'])
def update_user_by_id(user_id):
    body = json.loads(request.data)
    user = dao.update_user_by_id(user_id, body)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route('/api/users/<int:user_id>/', methods = ['DELETE'])
def delete_user_by_id(user_id):
    user = dao.delete_user_by_id(user_id)
    if user is None:
        return failure_response("User could not be found!")
    return success_response(user)

@app.route('/api/users/<int:user_id>/restaurants/', methods=['POST'])
def assign_restaurant_to_user(user_id):
    body = json.loads(request.data)
    user = dao.assign_restaurant_to_user(
        name = body.get('name'),
        cuisine = body.get('cuisine'),
        price_level = body.get('price_level'),
        user_id = user_id
    )
    if user is None:
        return failure_response("User could not be found!")
    return success_response(user, 201)

@app.route('/api/users/<int:user_id>/restaurants/', methods = ['GET'])
def get_restaurants_by_user_id(user_id):
    restaurants = dao.get_restaurants_by_user_id(user_id)
    if restaurants is None:
        return failure_response("User could not be found!")
    return success_response(restaurants,201)

@app.route('/api/users/<int:user_id>/restaurants/<int:price_level>/', methods = ['GET'])
def get_user_restaurants_by_price_level(user_id, price_level):
    restaurants = dao.get_user_restaurants_by_price_level(user_id, price_level)
    if restaurants is None:
        return failure_response("User not found!")
    return success_response(restaurants, 201)

@app.route('/api/locations/', methods=['GET'])
def get_all_locations():
    return success_response(dao.get_all_locations())

@app.route('/api/locations/<int:location_id>/', methods = ['GET'])
def get_location_by_id(location_id):
    location = dao.get_location_by_id(location_id)
    if location is None:
        return failure_response("Location not found!")
    return success_response(location)

@app.route('/api/locations/', methods=['POST'])
def add_location_to_restaurant():
    body = json.loads(request.data)
    location = dao.add_location_to_restaurant(
        city = body.get('city'),
        state = body.get('state'),
        zipcode = body.get('zipcode'),
        restaurant_id = body.get('restaurant_id')
    )
    if location is None:
        return failure_response("Restaurant could not be found!")
    return success_response(location, 201)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
