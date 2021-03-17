from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets

import sys, os

from package.ui2 import Ui_MainWindow
from package.videocheck_project import VideoCheck


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Blanking Detector  by La Ruche Studio")
        self.project = VideoCheck()

        # Connexions
        # BOUTONS
        self.btn_import_video.clicked.connect(self.press_file_button)
        self.btn_start.clicked.connect(self.press_start_button)
        self.btn_report.clicked.connect(self.press_directory_button)
        # SpinBoxes
        self.spb_top_offset.valueChanged.connect(self.top_offset_changed)
        self.spb_bottom_offset.valueChanged.connect(self.bottom_offset_changed)
        self.spb_right_offset.valueChanged.connect(self.right_offset_changed)
        self.spb_left_offset.valueChanged.connect(self.left_offset_changed)

        self.spb_treshold.valueChanged.connect(self.treshold_changed)

        self.resize(1000, 500)
        self.show()

    def press_file_button(self):
        path = str(QtWidgets.QFileDialog.getOpenFileName()[0])
        res = self.project.load_video_file(path)
        if not res:
            print('error ffprobe')
        self.text_display.setPlainText(res)
        self.text_display.repaint()


    def press_start_button(self):
        if self.project.video_path == '':
            self.alert('Choose a video file')
            return
        if self.project.report_path == '':
            self.alert('Choose folder to create report')
            return

        self.project.analyse_video()
        self.text_display.setPlainText( str(self.project.generate_header() + '\n\n'+self.project.generate_report()))
        self.text_display.repaint()
        self.project.generate_html_report()

    def press_directory_button(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath:
            self.project.report_path = folderpath

    def top_offset_changed(self):
        self.project.crop_top = self.spb_top_offset.value()

    def bottom_offset_changed(self):
        self.project.crop_bottom = self.spb_bottom_offset.value()

    def right_offset_changed(self):
        self.project.crop_right = self.spb_right_offset.value()

    def left_offset_changed(self):
        self.project.crop_left = self.spb_left_offset.value()

    def treshold_changed(self):
        self.project.treshold = self.spb_treshold.value()

    def alert(self,message):
        self.m = QtWidgets.QMessageBox.about(self,"Attention", message)


if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = Window()

    window.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
