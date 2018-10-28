from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QLabel
from PyQt5.QtGui import QFont, QIcon, QPixmap
import time

partytion=" "
class window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()
    def initUi(self):

        QToolTip.setFont(QFont("Arial",15))
        self.setToolTip("Wybierz Partycje")

        BTC = QPushButton("C",self)
        BTD = QPushButton("D",self)
        BTE = QPushButton("E",self)
        BTF = QPushButton("F",self)
        BTG = QPushButton("G",self)
        BTH = QPushButton("H",self)
        BTC.resize(BTC.sizeHint())
        BTC.move(50,50)
        BTD.resize(BTD.sizeHint())
        BTD.move(150, 50)
        BTE.resize(BTE.sizeHint())
        BTE.move(250, 50)
        BTF.resize(BTF.sizeHint())
        BTF.move(350, 50)
        BTG.resize(BTG.sizeHint())
        BTG.move(50, 100)
        BTH.resize(BTH.sizeHint())
        BTH.move(150, 100)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(250, 150)


        self.setGeometry(400,400,500,300)
        self.setWindowTitle("SSH")

        self.show()
        BTC.clicked.connect(self.clickevent)
        BTD.clicked.connect(self.clickevent)
        BTE.clicked.connect(self.clickevent)
        BTF.clicked.connect(self.clickevent)
        BTG.clicked.connect(self.clickevent)
        BTH.clicked.connect(self.clickevent)


    def clickevent(self):
        try:
            click=self.sender()
            if click.text()=="C":
                x="C"
            elif click.text()=="D":
                x="D"
            elif click.text()=="E":
                x="E"
            elif click.text()=="F":
                x="F"
            elif click.text()=="G":
                x="G"
            elif click.text()=="H":
                x="H"

            path = x + ":/ssh"

            open(path, "a").close()
            QMessageBox.warning(self,"Sukces","SSH UTWORZONO NA PARTYCJI {}".format(x),QMessageBox.Ok)

        except Exception as error:
            QMessageBox.critical(self, "Blad","{}".format(error),QMessageBox.Ok)


import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    sys.exit(app.exec_())