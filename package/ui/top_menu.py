'''
Top menu Class
Markku P
2021

top_menu.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton


class TopMenu(QWidget):
    def __init__(self):
        super().__init__()
        # Create layouts
        self.setFixedHeight(150)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(10,0,10,5)
        self.layout.setSpacing(0)
        
        self.group_box_layout = QVBoxLayout()
        self.group_box_layout.setContentsMargins(10,0,0,10)
        self.group_box_layout.setSpacing(0)

        self.group_box_layout_mode = QVBoxLayout()
        self.group_box_layout_mode.setContentsMargins(10,5,10,5)
        self.group_box_layout_mode.setSpacing(0)


        # Create groupboxs
        self.group_box = QGroupBox("Settings")
        self.group_box.setLayout(self.group_box_layout)

        self.group_box_mode = QGroupBox("Mode")
        self.group_box_mode.setStyleSheet("QGroupBox { font-size: 14px; } ")
        self.group_box_mode.setMaximumWidth(160)
        self.group_box_mode.setLayout(self.group_box_layout_mode)

        # Create buttons
        self.button_encrypt = QPushButton("Encrypt")
        self.button_encrypt.setMaximumWidth(200)
        self.button_encrypt.setMaximumHeight(26)
        self.button_encrypt.clicked.connect(self.encrypt_pressed)

        self.button_decrypt = QPushButton("Decrypt")
        self.button_decrypt.setMaximumWidth(200)
        self.button_decrypt.setMaximumHeight(26)
        self.button_decrypt.clicked.connect(self.decrypt_pressed)

        # Add widget to layouts
        self.group_box_layout_mode.addWidget(self.button_encrypt)
        self.group_box_layout_mode.addWidget(self.button_decrypt)
        self.group_box_layout.addWidget(self.group_box_mode)

        self.layout.addWidget(self.group_box)

        # Set default mode to encrypt
        self.encrypt_pressed()

        # Set layout
        self.setLayout(self.layout)

    def encrypt_pressed(self):
        self.button_decrypt.setStyleSheet("QPushButton {color: gray;} QPushButton::hover {color: white;}")
        self.button_encrypt.setStyleSheet("background-color: red;")
        # TODO send signal

    def decrypt_pressed(self):
        self.button_encrypt.setStyleSheet("QPushButton {color: gray;} QPushButton::hover {color: white;}")
        self.button_decrypt.setStyleSheet("background-color: red;")
        # TODO send signal