'''
Plain text side Class
Markku P
2021

plain_text_side.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QGroupBox, QPushButton
from PyQt5.QtCore import Qt, QObject, pyqtSlot as Slot
from package.ui.file_io_window import LoadFile, SaveFile
from package.file_io.plain_text_io import LoadPlainText, SavePlainText


class PlainTextSide(QWidget):
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
        self.group_box = QGroupBox("Plain text")
        self.group_box.setLayout(self.group_box_layout)

        # Create textbox
        self.plain_text = QPlainTextEdit()

        # Create buttons
        self.button_load_file = QPushButton("Load")
        self.button_load_file.setMaximumWidth(200)
        self.button_load_file.clicked.connect(self.load_plain_text)

        self.button_save_file = QPushButton("Save")
        self.button_save_file.setMaximumWidth(200)
        self.button_save_file.clicked.connect(self.save_plain_text)

        self.button_clear = QPushButton("Clear")
        self.button_clear.setMaximumWidth(200)
        self.button_clear.clicked.connect(lambda: self.plain_text.clear())

        # Add widget to layout
        self.buttons_layout.addWidget(self.button_load_file)
        self.buttons_layout.addWidget(self.button_save_file)
        self.buttons_layout.addWidget(self.button_clear)
        self.group_box_layout.addWidget(self.plain_text)
        self.layout.addWidget(self.group_box)
        self.layout.addLayout(self.buttons_layout)

        # Connect signal
        signal_change_ciphering_mode.connect(self.handle_change_ciphering_mode)

        # Set layout
        self.setLayout(self.layout)

    @Slot(int)
    def handle_change_ciphering_mode(self, mode):
        if mode == 1:
            self.plain_text.setReadOnly(False)
            self.plain_text.setPlaceholderText("Enter plain text here")
            self.button_load_file.setEnabled(True)

        elif mode ==2:
            self.plain_text.setReadOnly(True)
            self.plain_text.setPlaceholderText("Plain text")
            self.button_load_file.setEnabled(False)
            self.plain_text.clear()

    def load_plain_text(self):
        load_file = LoadFile()
        plain_text_file_name, extension = load_file.load("Load text file", "Text files (*.txt);;All files (*.*)")

        if plain_text_file_name != "":            
            # Load file
            load_plain_text = LoadPlainText()
            plain_text_data = load_plain_text.load(plain_text_file_name)

            if plain_text_data is not None:
                # Clear plain text window
                self.plain_text.clear()

                # Set plain text
                self.plain_text.insertPlainText(plain_text_data)

    def save_plain_text(self):
        save_file = SaveFile()
        plain_text_file_name, extension = save_file.save("Save text file", "Text files (*.txt);;All files (*.*)")

        if plain_text_file_name != "":
            # Save file
            plain_text_data = self.plain_text.toPlainText()
            save_plain_text = SavePlainText()
            save_plain_text.save(plain_text_file_name, plain_text_data)