'''
Plain text side Class
Markku P
2021

plain_text_side.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPlainTextEdit, QGroupBox


class PlainTextSide(QWidget):
    def __init__(self):
        super().__init__()
        # Create layouts
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,10,0,0)
        self.layout.setSpacing(0)

        self.group_box_layout = QHBoxLayout()
        self.group_box_layout.setContentsMargins(0,0,0,0)
        self.group_box_layout.setSpacing(0)

        # Create groupbox
        self.group_box = QGroupBox("Plain text")
        self.group_box.setLayout(self.group_box_layout)

        # Create textbox
        self.plain_text = QPlainTextEdit()
        self.plain_text.setPlaceholderText("Enter text here")

        # Add widget to layout
        self.group_box_layout.addWidget(self.plain_text)
        self.layout.addWidget(self.group_box)

        # Set layout
        self.setLayout(self.layout)