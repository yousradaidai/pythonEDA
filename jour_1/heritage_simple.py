class DateNaissance:

    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        return "{:0>2d} / {:0>2d} / {}".format(self.jour, self.mois, self.annee)

class Personne:

    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Prénom: {self.prenom}")
        print(f"Date de naissance: {self.date_naissance}")

class Employe(Personne):

    def __init__(self, nom, prenom, date_naissance, salaire):
        super().__init__(nom, prenom, date_naissance)
        self.salaire = salaire

    def afficher(self):
        super().afficher()
        print("Salaire: {}".format(self.salaire))


class Chef(Employe):

    def __init__(self, nom, prenom, date_naissance, salaire, service):
        super().__init__(nom, prenom, date_naissance, salaire)
        self.service = service

    def afficher(self):
        super().afficher()
        print("Service: {}".format(self.service))


P=Personne("Ilyass","Math",DateNaissance(1,7,1982))
P.afficher()
# Nom: Ilyass 
# Prénom: Math
# Date de naissance: 01 / 07 / 1982
 
E=Employe("Ilyass","Math",DateNaissance(1,7,1985),7865.548)
E.afficher()
# Nom: Ilyass 
# Prénom: Math
# Date de naissance: 01 / 07 / 1985
# Salaire: 7865.55
 
Ch=Chef("Ilyass","Math",DateNaissance(1,7,1988),7865.548,"Ressource humaine")
Ch.afficher()
# Nom: Ilyass 
# Prénom: Math
# Date de naissance: 01 / 07 / 1988
# Salaire: 7865.55
# Service: Ressource humaine