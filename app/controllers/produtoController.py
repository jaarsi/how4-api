from flask import Blueprint, request, jsonify
from peewee_validates import ModelValidator
from playhouse.shortcuts import model_to_dict, dict_to_model
from ..models import Produto, DoesNotExist

router = Blueprint('produtos', __name__)

@router.route('/', methods=['GET'])
def list():    
    result = [ model_to_dict(p) for p in Produto.select() ]
    return jsonify(result), 200

@router.route('/', methods=['POST'])
def create():
    try:        
        p = dict_to_model(Produto, request.json)
        validator = ModelValidator(p)
        
        if (not validator.validate()):
            return jsonify(errors=validator.errors), 400
        
        p.save()
        return model_to_dict(p), 201
    except Exception as err:
        return str(err), 500    

@router.route('/<int:id>', methods=['GET'])
def read(id):
    try:
        return model_to_dict( Produto.get(Produto.idProduto == id) )
    except DoesNotExist:
        return '', 404
    except Exception as err:
        return str(err), 500

@router.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        p = Produto.get( Produto.idProduto == id )
        p.noProduto = request.json['noProduto']
        p.deProduto = request.json['deProduto']
        validator = ModelValidator(p)
        
        if (not validator.validate()):
            return jsonify(errors=validator.errors), 400

        p.save()
        return model_to_dict(p)
    except DoesNotExist:
        return '', 404
    except Exception as err:
        return str(err), 500

@router.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        Produto.get( Produto.idProduto == id ).delete_instance()
        return '', 200
    except DoesNotExist:
        return '', 404
    except Exception as err:
        return str(err), 500
