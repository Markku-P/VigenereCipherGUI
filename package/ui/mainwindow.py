'''
Main Window Class
Markku P
2021

mainwindow.py
'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, settings):
        super().__init__()
        self.initUi(settings)
        
    def initUi(self, settings):
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.resize(settings["app"]["width"], settings["app"]["height"])

        # Dark theme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53,53,53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(15,15,15))
        palette.setColor(QPalette.AlternateBase, QColor(53,53,53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53,53,53))
        palette.setColor(QPalette.Disabled, QPalette.Button, QColor(53, 53, 53).darker())
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.gray)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Highlight, QColor(142,45,197).lighter())
        palette.setColor(QPalette.HighlightedText, Qt.black)
        QApplication.setPalette(palette)
        QApplication.setStyle(QStyleFactory.create('Fusion'))

        # Create statusbar
        self.statusBar().show()
        self.statusBar().setFixedHeight(30)

        # Show Mainwindow
        self.show()

    def closeEvent(self, event):
        event.accept()