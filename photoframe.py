#!/usr/bin/env python3

from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout, QSizeGrip, QFileDialog)
from PyQt5.QtCore import (QThread, QTimer, QFile, QSettings,Qt, QPoint )
import resources_rc
from ui_main import Ui_PhotoFrame
from ui_settings import Ui_Settings
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import random
import fnmatch

programSettings = QSettings(os.path.expanduser("~")+"/.config/photoframe/settings.conf", QSettings.NativeFormat)
MainWindowType = QtCore.Qt.Tool

def SettingsExist():
    if (programSettings.contains("SizeX") and
        programSettings.contains("SizeY") and
        programSettings.contains("directory") and
        programSettings.contains("PosX") and
        programSettings.contains("PosY") and
        programSettings.contains("UpdateInterval")):
        return True
    else:
        return False

def SettingsSave():
    programSettings.setValue("SizeX",window.geometry().width())
    programSettings.setValue("SizeY",window.geometry().height())
    programSettings.setValue("directory",settings.ui.txtPath.text())
    programSettings.setValue("PosX",window.x())
    programSettings.setValue("PosY",window.y())
    programSettings.setValue("UpdateInterval",settings.ui.spinUpdateInterval.value())

#Settings load

if (SettingsExist()):
    SizeX = int(programSettings.value("SizeX"))
    SizeY = int(programSettings.value("SizeY"))
    directory = programSettings.value("directory")
    PosX = int(programSettings.value("PosX"))
    PosY = int(programSettings.value("PosY"))
    UpdateInterval = int(programSettings.value("UpdateInterval"))
else:
    SizeX = 800
    SizeY = 600
    directory = ""
    PosX = 50
    PosY = 50
    UpdateInterval = 60

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        
        # Init
        
        self.ui = Ui_PhotoFrame()
        self.ui.setupUi(self)
        self.setWindowFlags(MainWindowType | Qt.WindowStaysOnBottomHint | Qt.FramelessWindowHint)
        self.locked = True
        self.resize(SizeX, SizeY)
        self.move(PosX,PosY)
        # Viewer configuration
        if (directory != ""):
            picture = QtGui.QPixmap(getRandomPicture(directory)).scaled(SizeX,SizeY,QtCore.Qt.KeepAspectRatio)
            self.ui.Viewer.setPixmap(picture)
        self.ui.Viewer.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.Viewer.customContextMenuRequested.connect(self.showMenu)
        
        # Timer
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerTimeout)
        
    # Functions    
    def showMenu(self,point):
            menu = QMenu(self)
            if self.locked:
                menu.addAction(QAction(QIcon(':icons/unlock.png'),"&Unlock", self, triggered=self.Unlock))
            else:
                menu.addAction(QAction(QIcon(':icons/lock.png'),"&Lock", self, triggered=self.Lock))
            menu.addAction(QAction(QIcon(':icons/refresh.png'),"&Refresh", self, triggered=self.Refresh))
            menu.addAction(QAction(QIcon(':icons/settings.png'),"&Settings", self, triggered=settings.show))
            menu.addAction(QAction(QIcon(':icons/menu_quit.png'),"&Quit", self, triggered=QApplication.instance().quit))
            menu.popup(self.mapToGlobal(point))
        
    def Unlock(self):
        window.setWindowFlags(QtCore.Qt.Window)
        self.locked = False
        window.show()
        
    def Lock(self):
        window.setWindowFlags(MainWindowType | Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint)
        self.locked = True
        window.show()
        
    def closeEvent(self, event):
        SettingsSave()
        QApplication.instance().quit()
        
    def Refresh(self):
        if (SettingsExist()):
            setPicture(programSettings.value("directory"))
            
    def resizeEvent(self,event):
        programSettings.setValue("SizeX",window.geometry().width())
        programSettings.setValue("SizeY",window.geometry().height())
        
        
    def moveEvent(self,event):
        programSettings.setValue("PosX",window.x())
        programSettings.setValue("PosY",window.y())
            
    def start(self):
        self.timer.setInterval(settings.ui.spinUpdateInterval.value()*1000*60)
        
        self.timer.start()
    
    def stop(self):
        self.timer.stop()
        
    def timerTimeout(self):
        self.ui.Viewer.setPixmap(QtGui.QPixmap(getRandomPicture(settings.ui.txtPath.text())).scaled(SizeX,SizeY,QtCore.Qt.KeepAspectRatio))
    
        
class Settings(QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        
        # Init
        
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.ui.txtPath.setText(directory)
        if SettingsExist():
            self.ui.spinUpdateInterval.setValue(int(programSettings.value("UpdateInterval")))
        
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.btnOK_clicked)
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.btnCancel_clicked)
        self.ui.btnOpen.clicked.connect(self.btnOpen_clicked)
        
        # Functions
        
    def btnCancel_clicked(self):
        self.hide()
    
    def closeEvent(self, event): 
        self.hide()
        event.ignore()
        
    def btnOpen_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, 'Open file', os.path.expanduser("~"), QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks | QFileDialog.ReadOnly)
        self.ui.txtPath.setText(directory)
    
    def btnOK_clicked(self):
        SettingsSave()
        directory = self.ui.txtPath.text()
        setPicture(directory)
        window.stop()
        window.start()
        self.hide()
        
        
def getRandomPicture(path):
    files = os.listdir(path)
    files_jpg = searchFilesRecursively(path,"*.jpg")
    files_png = searchFilesRecursively(path,"*.png")
    pictures = files_jpg+files_png
    
    index = random.randrange(0, len(pictures))
    return str(pictures[index])
    
def searchFilesRecursively(path,mask):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, mask):
            matches.append(os.path.join(root, filename))
    return (matches)
    
def setPicture(directory):
    picture = QtGui.QPixmap(getRandomPicture(directory)).scaled(SizeX,SizeY,QtCore.Qt.KeepAspectRatio)
    window.ui.Viewer.setPixmap(picture)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(True)
    window = Window()
    window.show()
    settings = Settings()
    if (SettingsExist()):
        settings.hide()
    else:
        settings.show()
    window.start()
    sys.exit(app.exec_())
