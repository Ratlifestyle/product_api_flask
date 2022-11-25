import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
CORS(app)
app.app_context().push()

#swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config= {
        'app_name': 'api_produits'
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
#end swagger configuration

engine_options = {
    'echo': True
}
db = SQLAlchemy(app, engine_options=engine_options)

from api_produits.models.Produit import Produit

db.create_all()
db.session.commit()
# db = SQLAlchemy(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

from api_produits.bluePrints.basic_endpoints.product_endpoints import productBluePrint

app.register_blueprint(productBluePrint)

import api_produits.errorsHandlers.ProductErrorsHandler