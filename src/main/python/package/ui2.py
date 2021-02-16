# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1647, 640)
        MainWindow.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #222831;\n"
"	color: #fff;\n"
"	selection-background-color: #fff;\n"
"	selection-color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #EEEDE7;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"	background-color: #4a5157;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"	background-color: transparent;\n"
"	border-left: 1px solid #003333;\n"
"	padding: 5px;\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"	background-color: #003333;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"	background-color: #006666;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}"
                        "\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #4a5157;\n"
"    border: 1px solid #4a5157;\n"
"    padding: 10px;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"	min-width: 200px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"   	background-color: #242424;\n"
"	height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"	background-color: #003333;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	padding: 3px;\n"
"	margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"	color: #000;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToo"
                        "lButton:pressed\n"
"{\n"
"	background-color: #727272;\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	background-color: #727272;\n"
"	border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #4891b4;\n"
"	color: #fff;\n"
"	min-width: 80px;\n"
"	border-radius: 4px;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #606060;\n"
"	color: #959595;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #54aad3;\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #2385b4;\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	background-color: #bd5355;\n"
"	border: 1px solid #bd5355;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit"
                        "-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #242424;\n"
"	color : #fff;\n"
"	border: 1px solid #868B8E;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"	border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"	background-color: #242424;\n"
"	color : #fff;\n"
"	border: 1px solid #868B8E;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBox-----*/\n"
"QToolBox\n"
"{\n"
"	background-color: transparent;\n"
"	border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBox::tab\n"
"{\n"
"	background-color: #002b2b;\n"
"	border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBox::tab:hover\n"
"{\n"
"	background-color: #006d6d;\n"
"	border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: #4a5157;\n"
"    padding-left: 6px;\n"
"    color: #fff;\n"
"    height: 20px;\n"
"	border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	ba"
                        "ckground-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #4a5157;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #4a5157;\n"
"    color: #fff;\n"
"    selection-background-color: #002b2b;\n"
"	selection-color: #fff;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	background-color: #4a5157;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"	border-radius: 4px;\n"
"    width: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDoubleSpinBox & QCalendarWidget-----*/\n"
"QDoubleSpinBox,\n"
"QCalendarWidget QSpinBox \n"
"{\n"
"	background-color: #242424;\n"
"	color : #fff;\n"
"	border: 1px solid #1d1d1d;\n"
"	border-radius: 4px;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDo"
                        "ubleSpinBox::up-button, \n"
"QCalendarWidget QSpinBox::up-button\n"
"{\n"
"	background-color: #4a5157;\n"
"    width: 16px; \n"
"	border-top-right-radius: 4px;\n"
"    border-width: 1px;\n"
"	border-color: #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:hover, \n"
"QCalendarWidget QSpinBox::up-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed, \n"
"QCalendarWidget QSpinBox::up-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-arrow,\n"
"QCalendarWidget QSpinBox::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button, \n"
"QCalendarWidget QSpinBox::down-button\n"
"{\n"
"	background-color: #4a5157;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"	border-bottom-right-radius: 4px;\n"
"	border-color: #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-b"
                        "utton:hover, \n"
"QCalendarWidget QSpinBox::down-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button:pressed, \n"
"QCalendarWidget QSpinBox::down-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-arrow,\n"
"QCalendarWidget QSpinBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #1d1d1d;\n"
"	border-radius: 4px;\n"
"    margin-top: 23px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: #002b2b;\n"
"    color: #fff;\n"
"	subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	min-width: 100px;\n"
"	border: 1px solid #1d1d1d;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom: none;\n"
"\n"
"}\n"
"\n"
""
                        "\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #4a5157;\n"
