'''
Bottom menu Class
Markku P
2021

top_menu.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class BottomMenu(QWidget):
    def __init__(self):
        super().__init__()
        # Crypt mode (1 = encrypt, 2 = decrypt)
        self.crypt_mode = None

        # Create layouts
        self.setFixedHeight(50)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,15,0,0)
        self.layout.setSpacing(0)

        # Create Encrypt / Decrypt button
        self.button_crypt = QPushButton()
        self.button_crypt.setMaximumWidth(300)
        font = self.button_crypt.font()
        font.setPointSize(20)
        self.button_crypt.setFont(font)
        self.button_crypt.clicked.connect(self.handle_crypt_button_pressed)

        # Add button to layout
        self.layout.addWidget(self.button_crypt)

        # Set layout
        self.setLayout(self.layout)

    def change_crypt_mode(self, mode):
        if mode == "encrypt":
            self.crypt_mode = 1
            self.button_crypt.setText("Encrypt")

        elif mode == "decrypt":
            self.crypt_mode = 2
            self.button_crypt.setText("Decrypt")

    def handle_crypt_button_pressed(self):
        pass