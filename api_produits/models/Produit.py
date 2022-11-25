from api_produits import db
from sqlalchemy import Column, Integer, Text

class Produit(db.Model):
    __tablename__ = 'produit'
    id = Column(Integer, primary_key=True)
    nom = Column(Text, nullable=False)
    stock = Column(Integer, nullable=False)

    def __init__(self, id, nom, stock):
        self.id = id
        self.nom = nom
        self.stock = stock
    
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.nom,
            "stock": self.stock
        }