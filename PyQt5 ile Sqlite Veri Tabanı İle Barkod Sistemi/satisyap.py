import sqlite3
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SatisWindow(object):
    def setupUi(self, SatisWindow):
        SatisWindow.setObjectName("SatisWindow")
        SatisWindow.resize(1129, 889)
        self.centralwidget = QtWidgets.QWidget(SatisWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(475, -10, 531, 261))
        self.Logo.setPixmap(QtGui.QPixmap("denemee2.png"))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.ArkaPlan = QtWidgets.QLabel(self.centralwidget)
        self.ArkaPlan.setGeometry(QtCore.QRect(0, -20, 1131, 931))
        self.ArkaPlan.setPixmap(QtGui.QPixmap("ArkaPlan.jpg"))
        self.ArkaPlan.setText("")
        self.ArkaPlan.setObjectName("ArkaPlan")
        self.satisyap = QtWidgets.QPushButton(self.centralwidget)
        self.satisyap.setGeometry(QtCore.QRect(420, 760, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.satisyap.setFont(font)
        self.satisyap.setStyleSheet("background-color: rgb(57, 57, 57);\n"
                                    "color: rgb(96, 255, 10);\n"
                                    "border-radius:25px;\n"
                                    "\n"
                                    "")
        self.satisyap.setObjectName("satisyap")
        self.Telif = QtWidgets.QLabel(self.centralwidget)
        self.Telif.setGeometry(QtCore.QRect(410, 830, 350, 20))
        self.Telif.setObjectName("Telif")
        self.barkodbilgi = QtWidgets.QLabel(self.centralwidget)
        self.barkodbilgi.setGeometry(QtCore.QRect(270, 210, 421, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.barkodbilgi.setFont(font)
        self.barkodbilgi.setObjectName("barkodbilgi")
        self.barkodgiris = QtWidgets.QLineEdit(self.centralwidget)
        self.barkodgiris.setGeometry(QtCore.QRect(270, 250, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.barkodgiris.setFont(font)
        self.barkodgiris.setStyleSheet("color: rgb(51, 208, 16);\n"
                                       "\n"
                                       "")
        self.barkodgiris.setText("")
        self.barkodgiris.setObjectName("barkodgiris")
        self.urunadibilgi = QtWidgets.QLabel(self.centralwidget)
        self.urunadibilgi.setGeometry(QtCore.QRect(270, 370, 421, 31))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.urunadibilgi.setFont(font)
        self.urunadibilgi.setObjectName("urunadibilgi")
        self.urunfiyatibilgi = QtWidgets.QLabel(self.centralwidget)
        self.urunfiyatibilgi.setGeometry(QtCore.QRect(270, 530, 421, 31))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.urunfiyatibilgi.setFont(font)
        self.urunfiyatibilgi.setObjectName("urunfiyatibilgi")
        self.urunfiyati = QtWidgets.QLabel(self.centralwidget)
        self.urunfiyati.setGeometry(QtCore.QRect(270, 560, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.urunfiyati.setFont(font)
        self.urunfiyati.setStyleSheet("background-color: rgb(216, 216, 216);\n"
                                      "color: rgb(51, 208, 16);\n"
                                      "\n"
                                      "")
        self.urunfiyati.setText("")
        self.urunfiyati.setObjectName("urunfiyati")
        self.urunadi = QtWidgets.QLabel(self.centralwidget)
        self.urunadi.setGeometry(QtCore.QRect(270, 400, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.urunadi.setFont(font)
        self.urunadi.setStyleSheet("background-color: rgb(216, 216, 216);\n"
                                   "color: rgb(51, 208, 16);\n"
                                   "\n"
                                   "")
        self.urunadi.setText("")
        self.urunadi.setObjectName("urunadi")
        self.urunebak = QtWidgets.QPushButton(self.centralwidget)
        self.urunebak.setGeometry(QtCore.QRect(420, 690, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.urunebak.setFont(font)
        self.urunebak.setStyleSheet("background-color: rgb(57, 57, 57);\n"
                                    "color: rgb(96, 255, 10);\n"
                                    "border-radius:25px;\n"
                                    "\n"
                                    "")
        self.urunebak.setObjectName("urunebak")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 630, 550, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.ArkaPlan.raise_()
        self.Logo.raise_()
        self.satisyap.raise_()
        self.Telif.raise_()
        self.barkodbilgi.raise_()
        self.barkodgiris.raise_()
        self.urunadibilgi.raise_()
        self.urunfiyatibilgi.raise_()
        self.urunfiyati.raise_()
        self.urunadi.raise_()
        self.urunebak.raise_()
        self.label.raise_()
        SatisWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SatisWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 21))
        self.menubar.setObjectName("menubar")
        SatisWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SatisWindow)
        self.statusbar.setObjectName("statusbar")
        SatisWindow.setStatusBar(self.statusbar)
        self.urunebak.clicked.connect(self.bilgial)
        self.satisyap.clicked.connect(self.satis)

        self.retranslateUi(SatisWindow)
        QtCore.QMetaObject.connectSlotsByName(SatisWindow)

    def retranslateUi(self, SatisWindow):
        _translate = QtCore.QCoreApplication.translate
        SatisWindow.setWindowTitle(_translate("SatisWindow", "MainWindow"))
        self.satisyap.setText(_translate("SatisWindow", "SATIŞ YAP"))
        self.Telif.setText(_translate("SatisWindow", "BU UYGULAMANIN BÜTÜN TELİF HAKLARI MAHMUT KUT\'A AİTTİR"))
        self.barkodbilgi.setText(_translate("SatisWindow", "ÜRÜN BARKODU OKUT :"))
        self.urunadibilgi.setText(_translate("SatisWindow", "ÜRÜNÜN ADI :"))
        self.urunfiyatibilgi.setText(_translate("SatisWindow", "ÜRÜNÜN  FİYATI  :"))
        self.urunebak.setText(_translate("SatisWindow", "ÜRÜNE BAK"))

    def bilgial(self):
        tablo = sqlite3.Connection("ürünler.db")
        edit = tablo.cursor()
        barkod = self.barkodgiris.text()

        edit.execute("CREATE TABLE IF NOT EXISTS ürünler(isim TEXT,barkod TEXT,fiyat NUMBER)")
        tablo.commit()
        edit.execute("SELECT * FROM ürünler WHERE barkod = ?", (barkod,))
        sorgulama = edit.fetchall()

        if (len(sorgulama) == 0):
            self.label.setText("!!!GEÇERSİZ BARKOD!!!")
        else:
            self.label.clear()
            edit.execute("SELECT isim FROM ürünler WHERE barkod = ?", (barkod,))
            isim = edit.fetchall()
            edit.execute("SELECT fiyat FROM ürünler WHERE barkod = ?", (barkod,))
            fiyat = edit.fetchall()
            self.urunadi.setText(isim[0][0])
            self.urunfiyati.setText(str(fiyat[0][0]))

    def satis(self):
        tablo = sqlite3.Connection("ürünler.db")
        edit = tablo.cursor()
        barkod = self.barkodgiris.text()
        zaman = str(datetime.datetime.now())
        if(len(barkod) != 0):
            edit.execute("CREATE TABLE IF NOT EXISTS ürünler(isim TEXT,barkod TEXT,fiyat NUMBER)")
            tablo.commit()
            edit.execute("SELECT isim FROM ürünler WHERE barkod = ?", (barkod,))
            isim = edit.fetchall()
            edit.execute("SELECT fiyat FROM ürünler WHERE barkod = ?", (barkod,))
            fiyat = edit.fetchall()
            tablo2 = sqlite3.Connection("satisbilgisi.db")
            edit2 = tablo2.cursor()
            edit2.execute("CREATE TABLE IF NOT EXISTS satisbilgisi(isim TEXT,fiyat NUMBER,barkod TEXT,tarih TEXT)")
            tablo2.commit()
            edit2.execute("INSERT INTO satisbilgisi VALUES(?,?,?,?)",(str(isim[0][0]), str(fiyat[0][0]), barkod, zaman,))
            tablo2.commit()
            self.barkodgiris.clear()
            self.urunadi.clear()
            self.urunfiyati.clear()
        else:
            self.label.setText("!!LÜTFEN BİLGİLERİ EKSİKSİZ GİRİN!!")


    def retranslateUi(self, SatisWindow):
        _translate = QtCore.QCoreApplication.translate
        SatisWindow.setWindowTitle(_translate("SatisWindow", "MainWindow"))
        self.satisyap.setText(_translate("SatisWindow", "SATIŞ YAP"))
        self.Telif.setText(_translate("SatisWindow", "© BU UYGULAMANIN BÜTÜN TELİF HAKLARI MAHMUT KUT\'A AİTTİR "))
        self.barkodbilgi.setText(_translate("SatisWindow", "ÜRÜN BARKODU OKUT :"))
        self.urunadibilgi.setText(_translate("SatisWindow", "ÜRÜNÜN ADI :"))
        self.urunfiyatibilgi.setText(_translate("SatisWindow", "ÜRÜNÜN  FİYATI  :"))
        self.urunebak.setText(_translate("SatisWindow", "ÜRÜNE BAK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SatisWindow = QtWidgets.QMainWindow()
    ui = Ui_SatisWindow()
    ui.setupUi(SatisWindow)
    SatisWindow.show()
    sys.exit(app.exec_())
