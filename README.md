# BIBLIOTHEQUE API VERSION 1

## Getting Started

### Installation des Dépendances

#### Python 3.10.0
#### pip 21.3.1 from C:\Users\hp\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)

#### Dépendances de PIP

Pour installer les dépendances, ouvrez le dossier `/Documentation` et exécuter la commande suivante:

```bash ou powershell ou cmd
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## GET/livres

    GENERAL:
        Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 
    
        
    EXEMPLE: curl http://localhost:5000/livres
```
        {
    "livres": [
           {
        "auteur": "JP",
        "categories id": 3,
        "date publication": "Sat, 01 Feb 2020 00:00:00 GMT",
        "editeur": "GRACIO",
        "id": 4,
        "isbn": "4R44",
        "titre": "AYZ DE YOPOUGON"
    },
    {
        "auteur": "Jonathan",
        "categories id": 7,
        "date publication": "Sat, 01 Feb 2020 06:40:23 GMT",
        "editeur": "moise",
        "id": 6,
        "isbn": "5R5T",
        "titre": "MON PERE MON CHOIX"
    },
    {
        "auteur": "JOJO",
        "categories id": 7,
        "date publication": "Sun, 14 Feb 2021 14:39:00 GMT",
        "editeur": "Vincent",
        "id": 7,
        "isbn": "8TRE",
        "titre": "L ENFANT NOIR"
    },
    {
        "auteur": "JIJI",
        "categories id": 3,
        "date publication": "Tue, 05 Mar 2019 12:00:00 GMT",
        "editeur": "RORO",
        "id": 8,
        "isbn": "6TRT",
        "titre": "LE VILLAGE ENCHANTEE"
    },
    {
        "auteur": "ROUSSEAU",
        "categories id": 8,
        "date publication": "Sat, 01 Aug 2020 00:00:00 GMT",
        "editeur": "MOI",
        "id": 9,
        "isbn": "7THC",
        "titre": "LE RENARD ET LE LIVRE"
    }
    ],
}
```

.##GET/livres(id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/livres/4
```
{
    "auteur": "JP",
    "categories id": 3,
    "date publication": "Sat, 01 Feb 2020 00:00:00 GMT",
    "editeur": "GRACIO",
    "id": 4,
    "isbn": "4R44",
    "titre": "AYZ DE YOPOUGON"
}
```


. ## DELETE/livres(id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur de suppression et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/livres/4
```
    {
    "id_Livre": 4,
    "suppression": true,
    "total_restant": 4
    }
```

. ##PATCH/livres(id)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, l'isbn et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH http://localhost:5000/livres/6 -H "Content-Type:application/json" -d '{"auteur": "Amos","editeur": "david","titre": "droit","isbn": "6RTR"}
  ```
  ```
    {
    "auteur": "Amos",
    "categories id": 7,
    "date publication": "Sat, 01 Feb 2020 06:40:23 GMT",
    "editeur": "david",
    "id": 6,
    "isbn": "6RTR",
    "titre": "droit"
    }
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres. 
    
        
    EXEMPLE: curl http://localhost:5000/categories

        {
    [
       {
        "id": 3,
        "libelle": "maths"
    },
    {
        "id": 6,
        "libelle": "informatique"
    },
    {
        "id": 1,
        "libelle": "chinois"
    },
    {
        "id": 4,
        "libelle": "philosophie"
    },
    {
        "id": 7,
        "libelle": "sorcellerie"
    },
    {
        "id": 8,
        "libelle": "religion"
    },
    {
        "id": 9,
        "libelle": "maintenance"
    }
    ],
}
```

.##GET/categories(id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/categories/4
```
    {
    "id": 4,
    "libelle": "arabe"
    }
```

. ## DELETE/categories(id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du suppression et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/categories/6
```
    {
    "id_cat": 6,
    "suppresion": true,
    "total_restant": 6
    }
```

. ##PATCH/categories(id)
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'http://localhost:5000/categories/4' -H "Content-Type:application/json" -d '{"categorie": "arabe"}'
  ```
  ```
    {
    "id": 4,
    "libelle": "arabe"
    }

.##GET/livres/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant et le total des livres.

    EXEMPLE: http://localhost:5000/books/categories/4
```
    {
{
    "Success": true,
    "categorie": {
        "id": 7,
        "libelle": "sorcellerie"
    },
    "livres": [
        {
            "auteur": "JOJO",
            "categories id": 7,
            "date publication": "Sun, 14 Feb 2021 14:39:00 GMT",
            "editeur": "Vincent",
            "id": 7,
            "isbn": "8TRE",
            "titre": "L ENFANT NOIR"
        },
        {
            "auteur": "Amos",
            "categories id": 7,
            "date publication": "Sat, 01 Feb 2020 06:40:23 GMT",
            "editeur": "david",
            "id": 6,
            "isbn": "6RTR",
            "titre": "droit"
        }
    ],
    "total": 2
}
}
```

