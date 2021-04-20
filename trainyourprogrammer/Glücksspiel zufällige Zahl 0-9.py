#Die Aufgabenstellung ist wie folgt:
#- Glücksspiel bei der eine random Zahl zwischen 0 - 9 erzeugt werden soll.
#- Der Spieler hat ein Startkonto von 10.000 Punkten und kann damit einen beliebigen Teilbetrag auf die zufällig erzeugte Zahl setzen.
#- Liegt er richtig bekommt er das 9 Fache seines Einsatzes als Gewinn
#- Programmieren Sie ein entsprechendes Programm, welches die Eingaben von der Tastatur einliest und
# die Ausgaben auf dem Bildschirm liefert. Die zu erratende Zahl kann durch einen verfügbaren Zufallsgenerator gezogen werden.
# 237


from random import randint

class bet_game:

    def __init__(self):
        
        self.points = 10000
        self.game_active = True

    def menu(self):
        print("-------------------------------------")
        print(f"You have {self.points} Points")
        print("What do you want to do?")
        print("\n[1]Bet\n[2]Exit")
        print("-------------------------------------\n")
        try:
            inp_menu = int(input("# "))
            if inp_menu == 1:
                self.game_function()
            elif inp_menu == 2:
                self.game_active = False
        except ValueError:
            print("\n-------------------------------------\nPlease insert a number\n-------------------------------------\n")
            temp = input("Press Enter to continue\n") 


    def game_function(self):
        
        rand_num = randint(0, 9)
        #print(rand_num)
        print("\nA random number has been created!")
        try:
            inp_num = int(input("Enter a Number from 0 to 9: "))    
            if(inp_num >= 0 and inp_num <= 9):
                inp_point = int(input("Enter the amount of points u want to bet: "))
                if(inp_point >= 0 and inp_point <= self.points):
                    self.points -= inp_point
                    if inp_num == rand_num:
                        print("-------------------------------------")
                        print("Congratulations you picked the right number and multiplied your points 9 times")
                        print("-------------------------------------")
                        inp_point *= 9
                        self.points += inp_point
                        temp = input("Press Enter to continue\n")
                    elif inp_num != rand_num:
                        print("-------------------------------------")
                        print("Wrong number")
                        print("-------------------------------------")
                        temp = input("\nPress Enter to continue\n")

                    else:
                        print("Something went wrong!")
                
                else:
                    print("\n-------------------------------------\nInvalid number\n-------------------------------------\n")
                    temp = input("Press Enter to continue\n")


            else:
                print("\n-------------------------------------\nInvalid number\n-------------------------------------\n")
                temp = input("Press Enter to continue\n")  

        except ValueError:
            print("\n-------------------------------------\nPlease insert a number\n-------------------------------------\n")
            temp = input("Press Enter to continue\n") 
               
    def run(self):

        print("\nWelcome to the Bet Game")
        while self.game_active:

            self.menu()
    
game = bet_game()
game.run()