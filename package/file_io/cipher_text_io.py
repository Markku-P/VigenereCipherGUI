'''
Cipher text I/O Class
Markku P
2021

cipher_text_io.py
'''

from PyQt5.QtCore import QFile


class LoadCipherText():
    def __init__(self):
        super().__init__()
 
    def load(self, file_uri):
        try:
            if QFile.exists(file_uri):
                with open(file_uri) as f:
                    cipher_text = f.read()
                    return cipher_text

        except Exception:
            # TODO handle file open error
            return None


class SaveCipherText():
    def __init__(self):
        super().__init__()

    def save(self, file_uri, cipher_text):
        pass