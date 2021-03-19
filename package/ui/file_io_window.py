'''
File IO window (QFileDialog)
Markku P
2021

file_io_window.py
'''

from PyQt5.QtWidgets import QFileDialog


class LoadFile(QFileDialog):
    def __init__(self):
        super().__init__()
        self.setFileMode(QFileDialog.ExistingFile)

    def load(self, window_title, filters_str = "All files (*.*)"):
        file_name = self.getOpenFileName(caption=window_title, filter=filters_str)
        return file_name

class SaveFile(QFileDialog):
    def __init__(self):
        super().__init__()
        self.setFileMode(QFileDialog.AnyFile)

    def save(self, window_title, filters_str = "All files (*.*)"):
        file_name = self.getSaveFileName(caption=window_title, filter=filters_str)
        return file_name