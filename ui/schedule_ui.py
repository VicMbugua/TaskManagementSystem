# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\VicMbugua\Projects\TaskManagementSystem\ui\schedule.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScheduleDialog(object):
    def setupUi(self, ScheduleDialog):
        ScheduleDialog.setObjectName("ScheduleDialog")
        ScheduleDialog.resize(405, 369)
        font = QtGui.QFont()
        font.setPointSize(10)
        ScheduleDialog.setFont(font)
        ScheduleDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ScheduleDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 16)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.task_name = QtWidgets.QLabel(ScheduleDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.task_name.setFont(font)
        self.task_name.setObjectName("task_name")
        self.horizontalLayout_2.addWidget(self.task_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(ScheduleDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.start_date = QtWidgets.QDateEdit(ScheduleDialog)
        self.start_date.setCalendarPopup(True)
        self.start_date.setObjectName("start_date")
        self.horizontalLayout_3.addWidget(self.start_date)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 18)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(ScheduleDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.start_time = QtWidgets.QTimeEdit(ScheduleDialog)
        self.start_time.setObjectName("start_time")
        self.horizontalLayout_4.addWidget(self.start_time)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(ScheduleDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.end_time = QtWidgets.QTimeEdit(ScheduleDialog)
        self.end_time.setObjectName("end_time")
        self.horizontalLayout_4.addWidget(self.end_time)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.repeat = QtWidgets.QCheckBox(ScheduleDialog)
        self.repeat.setObjectName("repeat")
        self.horizontalLayout_6.addWidget(self.repeat)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(ScheduleDialog)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.end_date = QtWidgets.QDateEdit(ScheduleDialog)
        self.end_date.setEnabled(False)
        self.end_date.setCalendarPopup(True)
        self.end_date.setObjectName("end_date")
        self.horizontalLayout_5.addWidget(self.end_date)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(ScheduleDialog)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sunday = QtWidgets.QCheckBox(ScheduleDialog)
        self.sunday.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sunday.sizePolicy().hasHeightForWidth())
        self.sunday.setSizePolicy(sizePolicy)
        self.sunday.setText("")
        self.sunday.setObjectName("sunday")
        self.verticalLayout_2.addWidget(self.sunday, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(ScheduleDialog)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.monday = QtWidgets.QCheckBox(ScheduleDialog)
        self.monday.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monday.sizePolicy().hasHeightForWidth())
        self.monday.setSizePolicy(sizePolicy)
        self.monday.setText("")
        self.monday.setChecked(True)
        self.monday.setObjectName("monday")
        self.verticalLayout_3.addWidget(self.monday, 0, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(ScheduleDialog)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tuesday = QtWidgets.QCheckBox(ScheduleDialog)
        self.tuesday.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tuesday.sizePolicy().hasHeightForWidth())
        self.tuesday.setSizePolicy(sizePolicy)
        self.tuesday.setText("")
        self.tuesday.setChecked(True)
        self.tuesday.setObjectName("tuesday")
        self.verticalLayout_4.addWidget(self.tuesday, 0, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(ScheduleDialog)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.wednesday = QtWidgets.QCheckBox(ScheduleDialog)
        self.wednesday.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wednesday.sizePolicy().hasHeightForWidth())
        self.wednesday.setSizePolicy(sizePolicy)
        self.wednesday.setText("")
        self.wednesday.setChecked(True)
        self.wednesday.setObjectName("wednesday")
        self.verticalLayout_5.addWidget(self.wednesday, 0, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(ScheduleDialog)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.thursday = QtWidgets.QCheckBox(ScheduleDialog)
        self.thursday.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thursday.sizePolicy().hasHeightForWidth())
        self.thursday.setSizePolicy(sizePolicy)
        self.thursday.setText("")
        self.thursday.setChecked(True)
        self.thursday.setObjectName("thursday")
        self.verticalLayout_6.addWidget(self.thursday, 0, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(ScheduleDialog)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.friday = QtWidgets.QCheckBox(ScheduleDialog)
        self.friday.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.friday.sizePolicy().hasHeightForWidth())
        self.friday.setSizePolicy(sizePolicy)
        self.friday.setText("")
        self.friday.setChecked(True)
        self.friday.setObjectName("friday")
        self.verticalLayout_7.addWidget(self.friday, 0, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(ScheduleDialog)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.saturday = QtWidgets.QCheckBox(ScheduleDialog)
        self.saturday.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saturday.sizePolicy().hasHeightForWidth())
        self.saturday.setSizePolicy(sizePolicy)
        self.saturday.setText("")
        self.saturday.setObjectName("saturday")
        self.verticalLayout_8.addWidget(self.saturday, 0, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(ScheduleDialog)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.save_btn = QtWidgets.QPushButton(ScheduleDialog)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_8.addWidget(self.save_btn)
        self.cancel_btn = QtWidgets.QPushButton(ScheduleDialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_8.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(ScheduleDialog)
        QtCore.QMetaObject.connectSlotsByName(ScheduleDialog)

    def retranslateUi(self, ScheduleDialog):
        _translate = QtCore.QCoreApplication.translate
        ScheduleDialog.setWindowTitle(_translate("ScheduleDialog", "Schedule Task"))
        self.task_name.setText(_translate("ScheduleDialog", "Schedule task name"))
        self.label_2.setText(_translate("ScheduleDialog", "Date:"))
        self.label_4.setText(_translate("ScheduleDialog", "Start time:"))
        self.label_5.setText(_translate("ScheduleDialog", "End time:"))
        self.repeat.setText(_translate("ScheduleDialog", "Repeat"))
        self.label_13.setText(_translate("ScheduleDialog", "End date:"))
        self.label_14.setText(_translate("ScheduleDialog", "Repeat days:"))
        self.label_6.setText(_translate("ScheduleDialog", "Sun"))
        self.label_7.setText(_translate("ScheduleDialog", "Mon"))
        self.label_8.setText(_translate("ScheduleDialog", "Tue"))
        self.label_9.setText(_translate("ScheduleDialog", "Wed"))
        self.label_10.setText(_translate("ScheduleDialog", "Thu"))
        self.label_11.setText(_translate("ScheduleDialog", "Fri"))
        self.label_12.setText(_translate("ScheduleDialog", "Sat"))
        self.save_btn.setText(_translate("ScheduleDialog", "Save"))
        self.cancel_btn.setText(_translate("ScheduleDialog", "Cancel"))
