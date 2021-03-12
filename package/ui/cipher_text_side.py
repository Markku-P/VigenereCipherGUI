'''
Cipher text side Class
Markku P
2021

cipher_text_side.py
'''

from PyQt5.QtWidgets import QWidget, QFrame, QHBoxLayout


class CipherTextSide(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        # empty mockup
        self.empty_mockup = QFrame()
        self.empty_mockup.setFrameShape(QFrame.StyledPanel)
        self.empty_mockup.setStyleSheet("background: #000000;")
        # ------------

        self.layout.addWidget(self.empty_mockup)
        self.setLayout(self.layout)