from portfolio.model.entities.service import Service
from pickle import Pickler,Unpickler

class Model:

    """initialisation of bdd to one object liste"""
    def init_bdd(self):
        liste = list()
        liste.append(Service())
        #ouvreture en ecriture binaire
        with open('portfolio/model/data',"wb") as fic:
            record = Pickler(fic)
            record.dump(liste)

    """ add service in database"""
    def add_service(self,name,techno,outil):
        #ouverture en lecture binaire
        with open('portfolio/model/data', "rb") as fic:
            record = Unpickler(fic)
            liste = record.load()
            liste.append(Service(name,techno,outil))
        # ouvreture en ecriture binaire
        with open('portfolio/model/data', "wb") as fic:
            record = Pickler(fic)
            record.dump(liste)

    """ display all services"""
    def display_all_service(self):
        # ouverture en lecture binaire
        with open('portfolio/model/data', 'rb') as fic:
            record = Unpickler(fic)
            liste = record.load()
        return liste

    """ delete one service """
    def delete_service(self,name):
        # ouverture en lecture binaire
        with open('portfolio/model/data', "rb") as fic:
            record = Unpickler(fic)
            liste = record.load()
        for el in liste:
            if el.name == name:
                liste.remove(el)
                break
        # ouvreture en ecriture binaire
        with open('portfolio/model/data', "wb") as fic:
            record = Pickler(fic)
            record.dump(liste)

#-------------------------------------------execution-----------------------------------

