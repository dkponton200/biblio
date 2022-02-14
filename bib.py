from pickle import BINBYTES
from flask import Flask, jsonify, request, url_for,abort
from flask_sqlalchemy import SQLAlchemy

bib = Flask(__name__)   
bib.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Password@localhost:5432/projet'
bib.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(bib)

class Livre(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), nullable=False, unique=True)
    titre = db.Column(db.String(50), nullable=False)
    date_publication = db.Column(db.DateTime, nullable=True)
    auteur = db.Column(db.String(30), nullable=False)
    editeur = db.Column(db.String(30), nullable=False)
    categories_id=db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    
    def __init__(self, isbn, titre, date_publication, auteur, editeur, categories_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categories_id=categories_id
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id':self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date publication': self.date_publication,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'categories id': self.categories_id,
        }

class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(20), nullable=False)
    livres=db.relationship('Livre', backref='categories', lazy=True)
    
    def __init__(self, id, libelle):
        self.id=id
        self.libelle=libelle
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'libelle': self.libelle,
        }
        
db.create_all()

    
@bib.route('/livres')
def tous_les_livres():
    livres=Livre.query.all()
    livres=[l.format() for l in livres]
    return jsonify(livres)

@bib.route('/livres/<int:id>')
def livres_id(id):
    livres = Livre.query.get(id)
    if livres is None:
        return "Aucun livre enregistré a ce id"
    else:
        return livres.format()

@bib.route('/categories/<int:id>/livres')
def Livres_categories(id):
    try:
        categories = Categorie.query.get(id)
        livres = Livre.query.filter_by(categories_id=id).all()
        livres = [l.format() for l in livres]
        return jsonify({
            'Success': True,
            'total': len(livres),
            'categorie': categories.format(),
            'livres': livres
                        })
    except:
        return "Aucun livre dans cette categorie"
    finally:
        db.session.close()



@bib.route('/categories/<int:id>')
def avoir_categories_id(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        return "Aucune categorie enregistré a cet Id"
    else:
        return categorie.format()


@bib.route('/categories')
def toutes_les_categories():
    categories=Categorie.query.all()
    categories=[l.format() for l in categories]
    return jsonify(categories)

@bib.route('/livres/<int:id>', methods=['DELETE'])
def sup_livres(id):
    try:
            livres = Livre.query.get(id)
            livres.delete()
            return jsonify({
            'suppression': True,
            'id_Livre': id,
            'total_restant': Livre.query.count()
            })
    except:
        return "suppression echouée"
    finally:
        db.session.close()


@bib.route('/categories/<int:id>', methods=['DELETE'])
def sup_categories(id):
    try:
        categories = Categorie.query.get(id)
        categories.delete()
        return jsonify({
            'suppresion': True,
            'id_cat': id,
            'total_restant': Categorie.query.count()
        })
    except:
        return "suppresion echouée"
    finally:
        db.session.close()


@bib.route('/livres/<int:id>', methods=['PATCH'])
def patcher_livres(id):
    body = request.get_json()
    livres = Livre.query.get(id)
    try:
        if 'titre' in body or 'isbn' in body or 'editeur' in body or 'editeur' in body:
            livres.titre = body['titre']
            livres.auteur = body['auteur']
            livres.editeur = body['editeur']
            livres.isbn = body['isbn']
        livres.update()
        return livres.format()
    except:
        return "modification echouée"


@bib.route('/categories/<int:id>', methods=['PATCH'])
def patcher_categorie(id):
    body = request.get_json()
    categories = Categorie.query.get(id)
    try:
        if 'libelle' in body:
            categories.libelle = body['libelle']
        categories.update()
        return categories.format()
    except:
        return "modification echouée"