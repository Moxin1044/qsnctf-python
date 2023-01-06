from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("MainWindow")
        Main.resize(948, 745)
        Main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/19190/.designer/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
