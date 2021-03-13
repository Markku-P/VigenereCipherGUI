'''
VigenereCipherGUI
*****************
Vigenere Cipher GUI using Python and QT framework
Markku P
2021

main.py
'''

import sys
import yaml
from PyQt5.QtWidgets import QApplication
from package.ui.mainwindow import MainWindow

if __name__ == "__main__":
    
    # Get app settings from settings.yaml file
    try:
        settings = yaml.safe_load(open("settings.yaml"))
    except FileNotFoundError:
        sys.exit("settings.yaml file not found. Exiting.")
    except yaml.YAMLError:
        sys.exit("Syntax error on settings.yaml. Please fix it and try again.")

    # Set Application name and versio
    app = QApplication(sys.argv)
    app.setApplicationName(str(settings.get("app").get("application_name") + " Ver " + str(settings.get("app").get("application_versio"))))
    app.setApplicationVersion(str(settings.get("app").get("application_versio")))

    # Create app mainwindow
    app_mainwindow = MainWindow(settings)

    sys.exit(app.exec_())