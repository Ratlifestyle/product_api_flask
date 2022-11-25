from flask import Blueprint, jsonify, request, json, make_response
from api_produits import db
from api_produits.models.Produit import Produit
from api_produits.exceptions.ProductExceptions import ExistingProductException
from api_produits.exceptions.BadRequestException import BadRequestException
from api_produits.exceptions.ProductExceptions import NonExistingProductException


productBluePrint = Blueprint('ProductBlueprint', __name__)


@productBluePrint.route('/product', methods=['GET'])
def getProducts():
    products = Produit.query.all()
    return jsonify(result=[product.to_dict() for product in products]), 200


@productBluePrint.route('/product', methods=['POST'])
def createProduct():
    request_data = json.loads(request.get_data())
    if 'id' in request_data and 'nom' in request_data and 'stock' in request_data:
        product = Produit.query.get(request_data['id'])
        if not product:
            try:
                id = request_data['id']
                name = request_data['nom']
                stock = request_data['stock']
                product = Produit(id, name, stock)
                db.session.add(product)
                db.session.commit()
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered',
                    'status_code': '201',
                }
                return make_response(jsonify(responseObject)), 201
            except Exception:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occured . Please try again',
                    'status_code': '500',
                }
                return make_response(jsonify(responseObject)), 500
        else:
            raise ExistingProductException()
    else:
        raise BadRequestException()


@productBluePrint.route('/product/<id>', methods=['GET'])
def getProduct(id):
    product = Produit.query.get(id)
    if product:
        return make_response(jsonify(product.to_dict())), 200
    else:
        raise NonExistingProductException()


@productBluePrint.route('/product/<id>', methods=['PUT', 'PATCH'])
def replaceProduct(id):
    product = Produit.query.get(id)
    request_data = json.loads(request.get_data())
    if product:
        try:
            product.nom = request_data['nom']
            product.stock = request_data['stock']
            db.session.commit()
            responseObject = {
                'status': 'success',
                'message': 'Successfully modified',
                'status_code': '201',
            }
            return make_response(jsonify(responseObject)), 201
        except Exception:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occured . Please try again',
                'status_code': '500',
            }
            return make_response(jsonify(responseObject)), 500
    else:
        raise NonExistingProductException()


@productBluePrint.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Produit.query.filter_by(id=id).delete()
    db.session.commit()
    if product:
        responseObject = {
            'status': 'success',
            'message': 'Successfully deleted',
            'status_code': '200',
        }
        return make_response(jsonify(responseObject)), 200
    else:
        raise NonExistingProductException()
