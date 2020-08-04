from api import db

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

class NationalPark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    routes = db.relationship('HikeRoute', backref='national_park', lazy=True)

    def save(self):
        db.session.add(self)
    
    def delete(self):
        db.session.delete(self)

    @staticmethod
    def get_all():
        return NationalPark.query.all()

    def __repr__(self):
        return f'<NationalPark {self.name} | Longitude {self.longitude} | Latitude {self.latitude}>'

class HikeRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Float(precision=2), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)

    national_park_id = db.Column(db.Integer, db.ForeignKey('national_park.id'))

    def save(self):
        db.session.add(self)
    
    def delete(self):
        db.session.delete(self)

    @staticmethod
    def get_all():
        return HikeRoute.query.all()

    def __repr__(self):
        return f'<HikeRoute {self.name} | Length {self.length}>'

# ---------------------------------
# Marshmallow serialization schemas
# ---------------------------------
class HikeRouteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HikeRoute
        include_fk = True
        sqla_session = db.session
        load_instance = True

class NationalParkSchema(SQLAlchemyAutoSchema):
    hike_routes = Nested(HikeRouteSchema, many=True)
    class Meta:
        model = NationalPark
        include_fk = True
        load_instance = True
        sqla_session = db.session