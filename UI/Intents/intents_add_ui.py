# intents_add_ui.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Intent Name
        self.intentNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.intentNameLabel.setObjectName("intentNameLabel")
        self.verticalLayout.addWidget(self.intentNameLabel)
        self.intentNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.intentNameLineEdit.setObjectName("intentNameLineEdit")
        self.verticalLayout.addWidget(self.intentNameLineEdit)

        # Pattern
        self.patternLabel = QtWidgets.QLabel(self.centralwidget)
        self.patternLabel.setObjectName("patternLabel")
        self.verticalLayout.addWidget(self.patternLabel)
        self.patternLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.patternLineEdit.setObjectName("patternLineEdit")
        self.verticalLayout.addWidget(self.patternLineEdit)

        # Response
        self.responseLabel = QtWidgets.QLabel(self.centralwidget)
        self.responseLabel.setObjectName("responseLabel")
        self.verticalLayout.addWidget(self.responseLabel)
        self.responseLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.responseLineEdit.setObjectName("responseLineEdit")
        self.verticalLayout.addWidget(self.responseLineEdit)

        # Submit Button
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout.addWidget(self.submitButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Intent"))
        self.intentNameLabel.setText(_translate("MainWindow", "Intent Name:"))
        self.patternLabel.setText(_translate("MainWindow", "Pattern:"))
        self.responseLabel.setText(_translate("MainWindow", "Response:"))
        self.submitButton.setText(_translate("MainWindow", "Add Intent"))
