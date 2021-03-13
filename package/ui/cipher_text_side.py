'''
Cipher text side Class
Markku P
2021

cipher_text_side.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPlainTextEdit


class CipherTextSide(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        # Create textbox
        self.cipher_text = QPlainTextEdit()
        self.cipher_text.setPlaceholderText("Encrypted text")
        self.cipher_text.setReadOnly(True)

        # Add widget to layout
        self.layout.addWidget(self.cipher_text)

        # Set layout
        self.setLayout(self.layout)