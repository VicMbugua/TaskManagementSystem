# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\VicMbugua\Projects\TaskManagementSystem\resources\interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 24))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu_btn = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/134216_menu_lines_hamburger_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setCheckable(False)
        self.menu_btn.setAutoRepeat(False)
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_4.addWidget(self.menu_btn)
        self.menu_label = QtWidgets.QLabel(self.widget_4)
        self.menu_label.setObjectName("menu_label")
        self.horizontalLayout_4.addWidget(self.menu_label)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icons_only_widget = QtWidgets.QWidget(self.widget_2)
        self.icons_only_widget.setStyleSheet("")
        self.icons_only_widget.setObjectName("icons_only_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.icons_only_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.home_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/216242_home_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_1.setIcon(icon1)
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout_2.addWidget(self.home_btn_1)
        self.tasks_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.tasks_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/9040503_list_task_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tasks_btn_1.setIcon(icon2)
        self.tasks_btn_1.setCheckable(True)
        self.tasks_btn_1.setAutoExclusive(True)
        self.tasks_btn_1.setObjectName("tasks_btn_1")
        self.verticalLayout_2.addWidget(self.tasks_btn_1)
        self.completed_tasks_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.completed_tasks_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/9104111_list_checklist_done_complete_task_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.completed_tasks_btn_1.setIcon(icon3)
        self.completed_tasks_btn_1.setCheckable(True)
        self.completed_tasks_btn_1.setAutoExclusive(True)
        self.completed_tasks_btn_1.setObjectName("completed_tasks_btn_1")
        self.verticalLayout_2.addWidget(self.completed_tasks_btn_1)
        self.calendar_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.calendar_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/290104_calendar_clock_date_event_schedule_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calendar_btn_1.setIcon(icon4)
        self.calendar_btn_1.setCheckable(True)
        self.calendar_btn_1.setAutoExclusive(True)
        self.calendar_btn_1.setObjectName("calendar_btn_1")
        self.verticalLayout_2.addWidget(self.calendar_btn_1)
        spacerItem = QtWidgets.QSpacerItem(20, 325, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.exit_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/211650_close_circled_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_2.addWidget(self.exit_btn_1)
        self.horizontalLayout.addWidget(self.icons_only_widget)
        self.full_name_widget = QtWidgets.QWidget(self.widget_2)
        self.full_name_widget.setObjectName("full_name_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.full_name_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.home_btn_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout.addWidget(self.home_btn_2)
        self.tasks_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.tasks_btn_2.setIcon(icon2)
        self.tasks_btn_2.setCheckable(True)
        self.tasks_btn_2.setAutoExclusive(True)
        self.tasks_btn_2.setObjectName("tasks_btn_2")
        self.verticalLayout.addWidget(self.tasks_btn_2)
        self.completed_tasks_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.completed_tasks_btn_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.completed_tasks_btn_2.setIcon(icon3)
        self.completed_tasks_btn_2.setCheckable(True)
        self.completed_tasks_btn_2.setAutoExclusive(True)
        self.completed_tasks_btn_2.setObjectName("completed_tasks_btn_2")
        self.verticalLayout.addWidget(self.completed_tasks_btn_2)
        self.calendar_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.calendar_btn_2.setIcon(icon4)
        self.calendar_btn_2.setCheckable(True)
        self.calendar_btn_2.setAutoExclusive(True)
        self.calendar_btn_2.setObjectName("calendar_btn_2")
        self.verticalLayout.addWidget(self.calendar_btn_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 325, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout.addWidget(self.exit_btn_2)
        self.horizontalLayout.addWidget(self.full_name_widget)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.header_widget = QtWidgets.QWidget(self.widget)
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.header_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.user_btn = QtWidgets.QPushButton(self.header_widget)
        self.user_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icons/1564534_customer_man_user_account_profile_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon6)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_3.addWidget(self.user_btn)
        self.verticalLayout_4.addWidget(self.header_widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.no_of_tasks = QtWidgets.QLabel(self.home_page)
        self.no_of_tasks.setGeometry(QtCore.QRect(240, 30, 281, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.no_of_tasks.setFont(font)
        self.no_of_tasks.setText("")
        self.no_of_tasks.setObjectName("no_of_tasks")
        self.stackedWidget.addWidget(self.home_page)
        self.tasks_page = QtWidgets.QWidget()
        self.tasks_page.setObjectName("tasks_page")
        self.tasks_list = QtWidgets.QTableView(self.tasks_page)
        self.tasks_list.setGeometry(QtCore.QRect(10, 130, 551, 341))
        self.tasks_list.setAlternatingRowColors(True)
        self.tasks_list.setObjectName("tasks_list")
        self.add_task_btn = QtWidgets.QPushButton(self.tasks_page)
        self.add_task_btn.setGeometry(QtCore.QRect(390, 60, 75, 23))
        self.add_task_btn.setObjectName("add_task_btn")
        self.stackedWidget.addWidget(self.tasks_page)
        self.completed_tasks_page = QtWidgets.QWidget()
        self.completed_tasks_page.setObjectName("completed_tasks_page")
        self.completed_tasks = QtWidgets.QTableView(self.completed_tasks_page)
        self.completed_tasks.setGeometry(QtCore.QRect(35, 111, 491, 331))
        self.completed_tasks.setObjectName("completed_tasks")
        self.stackedWidget.addWidget(self.completed_tasks_page)
        self.calendar_page = QtWidgets.QWidget()
        self.calendar_page.setObjectName("calendar_page")
        self.label_7 = QtWidgets.QLabel(self.calendar_page)
        self.label_7.setGeometry(QtCore.QRect(210, 200, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.calendar_page)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.tasks_btn_1.toggled['bool'].connect(self.tasks_btn_2.setChecked) # type: ignore
        self.completed_tasks_btn_1.toggled['bool'].connect(self.completed_tasks_btn_2.setChecked) # type: ignore
        self.calendar_btn_1.toggled['bool'].connect(self.calendar_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.tasks_btn_2.toggled['bool'].connect(self.tasks_btn_1.setChecked) # type: ignore
        self.completed_tasks_btn_2.toggled['bool'].connect(self.completed_tasks_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        self.calendar_btn_2.toggled['bool'].connect(self.calendar_btn_1.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Menu</p></body></html>"))
        self.menu_label.setText(_translate("MainWindow", "MENU"))
        self.home_btn_1.setToolTip(_translate("MainWindow", "Home"))
        self.tasks_btn_1.setToolTip(_translate("MainWindow", "Tasks"))
        self.completed_tasks_btn_1.setToolTip(_translate("MainWindow", "Completed Tasks"))
        self.calendar_btn_1.setToolTip(_translate("MainWindow", "<html><head/><body><p>Calendar</p></body></html>"))
        self.exit_btn_1.setToolTip(_translate("MainWindow", "Exit"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.tasks_btn_2.setText(_translate("MainWindow", "Tasks"))
        self.tasks_btn_2.setShortcut(_translate("MainWindow", "Alt+T"))
        self.completed_tasks_btn_2.setText(_translate("MainWindow", "Completed Tasks"))
        self.calendar_btn_2.setText(_translate("MainWindow", "Calendar"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "TASK MANAGEMENT SYSTEM"))
        self.user_btn.setToolTip(_translate("MainWindow", "User"))
        self.add_task_btn.setText(_translate("MainWindow", "Add Task"))
        self.label_7.setText(_translate("MainWindow", "CALENDAR PAGE"))
import ui.resources_rc as resources_rc