import os
import subprocess  
import sys
from PyQt5 import QtGui 
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore  
import qdarkstyle   #pip install qdarkstyle 
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QPushButton,QLabel,QFileDialog,QComboBox, QLCDNumber  #pip install PyQt5
from pytube import YouTube 
from itertools import islice
from math import ceil
from random import randint
from instaloader import Instaloader, Profile


from instaloader import Instaloader, Profile

#########################################################

#---> Deck

class App(QWidget):

    def __init__(self):
        super().__init__()

       
        
        app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        self.title = 'Deck'
        self.initUI()
        self.show()




    
    def initUI(self):
        #####__Internet__####

        label3 = QLabel('Interent', self)
        label3.move(50, 50)
        font3 = label3.font()
        font3.setPointSize(10)
        label3.setFont(font3)
          
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(40, 70, 100, 40)
        geek_list = ["Google","Youtube","T-online","Github","Iserv"] #Liste der Webseiten
        self.combo_box.addItems(geek_list)
        self.btn1 = QPushButton('OK', self)
        self.btn1.setGeometry(150, 70, 100, 40)
        self.btn1.clicked.connect(self.showDialog1)

        ####__IDE___####

        label4 = QLabel('IDE', self)
        label4.move(50, 120)
        font4 = label4.font()
        font4.setPointSize(10)
        label4.setFont(font4)

        self.combo_box1 = QComboBox(self)
        self.combo_box1.setGeometry(40, 140, 100, 40)
        geek_list1 = ["Android","Arduino","VSC","Net Beans"] #Liste der Webseiten
        self.combo_box1.addItems(geek_list1)
        self.btn2 = QPushButton('OK', self)
        self.btn2.setGeometry(150, 140, 100, 40)
        self.btn2.clicked.connect(self.showDialog2)




        label5 = QLabel('Programme', self)
        label5.move(50, 190)
        font5 = label5.font()
        font5.setPointSize(10)
        label5.setFont(font5)

        self.combo_box2 = QComboBox(self)
        self.combo_box2.setGeometry(40, 210, 100, 40)
        geek_list2 = ["Spotify","Steam","Paint","Notpad","Editor","Whatsapp","Discord","VM Ware"] #Liste der Webseiten
        self.combo_box2.addItems(geek_list2)
        self.btn3 = QPushButton('OK', self)
        self.btn3.setGeometry(150, 210, 100, 40)
        self.btn3.clicked.connect(self.showDialog3)

        self.btn4 = QPushButton('Shutdown', self)
        self.btn4.setGeometry(150, 280, 100, 40)
        self.btn4.clicked.connect(self.showDialog4)


        self.combo_box3 = QComboBox(self)
        self.combo_box3.setGeometry(300, 70, 100, 40)
        geek_list3 = ["Top 5","Top 10","Alle"] #Liste der Webseiten
        self.combo_box3.addItems(geek_list3)
        self.btn5 = QPushButton('OK', self)
        self.btn5.setGeometry(410, 70, 100, 40)
        self.btn5.clicked.connect(self.showDialog5)

        label1 = QLabel('Deck', self)
        label1.move(50, 0)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)

        label2 = QLabel('Instagram', self)
        label2.move(250, 0)
        font2 = label2.font()
        font2.setPointSize(20)
        label2.setFont(font2)


        self.setGeometry(1350, 50, 570, 400)
        self.setWindowTitle('Deck')
        self.show()

 
############################################################################################################################################################

