'''
Plain text I/O Class
Markku P
2021

plain_text_io.py
'''

from PyQt5.QtCore import QFile


class LoadPlainText():
    def __init__(self):
        super().__init__()
 
    def load(self, file_uri):
        try:
            if QFile.exists(file_uri):
                with open(file_uri) as f:
                    plain_text = f.read().replace("\n", "")
                    return plain_text

        except Exception:
            # TODO handle file open error
            return None


class SavePlainText():
    def __init__(self):
        super().__init__()
    
    def save(self, file_uri, plain_text):
        try:
            with open(file_uri, 'w') as f:
                f.write(plain_text)
                return True

        except Exception:
            # TODO handle file write error
            return False