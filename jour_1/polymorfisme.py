class Courrier:

    def __init__(self, adrDest, adrExp, poids, expMode):
        self.adrDest = adrDest
        self.adrExp = adrExp
        self.poids = poids
        self.expMode = expMode

    def ToString(self):
        print(f"Adresse destination: {self.adrDest}")
        print(f"Adresse expédition: {self.adrExp}")
        print(f"Poids: {self.poids} grammes")
        print(f"Mode: {self.expMode}")


class Colis(Courrier):

    def __init__(self, adrDest, adrExp, poids, expMode, volume):
        super().__init__(adrDest, adrExp, poids, expMode)
        self.volume = volume

    def calculTimbre(self):
        if self.expMode == "normal":
            return (0.25 * self.volume) * (self.poids/1000)
        elif self.expMode == "expresse":
            return (25 * self.volume) * (self.poids/1000) * 20

    def ToString(self):
        print("Colis: ")
        super().ToString()
        print("Volume: {} litres".format(self.volume))
        print("Prix du timbre: {}".format(self.calculTimbre()))


class Lettre(Courrier):

    def __init__(self, adrDest, adrExp, poids, expMode, format):
        super().__init__(adrDest, adrExp, poids, expMode)
        self.format = format

    def calculTimbre(self):
        tarifDeBase = 3.5
        if self.format == "A4":
            tarifDeBase = 2.50
        if self.expMode == "normal":
            return tarifDeBase + (self.poids/1000)
        
        elif self.expMode == "expresse":
            return tarifDeBase + (2.0 * (self.poids/1000))

    def ToString(self):
        print("Lettre: ")
        super().ToString()

        print("Format: {}".format(self.format))
        print("Prix du timbre: {}".format(self.calculTimbre()))


L1=Lettre("Lille","Paris",80,"normal","A4")
L1.ToString()
# Lettre:
# Adresse destination: Lille 
# Adress expedition: Paris
# Poids: 80.00 grammes
# Mode: normal 
# Format:A4
# Prix du timbre:0.20
C1=Colis("Marrakeche","Barcelone",3500,"expresse",2.25)
C1.ToString()
# Collis:
# Adresse destination: Marrakeche 
# Adress expedition: Barcelone 
# Poids: 3500.00 grammes
# Mode: expresse 
# Volume: 2.25 litres
# Prix du timbre:3937.50