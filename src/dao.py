from db import db, Restaurant, Location, User

def get_all_users():
    return [u.serialize() for u in User.query.all()]

def create_user(first_name,last_name):
    new_user = User(
        first_name = first_name,
        last_name = last_name
        )
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_user_by_id(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    db.session.commit()
    return user.serialize()

def update_user_by_id(user_id, body):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    user.first_name = body.get("first_name", user.first_name)
    user.last_name = body.get("last_name", user.last_name)
    db.session.commit()
    return user.serialize()

def delete_user_by_id(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return user.serialize()

def _get_or_create_restaurant(name, cuisine, price_level, user_id ):
    restaurant = Restaurant.query.filter_by(name = name).first()
    if restaurant is not None:
        return restaurant
    new_restaurant = Restaurant(
        name = name,
        cuisine = cuisine,
        price_level = price_level,
        user_id = user_id
    )
    db.session.add(new_restaurant)
    db.session.commit()
    return new_restaurant

def get_restaurants_by_user_id(user_id):
    user = User.query.filter_by (id = user_id).first()
    if user is None:
        return None
    return [s.serialize() for s in user.restaurants]

def get_user_restaurants_by_price_level(user_id, price_level):
    user = User.query.filter_by (id = user_id).first()
    if user is None:
        return None
    restaurants = []
    for s in user.restaurants:
        if s.price_level == price_level:
            restaurants.append(s)
    return [r.serialize() for r in restaurants]


def assign_restaurant_to_user(name, cuisine, price_level, user_id):
    user = User.query.filter_by (id = user_id).first()
    if user is None:
        return None
    restaurant = _get_or_create_restaurant(name, cuisine, price_level, user_id)
    user.restaurants.append(restaurant)
    db.session.commit()
    return user.serialize()

def get_all_locations():
    return [l.serialize() for l in Location.query.all()]

def _get_or_create_location(city, state, zipcode, restaurant_id ):
    location = Location.query.filter_by(zipcode = zipcode).first()
    if location is not None:
        return location
    new_location = Location(
        city = city,
        state = state,
        zipcode = zipcode,
        restaurant_id = restaurant_id
    )
    db.session.add(new_location)
    db.session.commit()
    return new_location

def get_location_by_id(location_id):
    location = Location.query.filter_by(id = location_id).first()
    if location is None:
        return None
    db.session.commit()
    location_json = location.serialize()
    restaurants = []
    for r in location.restaurants:
        restaurants.append(r.serialize())
    location_json['restaurants'] = restaurants
    return location_json

def add_location_to_restaurant(city, state, zipcode, restaurant_id):
    restaurant = Restaurant.query.filter_by(id = restaurant_id).first()
    if restaurant is None:
        return None
    location = _get_or_create_location(city, state, zipcode, restaurant_id)
    restaurant.locations.append(location)
    db.session.commit()
    return Restaurant.query.filter_by(id = restaurant_id).first().serialize()


