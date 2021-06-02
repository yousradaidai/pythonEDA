class CompteBancaire :
    def __init__(self, nom='Almada',solde=1000):
        self.nom = nom
        self.solde = solde
        #print("compte créé avec succées, vous êtes déjà facturé de frais")
    def depot(self,somme):
        self.solde = self.solde + somme
    def retrait(self,somme):
        self.solde = self.solde - somme 
    def affiche(self):
        print(f"Le solde du compte de {self.nom} est de {str(self.solde)}")

compte1 = CompteBancaire("Duchmol", 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
#Le solde du compte bancaire de Duchmol est de 950 euros.
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()
#Le solde du compte bancaire de Dupont est de 1025 euros.