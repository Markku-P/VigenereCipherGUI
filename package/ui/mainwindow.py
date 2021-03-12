'''
Main Window Class
Markku P
2021

mainwindow.py
'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QStatusBar, QMenuBar
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import Qt, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from package.ui.menubar import MenuBar
from package.ui.central_widget import CentralWidget


class SignalComm(QObject):
    close_app = Signal()

class MainWindow(QMainWindow):
    def __init__(self, settings):
        super().__init__()
        self.initUi(settings)
        
    def initUi(self, settings):
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.setMinimumSize(400, 300)
        self.resize(settings["app"]["width"], settings["app"]["height"])

        # Create signals instance
        self.signal_comm = SignalComm()

        # Signals
        self.signal_comm.close_app.connect(self.close)

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

        # Create menubar
        self.menubar = MenuBar(self.signal_comm.close_app)

        # Create central widget
        self.central_widget = CentralWidget(settings)

        # Create statusbar
        self.statusbar = QStatusBar()
        self.statusbar.setFixedHeight(25)

        # Add widgets to mainwindow
        self.setMenuBar(self.menubar)
        self.setCentralWidget(self.central_widget)
        self.setStatusBar(self.statusbar)

        # Show Mainwindow
        self.show()

    @Slot()
    def closeEvent(self, event):
        print("Exiting")
        event.accept()