from api import db

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class HikeRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    length = db.Column(db.Float(precision=2))

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
        sqla_session = db.session
        load_instance = True
