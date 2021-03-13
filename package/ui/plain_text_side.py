'''
Plain text side Class
Markku P
2021

plain_text_side.py
'''

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPlainTextEdit


class PlainTextSide(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        # Create textbox
        self.plain_text = QPlainTextEdit()
        self.plain_text.setPlaceholderText("Enter text here")

        # Add widget to layout
        self.layout.addWidget(self.plain_text)

        # Set layout
        self.setLayout(self.layout)
