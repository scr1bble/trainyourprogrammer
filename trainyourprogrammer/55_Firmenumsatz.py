# Die Zentrale einer Supermarktkette möchte die Umsatzzahlen ermitteln.
# Hierzu läßt sie sich die Zahlen aus den einzelnen Filialen geben.
# Diese haben wiederum unterschiedliche Kassen, die morgens mit einer gewissen Anfangsumme bestückt werden und am Abend eine Endsumme haben.

# Erstelle entsprechende Klassen mit sinnvollen Methoden um den Gesamtumsatz zu berechnen.


import random

class Kasse():
    def __init__(self):
        super().__init__()

        self.Kassenstand = 250

    def kassenstandänderung(self, val):
        self.Kassenstand+=val

    def diebstahl(self):
        self.Kassenstand = 0

    def Kleingeldbetrug(self):
        self.Kassenstand += 1


class Filiale():
    def __init__(self):
        super().__init__()

        self.Kassen = []
        self.GesamtKassenstand = 0

        for i in range(random.randint(4,10)):
            self.Kassen.append(Kasse)

    def gesamtKassenstandberechnen(self):
        for i in range(len(self.Kassen)):
            self.GesamtKassenstand += self.Kassen[i].Kassenstand
            

