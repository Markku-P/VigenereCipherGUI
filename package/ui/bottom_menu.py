'''
Bottom menu Class
Markku P
2021

bottom_menu.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QObject, pyqtSlot as Slot


class BottomMenu(QWidget):
    def __init__(self, settings, signal_change_ciphering_mode):
        super().__init__()

        # Create layouts
        self.setFixedHeight(50)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,15,0,0)
        self.layout.setSpacing(0)

        # Create Encrypt / Decrypt button
        self.button_cipher = QPushButton()
        self.button_cipher.setMaximumWidth(300)
        font = self.button_cipher.font()
        font.setPointSize(20)
        self.button_cipher.setFont(font)
        self.button_cipher.clicked.connect(self.handle_cipher_button_pressed)

        # Add button to layout
        self.layout.addWidget(self.button_cipher)

        # Connect change ciphering mode signal
        signal_change_ciphering_mode.connect(self.handle_ciphering_mode_change)

        # Set layout
        self.setLayout(self.layout)

    @Slot(int)
    def handle_ciphering_mode_change(self, mode):
        if mode == 1:
            self.button_cipher.setText("Encrypt")

        elif mode == 2:
            self.button_cipher.setText("Decrypt")

    def handle_cipher_button_pressed(self):
        # TODO start encrypt/decrypt
        pass