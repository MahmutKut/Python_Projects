import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.yazi_alani2= QLabel("")

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.yazi_alani)
        self.v_box.addWidget(self.yazi_alani2)

        self.setLayout(self.v_box)

class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Notepad()
        self.setCentralWidget(self.pencere)
        self.menu()

    def menu(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        düzen = menubar.addMenu("Düzen")

        self.yeni = QAction("Yeni")
        self.yeni.setShortcut("CTRL+N")

        self.dosya_ac = QAction("Aç")
        self.dosya_ac.setShortcut("CTRL+O")

        self.dosya_kaydet = QAction("Kaydet")
        self.dosya_kaydet.setShortcut("CTRL+S")

        self.cikis = QAction("Çıkış")
        self.cikis.setShortcut("CTRL+Q")

        self.degistir = QAction("DEGİSTİR")



        self.setWindowTitle("NOTEBOOK")

        dosya.addAction(self.yeni)
        dosya.addAction(self.dosya_ac)
        dosya.addAction(self.dosya_kaydet)
        dosya.addAction(self.cikis)


        dosya.triggered.connect(self.click)

        self.setGeometry(700,300,500,500)
        self.show()
    def click(self,action):
        if(action.text() == "Yeni"):
            if(int(len(self.pencere.yazi_alani.toPlainText())) != 0):
                self.pencere.yazi_alani2.setText("YAZILI OLAN METİNLER VAR YENİ DOSYA AÇMAK İSTİYOR MUSUNUZ ?")
                self.buton = QPushButton("Yeni Dosya Aç")
                self.pencere.v_box.addWidget(self.buton)
                self.buton.clicked.connect(self.penceretemizle)


        elif (action.text() == "Aç"):
            dosya_adi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
            file = open(dosya_adi[0],"r")
            self.pencere.yazi_alani.setText(file.read())
        elif (action.text() == "Kaydet"):
            dosya_adi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
            file = open(dosya_adi[0],"w")
            file.write(self.pencere.yazi_alani.toPlainText())
        elif(action.text()=="Çıkış"):
            qApp.exit()

    def penceretemizle(self):
        self.pencere.yazi_alani.clear()
        self.pencere.yazi_alani2.clear()
        self.buton.close()




app = QApplication(sys.argv)
note = Notebook()
sys.exit(app.exec_())