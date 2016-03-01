# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhotoFrame(object):
    def setupUi(self, PhotoFrame):
        PhotoFrame.setObjectName("PhotoFrame")
        PhotoFrame.resize(670, 481)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PhotoFrame.sizePolicy().hasHeightForWidth())
        PhotoFrame.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PhotoFrame.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PhotoFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Viewer = QtWidgets.QLabel(PhotoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Viewer.sizePolicy().hasHeightForWidth())
        self.Viewer.setSizePolicy(sizePolicy)
        self.Viewer.setAutoFillBackground(False)
        self.Viewer.setText("")
        self.Viewer.setPixmap(QtGui.QPixmap(":/icons/dummy.png"))
        self.Viewer.setScaledContents(True)
        self.Viewer.setAlignment(QtCore.Qt.AlignCenter)
        self.Viewer.setObjectName("Viewer")
        self.gridLayout.addWidget(self.Viewer, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(PhotoFrame)
        QtCore.QMetaObject.connectSlotsByName(PhotoFrame)

    def retranslateUi(self, PhotoFrame):
        _translate = QtCore.QCoreApplication.translate
        PhotoFrame.setWindowTitle(_translate("PhotoFrame", "Photo Frame"))

import resources_rc
