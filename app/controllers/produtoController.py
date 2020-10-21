from flask import Blueprint, jsonify, request
from ..models import Produto

router = Blueprint('produtos')

@router.route('/', methods=['GET'])
def list():
    return jsonify(Produto.select())

@router.route('/', methods=['POST'])
def create():
    p = Produto()    
    p.noProduto = request.json['noProduto']
    p.deProduto = request.json['deProduto']
    p.save()
    return jsonify(p)

@router.route('/:id', methods=['GET'])
def read(id):
    pass

@router.route('/:id', methods=['PUT'])
def update():
    pass            

@router.route('/:id', methods=['DELETE'])
def delete():
    pass                