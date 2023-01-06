import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QLabel, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        vbox = QVBoxLayout()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # Hide the "?" button
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.resize(960, 750)
        # self.hint = QLabel("Enter your name:")
        # vbox.addWidget(self.hint)
        self.setLayout(vbox)
        self.setWindowTitle("青少年CTF-CTF工具 Developer 0.0.1")
        self.show()


app = QApplication(sys.argv)
dialog = Dialog()
sys.exit(app.exec_())
