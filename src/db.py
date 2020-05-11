from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# your classes here
association_table = db.Table('association', db.Model.metadata,
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'))
)

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    cuisine = db.Column(db.String, nullable = False)
    price_level = db.Column(db.Integer, nullable = False)
    locations = db.relationship('Location', secondary = association_table, back_populates = 'restaurants')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', False)
        self.cuisine = kwargs.get('cuisine', False)
        self.price_level = kwargs.get('price_level')
        self.user_id = kwargs.get('user_id', False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'cuisine': self.cuisine,
            'price_level': self.price_level,
            'locations': [s.serialize() for s in self.locations],
        }

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String, nullable = False)
    state = db.Column(db.Integer, nullable = False)
    zipcode = db.Column(db.Integer, nullable = False)
    restaurants = db.relationship('Restaurant', secondary=association_table, back_populates='locations')

    def __init__(self, **kwargs):
        self.city = kwargs.get('city', False)
        self.state = kwargs.get('state', False)
        self.zipcode = kwargs.get('zipcode', False)

    def serialize(self):
        return {
        'id' : self.id,
        'city': self.city,
        'state': self.state,
        'zipcode': self.zipcode,
        'restaurants': []
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    restaurants = db.relationship('Restaurant', cascade = 'delete')

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name','')
        self.last_name = kwargs.get('last_name')

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'restaurants': [s.serialize() for s in self.restaurants],
        }
