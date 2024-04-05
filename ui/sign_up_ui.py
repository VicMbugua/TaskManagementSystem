# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\VicMbugua\Projects\TaskManagementSystem\ui\sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(356, 304)
        self.centralwidget = QtWidgets.QWidget(SignUp)
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
        spacerItem = QtWidgets.QSpacerItem(5, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(115, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(115, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.view_password_btn = QtWidgets.QPushButton(self.centralwidget)
        self.view_password_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.view_password_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\VicMbugua\\Projects\\TaskManagementSystem\\ui\\../icons/hidden_eye_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_password_btn.setIcon(icon)
        self.view_password_btn.setAutoDefault(True)
        self.view_password_btn.setObjectName("view_password_btn")
        self.horizontalLayout_3.addWidget(self.view_password_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(115, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.confirm_password = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setClearButtonEnabled(False)
        self.confirm_password.setObjectName("confirm_password")
        self.horizontalLayout_4.addWidget(self.confirm_password)
        self.view_password_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.view_password_btn_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.view_password_btn_2.setText("")
        self.view_password_btn_2.setIcon(icon)
        self.view_password_btn_2.setAutoDefault(True)
        self.view_password_btn_2.setObjectName("view_password_btn_2")
        self.horizontalLayout_4.addWidget(self.view_password_btn_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.error_message = QtWidgets.QLabel(self.centralwidget)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.sign_up_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.sign_up_btn.setAutoDefault(True)
        self.sign_up_btn.setObjectName("sign_up_btn")
        self.verticalLayout.addWidget(self.sign_up_btn)
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.login_btn.setAutoDefault(True)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        SignUp.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignUp)
        self.username.returnPressed.connect(self.password.setFocus) # type: ignore
        self.password.returnPressed.connect(self.confirm_password.setFocus) # type: ignore
        self.confirm_password.returnPressed.connect(self.sign_up_btn.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SignUp)
        SignUp.setTabOrder(self.username, self.password)
        SignUp.setTabOrder(self.password, self.confirm_password)
        SignUp.setTabOrder(self.confirm_password, self.sign_up_btn)
        SignUp.setTabOrder(self.sign_up_btn, self.login_btn)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Sign Up"))
        self.label.setText(_translate("SignUp", "Sign Up"))
        self.label_2.setText(_translate("SignUp", "Username:"))
        self.username.setToolTip(_translate("SignUp", "<html><head/><body><p>Username must start with a letter and contain only letters, numbers, or underscores.</p></body></html>"))
        self.username.setPlaceholderText(_translate("SignUp", "Username"))
        self.label_3.setText(_translate("SignUp", "Password:"))
        self.password.setPlaceholderText(_translate("SignUp", "Password"))
        self.view_password_btn.setToolTip(_translate("SignUp", "View Password"))
        self.label_4.setText(_translate("SignUp", "Confirm Password:"))
        self.confirm_password.setPlaceholderText(_translate("SignUp", "Confirm Password"))
        self.view_password_btn_2.setToolTip(_translate("SignUp", "View Password"))
        self.error_message.setText(_translate("SignUp", "Error message"))
        self.caps_lock.setText(_translate("SignUp", "Cap locks"))
        self.sign_up_btn.setText(_translate("SignUp", "Sign Up"))
        self.sign_up_btn.setProperty("groupName", _translate("SignUp", "top_login"))
        self.login_btn.setText(_translate("SignUp", "Login"))
        self.login_btn.setProperty("groupName", _translate("SignUp", "bottom_login"))
