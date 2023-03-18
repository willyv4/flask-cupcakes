"""Flask app for Cupcakes"""

from models import db, connect_db, Cupcake
from flask import Flask, jsonify, request, render_template,  redirect, flash, session


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "petsarecool1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)


@app.route('/')
def home():
    cakes = Cupcake.query.all()

    return render_template('index.html', cakes=cakes)


@app.route('/api/cupcakes')
def get_cupcakes():
    all_cakes = [cake.serialize() for cake in Cupcake.query.all()]

    return jsonify(cupcakes=all_cakes)


@app.route('/api/cupcakes/<int:id>')
def get_a_capcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_a_cupcake():
    new_cake = Cupcake(flavor=request.json['flavor'], size=request.json['size'],
                       rating=request.json['rating'], image=request.json['image'])
    db.session.add(new_cake)
    db.session.commit()
    resp = jsonify(cupcake=new_cake.serialize())

    return (resp, 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()

    return jsonify(update_cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message=f"Cupcake {cupcake.id} Deleted Succesfully")
