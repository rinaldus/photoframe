# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(487, 120)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        self.txtPath = QtWidgets.QLineEdit(Settings)
        self.txtPath.setGeometry(QtCore.QRect(110, 10, 341, 22))
        self.txtPath.setAutoFillBackground(False)
        self.txtPath.setReadOnly(True)
        self.txtPath.setObjectName("txtPath")
        self.btnOpen = QtWidgets.QPushButton(Settings)
        self.btnOpen.setGeometry(QtCore.QRect(460, 10, 21, 21))
        self.btnOpen.setObjectName("btnOpen")
        self.label = QtWidgets.QLabel(Settings)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 21))
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setGeometry(QtCore.QRect(160, 90, 165, 21))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(Settings)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 141, 21))
        self.label_2.setObjectName("label_2")
        self.spinUpdateInterval = QtWidgets.QSpinBox(Settings)
        self.spinUpdateInterval.setGeometry(QtCore.QRect(160, 50, 51, 22))
        self.spinUpdateInterval.setMinimum(1)
        self.spinUpdateInterval.setMaximum(1000)
        self.spinUpdateInterval.setProperty("value", 60)
        self.spinUpdateInterval.setObjectName("spinUpdateInterval")
        self.label_3 = QtWidgets.QLabel(Settings)
        self.label_3.setGeometry(QtCore.QRect(220, 50, 56, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.btnOpen.setText(_translate("Settings", "..."))
        self.label.setText(_translate("Settings", "Source path"))
        self.label_2.setText(_translate("Settings", "Change picture every"))
        self.label_3.setText(_translate("Settings", "minutes"))

import resources_rc
