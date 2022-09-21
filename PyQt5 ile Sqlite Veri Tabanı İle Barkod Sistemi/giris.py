import satisyap
from PyQt5 import QtCore, QtGui, QtWidgets
import ürünekle


class Ui_MainWindow(object):
    def satisyappencere(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = satisyap.Ui_SatisWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def uruneklepencere(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ürünekle.Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 889)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(320, 20, 491, 341))
        self.Logo.setPixmap(QtGui.QPixmap("denemee.png"))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.ArkaPlan = QtWidgets.QLabel(self.centralwidget)
        self.ArkaPlan.setGeometry(QtCore.QRect(0, -10, 1131, 871))
        self.ArkaPlan.setPixmap(QtGui.QPixmap("arkaplan.jpg"))
        self.ArkaPlan.setText("")
        self.ArkaPlan.setObjectName("ArkaPlan")
        self.satisyap = QtWidgets.QPushButton(self.centralwidget)
        self.satisyap.setGeometry(QtCore.QRect(270, 500, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.satisyap.setFont(font)
        self.satisyap.setStyleSheet("background-color: rgb(57, 57, 57);\n"
"color: rgb(96, 255, 10);")
        self.satisyap.setObjectName("satisyap")
        self.urunekle = QtWidgets.QPushButton(self.centralwidget)
        self.urunekle.setGeometry(QtCore.QRect(270, 640, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.urunekle.setFont(font)
        self.urunekle.setStyleSheet("background-color: rgb(57, 57, 57);\n"
"color: rgb(96, 255, 10);")
        self.urunekle.setObjectName("urunekle")
        self.Telif = QtWidgets.QLabel(self.centralwidget)
        self.Telif.setGeometry(QtCore.QRect(400, 820, 331, 20))
        self.Telif.setObjectName("Telif")
        self.ArkaPlan.raise_()
        self.Logo.raise_()
        self.satisyap.raise_()
        self.urunekle.raise_()
        self.Telif.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.satisyap.clicked.connect(self.satisyappencere)
        self.urunekle.clicked.connect(self.uruneklepencere)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.satisyap.setText(_translate("MainWindow", "SATIŞ YAP"))
        self.urunekle.setText(_translate("MainWindow", "ÜRÜN EKLE"))
        self.Telif.setText(_translate("MainWindow", "© BU UYGULAMANIN BÜTÜN TELİF HAKLARI MAHMUT KUT\'A AİTTİR"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

