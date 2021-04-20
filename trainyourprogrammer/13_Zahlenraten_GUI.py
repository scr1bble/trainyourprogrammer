from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel
import sys
import qdarkstyle
import random

class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.resW = QApplication.desktop().screenGeometry().width()
        self.resH = QApplication.desktop().screenGeometry().height()
        self.width = 400
        self.height = 500
        self.posx = (self.resH / 2) - self.height / 2
        self.posy = (self.resW / 2) - self.width / 2

        self.GesuchteZahl = random.randint(0,10)
        self.Guess = 0
        self.Versuche = 0

        self.windowsSetting()
        self.createLine_Raten()

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def windowsSetting(self):
        self.setWindowTitle("Zahlen raten YOOOOOO")
        self.setGeometry(int(self.posy),int(self.posx),int(self.width),int(self.height))
        self.show()

    def createLine_Raten(self):
        self.Raten = QLineEdit(self)
        self.Raten.resize(100,100)
        self.Raten.move(100,100)
        self.Raten.show()

        self.textLineRaten = QLabel(self)
        self.textLineRaten.setText("  Versuchen Sie die Zahl zu erraten!     ")
        self.textLineRaten.move(100, 80)
        self.textLineRaten.show()

        self.Zahlgezogen = QLabel(self)
        self.Zahlgezogen.setText("Die Zahl wurde ausgesucht, nun ist es Ihre Aufgabe diese zu erraten!   ")
        self.Zahlgezogen.move(35,50)
        self.Zahlgezogen.show()

        self.SubmitVersuch = QPushButton("Zahl einreichen!    ", self)
        self.SubmitVersuch.clicked.connect(self.OnButtonSubmit)
        self.SubmitVersuch.move(200,100)
        self.SubmitVersuch.resize(100,100)
        self.SubmitVersuch.show()

        self.VersucheText = QLabel(self)
        self.VersucheText.setText(f"Sie brauchten bisher {self.Versuche} Versuche!   ")
        self.VersucheText.move(110, 400)
        self.VersucheText.resize(400,100)
        self.VersucheText.show()

        self.KleinerGrößer = QLabel(self)
        self.KleinerGrößer.move(120, 350)
        self.KleinerGrößer.resize(400,20)
        self.KleinerGrößer.show()


    def OnButtonSubmit(self):

        if self.Raten.text()=="":
            Guess = 0
        else:
            Guess = int(self.Raten.text())
        self.Guess = Guess





        if Guess == self.GesuchteZahl:
            self.Erraten = QLabel(self)
            self.Erraten.setText("  Sie haben die Zahl erraten!    ")
            self.Erraten.move(110,300)
            self.Erraten.show()
            self.VersucheText.setText(f"Sie haben {self.Versuche} Versuche gebraucht!    ")
            self.Lösung = QLabel(self)
            self.Lösung.setText(f"Die Lösung lautete {Guess}      ")
            self.Lösung.move(130,400)
            self.Lösung.show()
            self.Versuche = self.Versuche + 1


        if Guess < self.GesuchteZahl:

            self.Versuche = self.Versuche + 1
            self.Raten.setText("")
            self.VersucheText.setText(f"Sie brauchten bisher {self.Versuche} Versuche!   ")
            self.VersucheText.show()
            self.KleinerGrößer.setText("Die gesuchte Zahl ist größer!     ")
            self.KleinerGrößer.show()

        if Guess > self.GesuchteZahl:
            self.Versuche = self.Versuche + 1
            self.Raten.setText("")
            self.VersucheText.setText(f"Sie brauchten bisher {self.Versuche} Versuche!   ")
            self.VersucheText.show()
            self.KleinerGrößer.setText("Die gesuchte Zahl ist kleiner!   ")
            self.KleinerGrößer.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = Fenster()
    sys.exit(app.exec())