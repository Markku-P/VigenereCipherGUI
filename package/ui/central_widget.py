'''
Central widget Class
Markku P
2021

central_widget.py
'''

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSplitter
from PyQt5.QtCore import Qt
from package.ui.top_menu import TopMenu
from package.ui.plain_text_side import PlainTextSide
from package.ui.cipher_text_side import CipherTextSide
from package.ui.bottom_menu import BottomMenu


class CentralWidget(QWidget):
    def __init__(self, settings):
        super().__init__()
        # Create layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Create topmenu
        self.top_menu = TopMenu()

        # Create splitter 1
        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.setStyleSheet("QSplitter::handle{padding: 4px;}")

        # Create Plain text side
        self.plain_text_side = PlainTextSide()

        # Create Cipher text side
        self.cipher_text_side = CipherTextSide()

        # Create bottom menu
        self.bottom_menu = BottomMenu()

        # Add widgets to splitter
        self.splitter1.addWidget(self.plain_text_side)
        self.splitter1.addWidget(self.cipher_text_side)

        # Add top menu to layout
        self.layout.addWidget(self.top_menu)

        # Add splitters to layout
        self.splitter1.setSizes([122,1])
        self.layout.addWidget(self.splitter1)

        # Add bottom menu to layout
        self.layout.addWidget(self.bottom_menu)

        # Set layout
        self.setLayout(self.layout)
