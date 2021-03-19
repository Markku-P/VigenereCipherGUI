'''
Top menu Class
Markku P
2021

top_menu.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QCheckBox, QLineEdit
from PyQt5.QtCore import Qt
from package.ui.file_io_window import LoadFile, SaveFile


class TopMenu(QWidget):
    def __init__(self, signal_change_ciphering_mode):
        super().__init__()
        # Create main layout
        self.setFixedHeight(150)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(10,0,10,5)
        self.layout.setSpacing(0)
        
        # Create settings groupbox layout
        self.group_box_layout = QHBoxLayout()
        self.group_box_layout.setContentsMargins(10,0,0,10)
        self.group_box_layout.setSpacing(10)
        self.group_box_layout.setAlignment(Qt.AlignLeft)

        # Create settings groupbox
        self.group_box = QGroupBox("Settings")
        self.group_box.setMinimumWidth(800)
        self.group_box.setLayout(self.group_box_layout)

        # Create sub groupboxes
        self.create_mode_groupbox()
        self.create_cipher_key_groupbox()
        self.create_cipher_alphabets_groupbox()

        # Add sub groupboxes to main groupbox layout
        self.group_box_layout.addWidget(self.group_box_mode)
        self.group_box_layout.addWidget(self.group_box_key)
        self.group_box_layout.addWidget(self.group_box_alphabets)

        # Add settings groupbox to layout
        self.layout.addWidget(self.group_box)

        # Create instance of signal
        self.signal_change_ciphering_mode = signal_change_ciphering_mode

        # Set defaults
        self.encrypt_pressed()
        self.checkbox_default_key.setChecked(True)

        # Set layout
        self.setLayout(self.layout)

    def encrypt_pressed(self):
        self.button_decrypt.setStyleSheet("QPushButton {color: gray;} QPushButton::hover {color: white;}")
        self.button_encrypt.setStyleSheet("background-color: red;")

        # Send signal
        self.signal_change_ciphering_mode.emit(1)

    def decrypt_pressed(self):
        self.button_encrypt.setStyleSheet("QPushButton {color: gray;} QPushButton::hover {color: white;}")
        self.button_decrypt.setStyleSheet("background-color: red;")

        # Send signal
        self.signal_change_ciphering_mode.emit(2)

    def create_mode_groupbox(self):
        # Create layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10,5,10,5)
        layout.setSpacing(0)

        self.group_box_mode = QGroupBox("Mode")
        self.group_box_mode.setStyleSheet("QGroupBox { font-size: 14px; } ")
        self.group_box_mode.setMinimumWidth(160)
        self.group_box_mode.setLayout(layout)

        # Create buttons
        self.button_encrypt = QPushButton("Encrypt")
        self.button_encrypt.setMaximumWidth(200)
        self.button_encrypt.setMaximumHeight(26)
        self.button_encrypt.clicked.connect(self.encrypt_pressed)

        self.button_decrypt = QPushButton("Decrypt")
        self.button_decrypt.setMaximumWidth(200)
        self.button_decrypt.setMaximumHeight(26)
        self.button_decrypt.clicked.connect(self.decrypt_pressed)

        # Add widgets to layout
        layout.addWidget(self.button_encrypt)
        layout.addWidget(self.button_decrypt)

    def create_cipher_key_groupbox(self):
        # Create layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10,5,10,5)
        layout.setSpacing(0)

        sub_layout = QHBoxLayout()
        sub_layout.setAlignment(Qt.AlignLeft)

        self.group_box_key = QGroupBox("Cipher key")
        self.group_box_key.setStyleSheet("QGroupBox { font-size: 14px; } ")
        self.group_box_key.setMinimumWidth(250)
        self.group_box_key.setLayout(layout)

        # Create textbox
        self.textedit_key = QLineEdit()
        self.textedit_key.setFixedHeight(30)
        self.textedit_key.setPlaceholderText("Enter cipher key here")

        # Create buttons
        self.button_load_cipher_key = QPushButton("Load")
        self.button_load_cipher_key.setMaximumWidth(200)
        self.button_load_cipher_key.clicked.connect(self.load_key_file)

        self.button_save_cipher_key = QPushButton("Save")
        self.button_save_cipher_key.setMaximumWidth(200)
        self.button_save_cipher_key.clicked.connect(self.save_key_file)

        # Add widgets to layout
        layout.addWidget(self.textedit_key)
        sub_layout.addWidget(self.button_load_cipher_key)
        sub_layout.addWidget(self.button_save_cipher_key)
        layout.addLayout(sub_layout)

    def create_cipher_alphabets_groupbox(self):
        # Create layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10,0,10,5)
        layout.setSpacing(0)

        sub_layout = QHBoxLayout()
        sub_layout.setSpacing(10)
        
        self.group_box_alphabets = QGroupBox("Cipher alphabets")
        self.group_box_alphabets.setStyleSheet("QGroupBox { font-size: 14px; } ")
        self.group_box_alphabets.setMinimumWidth(400)
        self.group_box_alphabets.setLayout(layout)

        # Create checkbox
        self.checkbox_default_key = QCheckBox("Use default cipher alphabets")
        self.checkbox_default_key.setStyleSheet("QCheckBox { font-size: 14px; } ")
        self.checkbox_default_key.stateChanged.connect(self.set_default_cipher_alphabets)

        # Create textbox
        self.textedit_alphabets_file = QLineEdit()
        self.textedit_alphabets_file.setFixedHeight(30)
        self.textedit_alphabets_file.setPlaceholderText("File path")
        self.textedit_alphabets_file.setReadOnly(True)

        # Create button
        self.button_load_cipher_alphabets = QPushButton("Load")
        self.button_load_cipher_alphabets.setMinimumWidth(100)
        self.button_load_cipher_alphabets.clicked.connect(self.load_alphabets_file)

        # Add widgets to layout
        sub_layout.addWidget(self.textedit_alphabets_file)
        sub_layout.addWidget(self.button_load_cipher_alphabets)
        layout.addLayout(sub_layout)
        layout.addWidget(self.checkbox_default_key)

    def set_default_cipher_alphabets(self, state):
        if state:
            self.textedit_alphabets_file.setEnabled(False)
            self.button_load_cipher_alphabets.setEnabled(False)
        else:
            self.textedit_alphabets_file.setEnabled(True)
            self.button_load_cipher_alphabets.setEnabled(True)

    def load_key_file(self):
        load_file = LoadFile()
        key_file_name, extension = load_file.load("Load key file", "Vigenere key files (*.vkf);;All files (*.*)")

        if key_file_name != "":
            # TODO load file
            pass
            
    def save_key_file(self):
        save_file = SaveFile()
        key_file_name, extension = save_file.save("Save key file", "Vigenere key files (*.vkf);;All files (*.*)")

        if key_file_name != "":
            # TODO save file
            pass
    
    def load_alphabets_file(self):
        load_file = LoadFile()
        alphabets_file_name, extension = load_file.load("Load alphabets file", "Vigenere alphabets files (*.vaf);;All files (*.*)")

        if alphabets_file_name != "":
            self.textedit_alphabets_file.setText(alphabets_file_name)
            # TODO load file
            pass