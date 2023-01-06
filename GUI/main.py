import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets


class QMainWindow(QMainWindow):
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
        self.codetable = QTabWidget()
        self.codetable.setMovable(True)  # 允许移动选项卡
        titles = ["Base64编码", "Base64解码", "Base32编码"]
        for i in range(3):
            tab = CodeTab()
            layout = QVBoxLayout()
            layout.addWidget(QLabel(titles[i]))
            tab.setLayout(layout)
            self.codetable.addTab(tab, titles[i])
        self.setCentralWidget(self.codetable)
        self.setLayout(vbox)
        self.setWindowTitle("青少年CTF-CTF工具 Developer 0.0.1")
        self.show()


class CodeTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 创建垂直布局
        layout = QVBoxLayout()
        self.input_edit = QTextEdit()
        self.output_edit = QTextEdit()
        layout.addWidget(self.input_edit)
        layout.addWidget(self.output_edit)
        # 创建按钮
        enbutton = QPushButton("编码")
        debutton = QPushButton("解码")
        enbutton.clicked.connect(self.convert)  # 点击按钮时调用convert()方法
        layout.addWidget(enbutton)
        debutton.clicked.connect(self.convert)  # 点击按钮时调用convert()方法
        layout.addWidget(debutton)

        self.setLayout(layout)

    def convert(self):
        print("test")


app = QApplication(sys.argv)
dialog = QMainWindow()
sys.exit(app.exec_())
