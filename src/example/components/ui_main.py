# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(408, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_text = QLineEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setGeometry(QRect(60, 30, 200, 22))
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setGeometry(QRect(20, 30, 57, 14))
        self.button_t = QPushButton(self.centralwidget)
        self.button_t.setObjectName(u"button_t")
        self.button_t.setGeometry(QRect(20, 60, 80, 30))
        self.button_f = QPushButton(self.centralwidget)
        self.button_f.setObjectName(u"button_f")
        self.button_f.setGeometry(QRect(110, 60, 80, 30))
        self.button_and = QPushButton(self.centralwidget)
        self.button_and.setObjectName(u"button_and")
        self.button_and.setGeometry(QRect(200, 60, 80, 30))
        self.button_or = QPushButton(self.centralwidget)
        self.button_or.setObjectName(u"button_or")
        self.button_or.setGeometry(QRect(290, 60, 80, 30))
        self.button_equal = QPushButton(self.centralwidget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setGeometry(QRect(150, 100, 100, 30))
        self.button_delete = QPushButton(self.centralwidget)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setGeometry(QRect(260, 100, 80, 30))
        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(20, 150, 57, 14))
        self.output_text = QLabel(self.centralwidget)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setGeometry(QRect(80, 140, 200, 40))
        self.Prefix = QLabel(self.centralwidget)
        self.Prefix.setObjectName(u"Prefix")
        self.Prefix.setGeometry(QRect(80, 190, 200, 40))
        self.Prefix.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Logic Calculator", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.button_t.setText(QCoreApplication.translate("MainWindow", u"t", None))
        self.button_f.setText(QCoreApplication.translate("MainWindow", u"f", None))
        self.button_and.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.button_or.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.button_delete.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #f44336; color: white; font-weight: bold;", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.output_text.setText("")
        self.output_text.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"       background-color: white;\n"
"       color: black;\n"
"       font-family: Consolas, monospace;\n"
"       font-size: 18px;\n"
"       border: 3px solid black;\n"
"       border-radius: 4px;\n"
"       padding: 5px;\n"
"     ", None))
        self.Prefix.setText(QCoreApplication.translate("MainWindow", u"Prefix result", None))
        self.Prefix.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"       background-color: white;\n"
"       color: black;\n"
"       font-family: Consolas, monospace;\n"
"       font-size: 18px;\n"
"       border: 3px solid black;\n"
"       border-radius: 4px;\n"
"       padding: 5px;\n"
"     ", None))
    # retranslateUi

