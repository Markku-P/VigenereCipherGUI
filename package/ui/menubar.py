'''
Menubar Class
Markku P
2021

menubar.py
'''

from PyQt5.QtWidgets import QMenuBar, QAction
from PyQt5.QtGui import QKeySequence


class MenuBar(QMenuBar):
    def __init__(self, signal_close):
        super().__init__()

        # Create Menubar and actions
        # File menu
        self.actionFile = self.addMenu("File")

        self.new_action = QAction(self, text="New", shortcut=QKeySequence("Ctrl+N"))
        self.new_action.triggered.connect(lambda: print("New"))
        self.actionFile.addAction(self.new_action)

        self.open_action = QAction(self, text="Open", shortcut=QKeySequence("Ctrl+O"))
        self.open_action.triggered.connect(lambda: print("Open"))
        self.actionFile.addAction(self.open_action)

        self.save_action = QAction(self, text="Save", shortcut=QKeySequence("Ctrl+S"))
        self.save_action.triggered.connect(lambda: print("Save"))
        self.actionFile.addAction(self.save_action)

        self.actionFile.addSeparator()

        self.quit_action = QAction(self, text="Quit", shortcut=QKeySequence("Ctrl+Q"))
        self.quit_action.triggered.connect(lambda: signal_close.emit())
        self.actionFile.addAction(self.quit_action)

        # Edit menu
        self.actionEdit = self.addMenu("Edit")
        self.actionEdit.addAction("Copy").triggered.connect(lambda: print("Copy"))
        self.actionEdit.addAction("Paste").triggered.connect(lambda: print("Paste"))

        # Help menu
        self.actionHelp = self.addMenu("Help")
        self.actionHelp.addAction("Getting started").triggered.connect(lambda: print("Getting started"))
        self.actionHelp.addSeparator()
        self.actionHelp.addAction("About").triggered.connect(lambda: print("About"))