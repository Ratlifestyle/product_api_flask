import api_produits
from api_produits.exceptions.BadRequestException import BadRequestException
from api_produits.exceptions.ProductExceptions import ExistingProductException
from api_produits.exceptions.ProductExceptions import NonExistingProductException
from api_produits import app
from flask import make_response, jsonify


@app.errorhandler(BadRequestException)
def handle_exisitng_product(e):
    responseObject = {
        'status': 'failed',
        'message': e.message,
        'status_code': '409'
    }
    return make_response(jsonify(responseObject)), 409


app.register_error_handler(409, handle_exisitng_product)


@app.errorhandler(ExistingProductException)
def handle_exisitng_product(e):
    responseObject = {
        'status': 'failed',
        'message': e.message,
        'status_code': '401'
    }
    return make_response(jsonify(responseObject)), 401


app.register_error_handler(401, handle_exisitng_product)


@app.errorhandler(NonExistingProductException)
def handle_non_existent_product(e):
    responseObject = {
        'status': 'failed',
        'message': e.message,
        'status_code': '404'
    }
    return make_response(jsonify(responseObject)), 404
