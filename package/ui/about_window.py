'''
About window Class
Markku P
2021

about_window.py
'''

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import Qt


class AboutWindow(QWidget):
    def __init__(self, app_name = "Vigenere Cipher GUI", app_versio = 0):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("About")
        self.setFixedSize(400,300)

        # Create layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10,10,10,10)

        # Create label and text
        self.label01 = QLabel("ABOUT")
        self.label01.setAlignment(Qt.AlignCenter)
        font = self.label01.font()
        font.setPointSize(20)
        self.label01.setFont(font)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        about_html = f"""<font size='4'>{app_name}</font><br>
                        <font size='2'>Versio {app_versio}</font><br>
                        <font size='2'>
                        Programmed with Python and Qt Framework<br><br>
                        Modules used:
                        <ul>
                        <li>PyQt5</li>
                        <li>PyYAML</li>
                        <li>Vigenere cipher module (By Markku P)</li>
                        </ul><br>
                        </font>
                        <font size='4'>
                        Markku P 2021
                        </font> 
                        """
        self.text.setHtml(about_html)

        # Create pushbutton
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        # Add widgets to layout
        self.layout.addWidget(self.label01)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.close_button)

        # Set layout
        self.setLayout(self.layout)