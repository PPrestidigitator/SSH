# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QComboBox, QLabel
from PyQt5.QtGui import *
import sys
import datetime


class window(QWidget):
    selected_partition = ''

    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('img.jpg'))
        self.label.setGeometry(0, 0, 50, 250)
        self.lbl = QLabel(self)

        info = QLabel("Wybierz docelową partycje na której zostanie utworzony plik SSH", self)
        info.move(20, 20)
        QToolTip.setFont(QFont("Arial", 15))

        Create = QPushButton("Create", self)

        Create.setToolTip("kliknij aby utworzyć")

        Create.resize(Create.sizeHint())
        Create.move(100, 150)

        self.setGeometry(500, 400, 400, 250)
        self.setWindowTitle("SSH")

        ls = ["C", 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        partition = QComboBox(self)
        partition.addItems(ls)

        self.lbl = QLabel("wybierz partycje", self)

        partition.activated[str].connect(self.onactive)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200, 150)
        qbtn.setToolTip("Kliknij aby zamknąć")

        partition.move(200, 75)
        self.lbl.move(90, 75)

        Create.clicked.connect(self.clickevent)
        self.show()

    def onactive(self, text):
        global selected_partition
        self.lbl.setText(text)
        self.lbl.adjustSize()
        selected_partition = self.lbl.text()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def clickevent(self):
        timenow = datetime.datetime.now()
        try:
            click = self.sender()
            if click.text() == "Create":
                path = selected_partition + ":/ssh"
                open(path, "a").close()
                QMessageBox.warning(self, "Sukces", "SSH UTWORZONO NA PARTYCJI {}".format(selected_partition),
                                    QMessageBox.Ok)

        except FileNotFoundError as error:
            QMessageBox.critical(self, "Bląd", "Podana partycja nie istnieje: " "\n" "{}".format(selected_partition),
                                 QMessageBox.Ok)
            log = open("log.txt", "a")
            log.write(timenow.strftime("[%H:%M:%S %d.%m.%Y]") + ": {} \n".format(error))
            log.close()
        except Exception as unkown_ERROR:
            QMessageBox.warning(self, "Błąd", "Nieznany błąd", QMessageBox.Ok)
            log = open("log.txt", "a")
            log.write(timenow.strftime("[%H:%M:%S %d.%m.%Y]") + ": {} \n".format(unkown_ERROR))
            log.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    sys.exit(app.exec_())
