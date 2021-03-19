'''
Bottom menu Class
Markku P
2021

bottom_menu.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QObject, pyqtSlot as Slot

class ErrorOnDefaultMode(Exception):
    # To catch syntax error on default mode setting
    pass

class BottomMenu(QWidget):
    def __init__(self, settings, signal_change_ciphering_mode):
        super().__init__()
        # Crypt mode (1 = encrypt, 2 = decrypt)
        default_mode = settings.get("app").get("default_mode")

        # Try to get default crypt mode from settings
        try:
            if default_mode is not None and not (int(default_mode) < 1 or int(default_mode > 2)):
                self.crypt_mode = int(default_mode)
            else:
                raise ErrorOnDefaultMode()

        except (ValueError, ErrorOnDefaultMode):
            # Using default encrypt mode
            self.crypt_mode = 1

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

        # Connect change ciphering mode signal
        signal_change_ciphering_mode.connect(self.change_crypt_mode)

        # Set defaults
        signal_change_ciphering_mode.emit(self.crypt_mode)

        # Set layout
        self.setLayout(self.layout)

    @Slot(int)
    def change_crypt_mode(self, mode):
        if mode == 1:
            self.crypt_mode = 1
            self.button_crypt.setText("Encrypt")

        elif mode == 2:
            self.crypt_mode = 2
            self.button_crypt.setText("Decrypt")

    def handle_crypt_button_pressed(self):
        pass