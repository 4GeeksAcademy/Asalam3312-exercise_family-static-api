"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    
    return jsonify(members), 200


@app.route('/member/<int:member_id>', methods=['GET'])  # se crea la ruta para un solo miembro con un id flexible
def one_member(member_id):      # se crea la función 
    one = jackson_family.get_member(member_id)      # se crea la variable que contendra la informacion de la class.funcion(con el self (en este caso es member)_id )
    if not one:     # se crea condicional que verifique si la informacion se recibio correctamente
        return jsonify({"msg": "we couldn't find that member"}), 400    # si no
    return jsonify(one), 200        # si sí 

@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.json

    jackson_family.add_member(new_member)  # esto trae la información de la class.función y a esta función se le manda el valor deseado, el cual será poseriormente el name.
    return jsonify({"done": "user created"})

@app.route('/member/<int:member_id>', methods=['DELETE'])  # dentro del path se ingresa una url dinamica, la cual va a cambiar en función especifica del id unico de cada member
def delete_one_member(member_id):
    
    deleting_member = jackson_family.delete_member(member_id)
    if not deleting_member:
        return jsonify({"msg": "unespected value"}), 400
    return jsonify({'done': "member has been deleted successfully"}), 200

@app.route('/member/<int:member_id>', methods=['PUT'])
def update_family_member(member_id):
    
    new_member = request.json       # ya que lo que realiza la función update_member es borrar el miembro anterior y crear uno nuevo con la nueva información, es necesario hacer uso del new_member = request.json que está en el post

    updated_member = jackson_family.update_member(member_id, new_member)
    if not updated_member:
        return jsonify({"msg": "that user doesn't exist"}), 400
    return jsonify({"done": "member updated successfully"}), 200

   
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
