'''
Cipher text side Class
Markku P
2021

cipher_text_side.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QGroupBox, QPushButton
from PyQt5.QtCore import Qt, QObject, pyqtSlot as Slot
from package.ui.file_io_window import LoadFile, SaveFile
from package.file_io.cipher_text_io import LoadCipherText, SaveCipherText


class CipherTextSide(QWidget):
    def __init__(self, signal_change_ciphering_mode):
        super().__init__()
        # Create layouts
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,10,0,0)
        self.layout.setSpacing(0)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(10,0,0,0)
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setAlignment(Qt.AlignLeft)

        self.group_box_layout = QHBoxLayout()
        self.group_box_layout.setContentsMargins(0,0,0,0)
        self.group_box_layout.setSpacing(0)

        # Create groupbox
        self.group_box = QGroupBox("Cipher text")
        self.group_box.setLayout(self.group_box_layout)

        # Create textbox
        self.cipher_text = QPlainTextEdit()

        # Create buttons
        self.button_load_file = QPushButton("Load")
        self.button_load_file.setMaximumWidth(200)
        self.button_load_file.clicked.connect(self.load_encrypt_text)

        self.button_save_file = QPushButton("Save")
        self.button_save_file.setMaximumWidth(200)
        self.button_save_file.clicked.connect(self.save_encrypt_text)

        self.button_clear = QPushButton("Clear")
        self.button_clear.setMaximumWidth(200)
        self.button_clear.clicked.connect(lambda: self.cipher_text.clear())

        # Add widget to layout
        self.buttons_layout.addWidget(self.button_load_file)
        self.buttons_layout.addWidget(self.button_save_file)
        self.buttons_layout.addWidget(self.button_clear)
        self.group_box_layout.addWidget(self.cipher_text)
        self.layout.addWidget(self.group_box)
        self.layout.addLayout(self.buttons_layout)

        # Connect signal
        signal_change_ciphering_mode.connect(self.handle_change_ciphering_mode)

        # Set layout
        self.setLayout(self.layout)

    @Slot(int)
    def handle_change_ciphering_mode(self, mode):
        if mode == 1:
            self.cipher_text.setReadOnly(True)
            self.cipher_text.setPlaceholderText("Encrypted text")
            self.button_load_file.setEnabled(False)
            self.cipher_text.clear()

        elif mode ==2:
            self.cipher_text.setReadOnly(False)
            self.cipher_text.setPlaceholderText("Enter encrypted text here")
            self.button_load_file.setEnabled(True)

    def load_encrypt_text(self):
        load_file = LoadFile()
        encrypt_file_name, extension = load_file.load("Load encrypt file", "Vigenere encrypt files (*.vef);;Text files (*.txt);;All files (*.*)")

        if encrypt_file_name != "":            
            # Load file
            load_cipher_text = LoadCipherText()
            encrypt_text_data = load_cipher_text.load(encrypt_file_name)

            if encrypt_text_data is not None:
                # Clear cipher text window
                self.cipher_text.clear()

                # Set encrypt text
                self.cipher_text.insertPlainText(encrypt_text_data)

    def save_encrypt_text(self):
        save_file = SaveFile()
        encrypt_file_name, extension = save_file.save("Save encrypt file", "Vigenere encrypt files (*.vef);;All files (*.*)")

        if encrypt_file_name != "":
            # TODO save file
            pass