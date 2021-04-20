import random

GesuchteZahl = random.randint(0, 500)

def Check():
    i = True
    Versuche = 0
    Guess = int(input("Versuchen Sie die Zahl die ausgesucht wurde zu erraten!: "))
    while i == True:
        if Guess == GesuchteZahl:
            print("Sie haben die Zahl erraten!")
            i = False
            print(f"Sie haben {Versuche} Versuche gebraucht!")
        elif Guess < GesuchteZahl:
            print("Die gesuchte Zahl ist Größer!")
            Guess = int(input("Versuchen Sie die Zahl die ausgesucht wurde zu erraten!: "))
            Versuche = Versuche + 1
        elif Guess > GesuchteZahl:
            print("Die gesuchte Zahl ist kleiner!")
            Guess = int(input("Versuchen Sie die Zahl die ausgesucht wurde zu erraten!: "))
            Versuche = Versuche + 1


Check()