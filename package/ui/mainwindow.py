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
from package.ui.about_window import AboutWindow


class SignalComm(QObject):
    close_app = Signal()
    show_about = Signal()
    change_ciphering_mode = Signal(int)

class MainWindow(QMainWindow):
    def __init__(self, settings):
        super().__init__()
        self.initUi(settings)
        self.about_window = AboutWindow(settings["app"]["application_name"], settings["app"]["application_versio"])
        
    def initUi(self, settings):
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.setMinimumSize(400, 300)
        self.resize(settings["app"]["width"], settings["app"]["height"])

        # Create signals instance
        self.signal_comm = SignalComm()

        # Signals
        self.signal_comm.close_app.connect(self.close)
        self.signal_comm.show_about.connect(self.about)

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
        self.menubar = MenuBar(self.signal_comm.close_app, self.signal_comm.show_about)

        # Create central widget
        self.central_widget = CentralWidget(settings, self.signal_comm.change_ciphering_mode)

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
    def about(self):
        if self.about_window is not None:
            self.about_window.setWindowModality(Qt.ApplicationModal)
            self.about_window.move(self.x() + (self.width() / 2 - self.about_window.width() / 2), self.y() + (self.height() / 2 - self.about_window.height() / 2))
            self.about_window.show()
            self.about_window.activateWindow()

            # After about window close set focus back to mainwindow
            parent = self
            self.about_window.closeEvent = lambda self: parent.activateWindow()

    def closeEvent(self, event):
        print("Exiting")
        event.accept()