"	border: none;\n"
"    color: #fff;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCalendarWidget-----*/\n"
"QCalendarWidget QToolButton\n"
"{\n"
"  	background-color: transparent;\n"
"  	color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QToolButton::hover\n"
"{\n"
"	background-color: #006666;\n"
"	border: 1px solid #006666;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QMenu \n"
"{\n"
"	width: 120px;\n"
"	left: 20px;\n"
"	color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QWidget \n"
"{ \n"
"	alternate-background-color: #4a5157; \n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"{\n"
"	color: #fff;  \n"
"	background-color: #242424;  \n"
"	selection-background-color: #002b2b; \n"
"	selection-color: #fff; \n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QAbstractI"
                        "temView:disabled \n"
"{ \n"
"	color: #404040; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"	show-decoration-selected: 0;\n"
"	alternate-background-color: transparent;\n"
"	background-color: transparent;\n"
"   	border: none;\n"
"	color: #fff;\n"
"	font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"	color:#fff;\n"
"	background-color: #002b2b;\n"
"	border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"	background-color: transparent;\n"
"	alt"
                        "ernate-background-color: transparent;\n"
"    border : none;\n"
"    color: #fff;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"   	border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"	background-color: transparent;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"	background-color: #002b2b;\n"
"	border: 1px solid #002b2b;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"	background-color: #002b2b;\n"
"	border: 1px solid #002b2b;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"	background-color: #002b2b;\n"
"	border: 1px solid #002b2b;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #5e5e5e;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox----"
                        "-*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: lightgray;\n"
"    border: 1px solid #000;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: #002b2b;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"	border: 1px solid #46a2da; \n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"	color: #fff;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"	background-color: #d3d3d3;\n"
"	border: 2px solid #002b2b"
                        ";\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"	border: 2px solid #52beff;\n"
"	border-radius: 6px;\n"
"	background-color: #002b2b;  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:vertical \n"
"{\n"
"   border: none;\n"
"   width: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"   border: none;\n"
"   border-radius : 0px;\n"
"   background-color: #7a7a7a;\n"
"   min-height: 80px;\n"
"   width : 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"   background-color: #5d5f60; \n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:pressed \n"
"{\n"
"   background"
                        "-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical \n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"   background-color: #222222;\n"
"	\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal \n"
"{\n"
"   border: none;\n"
"   height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"   border: none;\n"
"   border-radius : 0px;\n"
"   background-color: #7a7a7a;\n"
"   min-height: 80px;\n"
""
                        "   height : 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal:pressed\n"
"{\n"
"   background-color: #5d5f60; \n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal\n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;"
                        "\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:horizontal \n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"   background-color: #222222;\n"
"	\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"	border: 1px solid #1d1d1d;\n"
"    text-align: center;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #3b86ae;\n"
"	border-radius: 9px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar\n"
"{\n"
"	background-color: #4a5157;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSizeGrip-----*/\n"
"QSizeGrip \n"
"{\n"
"	background-color: image(\"./ressources/sizegrip.png\"); /*To replace*/\n"
"	border: none;\n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_10)

        self.btn_import_video = QPushButton(self.centralwidget)
        self.btn_import_video.setObjectName(u"btn_import_video")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.btn_import_video)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_7)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.spb_top_offset = QSpinBox(self.centralwidget)
        self.spb_top_offset.setObjectName(u"spb_top_offset")
        self.spb_top_offset.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.spb_top_offset)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.spb_bottom_offset = QSpinBox(self.centralwidget)
        self.spb_bottom_offset.setObjectName(u"spb_bottom_offset")
        self.spb_bottom_offset.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.spb_bottom_offset)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.spb_left_offset = QSpinBox(self.centralwidget)
        self.spb_left_offset.setObjectName(u"spb_left_offset")
        self.spb_left_offset.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.spb_left_offset)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.spb_right_offset = QSpinBox(self.centralwidget)
        self.spb_right_offset.setObjectName(u"spb_right_offset")
        self.spb_right_offset.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.spb_right_offset)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(8, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_6)

        self.spb_treshold = QSpinBox(self.centralwidget)
        self.spb_treshold.setObjectName(u"spb_treshold")
        self.spb_treshold.setAlignment(Qt.AlignCenter)
        self.spb_treshold.setValue(2)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.spb_treshold)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(10, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.btn_report = QPushButton(self.centralwidget)
        self.btn_report.setObjectName(u"btn_report")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.btn_report)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.lineEdit_2)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.btn_start)


        self.horizontalLayout.addLayout(self.formLayout)

        self.text_display = QPlainTextEdit(self.centralwidget)
        self.text_display.setObjectName(u"text_display")
        self.text_display.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.text_display)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText("")
        self.btn_import_video.setText(QCoreApplication.translate("MainWindow", u"Video File", None))
        self.label_7.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Top Offset in pixels", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bottom Offset in pixel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Left Offset in pixel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Right Offset in pixel", None))
        self.label_8.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Treshold ( recommended 2)", None))
        self.label_9.setText("")
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"Report directory", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"START !", None))
    # retranslateUi