#----< Deck >----# 
    def showDialog1(self):
        # finding the content of current item in combo box
        content = self.combo_box.currentText()
        if content=="Google":
        #subprocess.Popen(['C:\Program Files\Google\Chrome\Application\chrome.exe'])    #customize atei paths if it is not your default browser 
            subprocess.Popen("start chrome /new-tab https://www.google.com ",shell = True)  #wenn es dein standart browser ist. www.google.com durch jede andere webseite tauschen
        
        if content=="Youtube":
            subprocess.Popen("start chrome /new-tab https://www.youtube.com/watch?v=Lrj2Hq7xqQ8 ",shell = True)  #wenn es dein standart browser ist. www.google.com durch jede andere webseite tauschen
            
        if content=="T-online":
            subprocess.Popen("start chrome /new-tab https://email.t-online.de/em ",shell = True)  #wenn es dein standart browser ist. www.google.com durch jede andere webseite tauschen
        
        if content=="Iserv":
            subprocess.Popen("start chrome /new-tab https://bbs-lingen-tg.eu/iserv/app/login?target=%2Fiserv%2Fmail  ",shell = True)  #wenn es dein standart browser ist. www.google.com durch jede andere webseite tauschen
        
        if content=="Github":
            subprocess.Popen("start chrome /new-tab https://github.com/ ",shell = True)  #wenn es dein standart browser ist. www.google.com durch jede andere webseite tauschen
                         

    def showDialog2(self):
        content = self.combo_box1.currentText()
        if content=="Android":
            subprocess.Popen(['D:\\Android Studio\\bin\\studio64.exe']) 

        if content=="Arduino":
            subprocess.Popen(['C:\\Users\\tobia\\Documents\\Dokumente\\Arduino\\Programm\\arduino-nightly-windows\\arduino-nightly\\arduino.exe'])         #Customize file paths

        if content=="VSC":
           subprocess.Popen(['C:\\Users\\tobia\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'])   #Customize file paths    

        if content=="Net Beans":
            subprocess.Popen(['C:\\Program Files\\NetBeans-12.2\\netbeans\\bin\\netbeans64.exe'])   #Customize file paths

           

    def showDialog3(self):
        content = self.combo_box2.currentText()
        if content=="Spotify":
            subprocess.Popen(['Spotify.exe'])#standard path
       
        if content=="Steam":
             subprocess.Popen(['C:\\Program Files (x86)\\Steam\\Steam.exe'])  #Customize file paths
        
        if content=="Paint":
            subprocess.Popen(['mspaint.exe'])  #standard path

        if content=="Notpad":
            subprocess.Popen(['C:\\Program Files\\Notepad++\\notepad++.exe'])  #Customize file paths


        if content=="Editor":
            subprocess.Popen(['notepad.exe']) #standard path

        if content=="Whatsapp":
            subprocess.Popen(['C:\\ProgramData\\tobia\\WhatsApp\\WhatsApp.exe'])   #Customize file paths

        if content=="VM Ware":
            subprocess.Popen(['C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmplayer.exe'])   #Customize file paths
    	
        if content=="Discord":
            subprocess.Popen(['C:\\Users\\tobia\\AppData\\Local\\Discord\\app-1.0.9001\\Discord.exe'])  #Customize file paths

            

    def showDialog4(self):
        os.system("shutdown /s /t 0")  #Shutdown motherfucker 


    def showDialog6(self):
        pass
        
          
          

        

############################################################################################################################################################
  
#----< Inster >----# 


    def showDialog5(self):
        # finding the content of current item in combo box
        content = self.combo_box3.currentText()
        if content=="Top 5":
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Der Instagram Name:')
                      
            if ok:
               
                PROFILE = text
            
            L = Instaloader(save_metadata=True, compress_json=False, download_video_thumbnails=False, download_comments=False, post_metadata_txt_pattern="{likes}")
            
            profile = Profile.from_username(L.context, PROFILE)

            posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=False)

            for post in islice(posts_sorted_by_likes, ceil(5)):
                L.download_post(post, PROFILE)   

        if content=="Top 10":
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Der Instagram Name:')
                      
            if ok:
                
                PROFILE = text

            L = Instaloader(save_metadata=True, compress_json=False, download_video_thumbnails=False, download_comments=False, post_metadata_txt_pattern="{likes}")

            profile = Profile.from_username(L.context, PROFILE)

            posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=False)

            for post in islice(posts_sorted_by_likes, ceil(10)):
                L.download_post(post, PROFILE)  

        if content=="Alle":
            text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Der Instagram Name:')
                      
            if ok:
                
                PROFILE = text

            L = Instaloader(save_metadata=True, compress_json=False, download_video_thumbnails=False, download_comments=False, post_metadata_txt_pattern="{likes}")

            profile = Profile.from_username(L.context, PROFILE)

            posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=False)

            for post in islice(posts_sorted_by_likes, ceil(99999999999999)):
                L.download_post(post, PROFILE)              
           

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())         
