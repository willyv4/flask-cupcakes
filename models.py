"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
from traitlets import default

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()


class Cupcake(db.Model):
    """ Cupcake database model """

    __tablename__ = "cupcake"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    image = db.Column(db.String(), nullable=False,
                      default='https://tinyurl.com/demo-cupcake')

    def serialize(self):
        """Returns a dict representation of cakes which we can turn into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
