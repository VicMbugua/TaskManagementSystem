# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\VicMbugua\Projects\TaskManagementSystem\ui\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(360, 281)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LogIn.sizePolicy().hasHeightForWidth())
        LogIn.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(LogIn)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QtCore.QSize(150, 20))
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        spacerItem1 = QtWidgets.QSpacerItem(108, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QtCore.QSize(150, 20))
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        spacerItem2 = QtWidgets.QSpacerItem(88, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.error_message = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.error_message.sizePolicy().hasHeightForWidth())
        self.error_message.setSizePolicy(sizePolicy)
        self.error_message.setMinimumSize(QtCore.QSize(0, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.error_message.setFont(font)
        self.error_message.setStyleSheet("color: red;")
        self.error_message.setAlignment(QtCore.Qt.AlignCenter)
        self.error_message.setObjectName("error_message")
        self.verticalLayout.addWidget(self.error_message)
        self.caps_lock = QtWidgets.QLabel(self.centralwidget)
        self.caps_lock.setAlignment(QtCore.Qt.AlignCenter)
        self.caps_lock.setObjectName("caps_lock")
        self.verticalLayout.addWidget(self.caps_lock)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.login_btn.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(41, 99, 224);\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 255);\n"
"color: black;\n"
"}")
        self.login_btn.setAutoDefault(True)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.sign_up_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_btn.setMinimumSize(QtCore.QSize(65, 20))
        self.sign_up_btn.setStyleSheet("QPushButton{\n"
"border: 1px solid rgb(41, 99, 224);\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 255, 255);\n"
"color: black;\n"
"border: none;\n"
"}")
        self.sign_up_btn.setAutoDefault(True)
        self.sign_up_btn.setObjectName("sign_up_btn")
        self.verticalLayout.addWidget(self.sign_up_btn)
        LogIn.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogIn)
        self.password.returnPressed.connect(self.login_btn.click) # type: ignore
        self.username.returnPressed.connect(self.password.setFocus) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Welcome"))
        self.label.setText(_translate("LogIn", "Welcome"))
        self.label_2.setText(_translate("LogIn", "Username:"))
        self.username.setToolTip(_translate("LogIn", "<html><head/><body><p>Username must start with a letter and contain only letters, numbers, or underscores.</p></body></html>"))
        self.username.setPlaceholderText(_translate("LogIn", "Username"))
        self.label_3.setText(_translate("LogIn", "Password:"))
        self.password.setPlaceholderText(_translate("LogIn", "Password"))
        self.error_message.setText(_translate("LogIn", "Error message"))
        self.caps_lock.setText(_translate("LogIn", "Cap locks"))
        self.login_btn.setText(_translate("LogIn", "Login"))
        self.sign_up_btn.setToolTip(_translate("LogIn", "<html><head/><body><p>Create a new account.</p></body></html>"))
        self.sign_up_btn.setText(_translate("LogIn", "Sign Up"))
