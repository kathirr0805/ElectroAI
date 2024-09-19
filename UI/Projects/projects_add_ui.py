# projects_add_ui.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Project Name
        self.projectNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.verticalLayout.addWidget(self.projectNameLabel)
        self.projectNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.projectNameLineEdit.setObjectName("projectNameLineEdit")
        self.verticalLayout.addWidget(self.projectNameLineEdit)

        # Components
        self.componentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.componentsLabel.setObjectName("componentsLabel")
        self.verticalLayout.addWidget(self.componentsLabel)
        self.componentsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.componentsLineEdit.setObjectName("componentsLineEdit")
        self.verticalLayout.addWidget(self.componentsLineEdit)

        # Connection
        self.connectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.connectionLabel.setObjectName("connectionLabel")
        self.verticalLayout.addWidget(self.connectionLabel)
        self.connectionTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.connectionTextEdit.setObjectName("connectionTextEdit")
        self.verticalLayout.addWidget(self.connectionTextEdit)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Project"))
        self.projectNameLabel.setText(_translate("MainWindow", "Project Name:"))
        self.componentsLabel.setText(_translate("MainWindow", "Components (comma-separated):"))
        self.connectionLabel.setText(_translate("MainWindow", "Connection Details:"))
        self.submitButton.setText(_translate("MainWindow", "Add Project"))
