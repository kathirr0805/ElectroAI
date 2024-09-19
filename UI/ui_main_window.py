# ui_main_window.py

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QRadioButton, QTextEdit, QVBoxLayout, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Radio Buttons for Chat and Voice Command
        self.radioChat = QtWidgets.QRadioButton(self.centralwidget)
        self.radioChat.setObjectName("radioChat")
        self.radioChat.setText("Chat")
        self.verticalLayout.addWidget(self.radioChat)
        
        self.radioVoice = QtWidgets.QRadioButton(self.centralwidget)
        self.radioVoice.setObjectName("radioVoice")
        self.radioVoice.setText("Voice Command")
        self.verticalLayout.addWidget(self.radioVoice)
        
        # Input area for chat
        self.userInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userInput.setObjectName("userInput")
        self.userInput.setPlaceholderText("Enter your message here...")
        self.verticalLayout.addWidget(self.userInput)
        
        # Button to submit chat input
        self.submitChat = QtWidgets.QPushButton(self.centralwidget)
        self.submitChat.setObjectName("submitChat")
        self.submitChat.setText("Submit")
        self.verticalLayout.addWidget(self.submitChat)
        
        # Button for voice command
        self.voiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.voiceButton.setObjectName("voiceButton")
        self.voiceButton.setText("Voice Command")
        self.verticalLayout.addWidget(self.voiceButton)
        
        # Text area for displaying responses
        self.responseDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.responseDisplay.setObjectName("responseDisplay")
        self.responseDisplay.setPlaceholderText("Responses will be displayed here...")
        self.verticalLayout.addWidget(self.responseDisplay)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Electro AI Assistant"))

