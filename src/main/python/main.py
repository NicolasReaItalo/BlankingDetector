from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets

import sys

from package.ui2 import Ui_MainWindow
from package.videocheck_project import VideoCheck

class Window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Blanking Detector  by La Ruche Studio")
        self.project = VideoCheck()



        # Connexions
        self.btn_import_video.clicked.connect(self.press_file_button)
        self.btn_start.clicked.connect(self.press_analyse_button)

        self.resize(700,500)
        self.show()

    def press_file_button(self):
        pass


    def press_analyse_button(self):
        pass




if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Window()

    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)