



#Formelsammlung
# U = R*I
# I = R/U
# R = I/U
#Werte eingabe
print("Geben sie die Werte in Ganzen Zahlen an. Für keinen Wert einfach die Null eingeben ")
U = int(input("Wie lautet ihr Voltwert "))
I = int(input("Wie lautet ihre Stromstärke "))
R = int(input("Wie lautet ihr Ohm wert "))
#Spannung berechnet
if R and I != 0 and U == 0:
    print("Die fehlende Spannung lautet:", R*I ,"Volt")
#Stromberechnung     
elif U and R != 0 and I == 0:
    Strom = U/R
    print("Der fehlende Strom lautet:", Strom ,"Ampere")
#Ohm Berechnung
elif U and I != 0 and R == 0:
    Widerstand = U/I
    print("Der fehlende Widerstand lautet:", Widerstand ,"Ohm")
# Wenn 2 Werte Gleich null sind soll er den Fehler ausgeben 
else:
    print("Falsche Eingabe! Ein Eingabewert muss Null sein")