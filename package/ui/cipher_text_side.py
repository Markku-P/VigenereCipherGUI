'''
Cipher text side Class
Markku P
2021

cipher_text_side.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPlainTextEdit, QGroupBox
from PyQt5.QtCore import Qt, QObject, pyqtSlot as Slot


class CipherTextSide(QWidget):
    def __init__(self, signal_change_ciphering_mode):
        super().__init__()
        # Create layouts
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,10,0,0)
        self.layout.setSpacing(0)

        self.group_box_layout = QHBoxLayout()
        self.group_box_layout.setContentsMargins(0,0,0,0)
        self.group_box_layout.setSpacing(0)

        # Create groupbox
        self.group_box = QGroupBox("Cipher text")
        self.group_box.setLayout(self.group_box_layout)

        # Create textbox
        self.cipher_text = QPlainTextEdit()

        # Add widget to layout
        self.group_box_layout.addWidget(self.cipher_text)
        self.layout.addWidget(self.group_box)

        # Connect signal
        signal_change_ciphering_mode.connect(self.handle_change_ciphering_mode)

        # Set layout
        self.setLayout(self.layout)

    @Slot(int)
    def handle_change_ciphering_mode(self, mode):
        if mode == 1:
            self.cipher_text.setReadOnly(True)
            self.cipher_text.setPlaceholderText("Encrypted text")

        elif mode ==2:
            self.cipher_text.setReadOnly(False)
            self.cipher_text.setPlaceholderText("Enter encrypted text here")