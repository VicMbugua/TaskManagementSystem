# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\VicMbugua\Projects\TaskManagementSystem\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 468)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/9054813_bx_task_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.navbar_widget = QtWidgets.QWidget(self.centralwidget)
        self.navbar_widget.setObjectName("navbar_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.navbar_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.navbar_widget)
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
        self.menu_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.menu_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/134216_menu_lines_hamburger_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon1)
        self.menu_btn.setAutoDefault(True)
        self.menu_btn.setProperty("groupName", "")
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_4.addWidget(self.menu_btn)
        self.menu_label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu_label.setFont(font)
        self.menu_label.setObjectName("menu_label")
        self.horizontalLayout_4.addWidget(self.menu_label)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.navbar_widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icons_only_widget = QtWidgets.QWidget(self.widget_2)
        self.icons_only_widget.setObjectName("icons_only_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.icons_only_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.home_btn_1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.home_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/216242_home_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_1.setIcon(icon2)
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setAutoDefault(True)
        self.home_btn_1.setProperty("groupName", "")
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout_2.addWidget(self.home_btn_1)
        self.tasks_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.tasks_btn_1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tasks_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/9104111_list_checklist_done_complete_task_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tasks_btn_1.setIcon(icon3)
        self.tasks_btn_1.setCheckable(True)
        self.tasks_btn_1.setAutoExclusive(True)
        self.tasks_btn_1.setAutoDefault(True)
        self.tasks_btn_1.setProperty("groupName", "")
        self.tasks_btn_1.setObjectName("tasks_btn_1")
        self.verticalLayout_2.addWidget(self.tasks_btn_1)
        self.completed_tasks_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.completed_tasks_btn_1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.completed_tasks_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/9040503_list_task_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.completed_tasks_btn_1.setIcon(icon4)
        self.completed_tasks_btn_1.setCheckable(True)
        self.completed_tasks_btn_1.setAutoExclusive(True)
        self.completed_tasks_btn_1.setAutoDefault(True)
        self.completed_tasks_btn_1.setProperty("groupName", "")
        self.completed_tasks_btn_1.setObjectName("completed_tasks_btn_1")
        self.verticalLayout_2.addWidget(self.completed_tasks_btn_1)
        self.calendar_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.calendar_btn_1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.calendar_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/290104_calendar_clock_date_event_schedule_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calendar_btn_1.setIcon(icon5)
        self.calendar_btn_1.setCheckable(True)
        self.calendar_btn_1.setAutoExclusive(True)
        self.calendar_btn_1.setAutoDefault(True)
        self.calendar_btn_1.setProperty("groupName", "")
        self.calendar_btn_1.setObjectName("calendar_btn_1")
        self.verticalLayout_2.addWidget(self.calendar_btn_1)
        spacerItem = QtWidgets.QSpacerItem(20, 325, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icons_only_widget)
        self.exit_btn_1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.exit_btn_1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/211650_close_circled_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon6)
        self.exit_btn_1.setAutoDefault(True)
        self.exit_btn_1.setProperty("groupName", "")
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_2.addWidget(self.exit_btn_1)
        self.horizontalLayout.addWidget(self.icons_only_widget)
        self.full_name_widget = QtWidgets.QWidget(self.widget_2)
        self.full_name_widget.setMinimumSize(QtCore.QSize(125, 0))
        self.full_name_widget.setObjectName("full_name_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.full_name_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.home_btn_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.home_btn_2.setIcon(icon2)
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setAutoDefault(True)
        self.home_btn_2.setProperty("groupName", "")
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout.addWidget(self.home_btn_2)
        self.tasks_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.tasks_btn_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tasks_btn_2.setIcon(icon3)
        self.tasks_btn_2.setCheckable(True)
        self.tasks_btn_2.setAutoExclusive(True)
        self.tasks_btn_2.setAutoDefault(True)
        self.tasks_btn_2.setProperty("groupName", "")
        self.tasks_btn_2.setObjectName("tasks_btn_2")
        self.verticalLayout.addWidget(self.tasks_btn_2)
        self.completed_tasks_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.completed_tasks_btn_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.completed_tasks_btn_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.completed_tasks_btn_2.setIcon(icon4)
        self.completed_tasks_btn_2.setCheckable(True)
        self.completed_tasks_btn_2.setAutoExclusive(True)
        self.completed_tasks_btn_2.setAutoDefault(True)
        self.completed_tasks_btn_2.setProperty("groupName", "")
        self.completed_tasks_btn_2.setObjectName("completed_tasks_btn_2")
        self.verticalLayout.addWidget(self.completed_tasks_btn_2)
        self.calendar_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.calendar_btn_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.calendar_btn_2.setIcon(icon5)
        self.calendar_btn_2.setCheckable(True)
        self.calendar_btn_2.setAutoExclusive(True)
        self.calendar_btn_2.setAutoDefault(True)
        self.calendar_btn_2.setProperty("groupName", "")
        self.calendar_btn_2.setObjectName("calendar_btn_2")
        self.verticalLayout.addWidget(self.calendar_btn_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 325, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_name_widget)
        self.exit_btn_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.exit_btn_2.setIcon(icon6)
        self.exit_btn_2.setAutoDefault(True)
        self.exit_btn_2.setProperty("groupName", "")
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout.addWidget(self.exit_btn_2)
        self.horizontalLayout.addWidget(self.full_name_widget)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.horizontalLayout_6.addWidget(self.navbar_widget)
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
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.search_btn = QtWidgets.QPushButton(self.header_widget)
        self.search_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.search_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/3844432_magnifier_search_zoom_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon7)
        self.search_btn.setAutoDefault(True)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        self.user_btn = QtWidgets.QPushButton(self.header_widget)
        self.user_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.user_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/1564534_customer_man_user_account_profile_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon8)
        self.user_btn.setAutoDefault(True)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_3.addWidget(self.user_btn)
        self.verticalLayout_4.addWidget(self.header_widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setProperty("groupName", "")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.no_of_tasks = QtWidgets.QLabel(self.home_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_of_tasks.sizePolicy().hasHeightForWidth())
        self.no_of_tasks.setSizePolicy(sizePolicy)
        self.no_of_tasks.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.no_of_tasks.setFont(font)
        self.no_of_tasks.setObjectName("no_of_tasks")
        self.horizontalLayout_8.addWidget(self.no_of_tasks)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.no_of_overdue_tasks = QtWidgets.QLabel(self.home_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_of_overdue_tasks.sizePolicy().hasHeightForWidth())
        self.no_of_overdue_tasks.setSizePolicy(sizePolicy)
        self.no_of_overdue_tasks.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.no_of_overdue_tasks.setFont(font)
        self.no_of_overdue_tasks.setObjectName("no_of_overdue_tasks")
        self.horizontalLayout_12.addWidget(self.no_of_overdue_tasks)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.home_page)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.filtered_tasks = QtWidgets.QTableView(self.home_page)
        self.filtered_tasks.setFocusPolicy(QtCore.Qt.TabFocus)
        self.filtered_tasks.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filtered_tasks.setTabKeyNavigation(False)
        self.filtered_tasks.setAlternatingRowColors(True)
        self.filtered_tasks.setShowGrid(False)
        self.filtered_tasks.setObjectName("filtered_tasks")
        self.verticalLayout_7.addWidget(self.filtered_tasks)
        self.stackedWidget.addWidget(self.home_page)
        self.tasks_page = QtWidgets.QWidget()
        self.tasks_page.setObjectName("tasks_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tasks_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_8 = QtWidgets.QWidget(self.tasks_page)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.project = QtWidgets.QComboBox(self.widget_8)
        self.project.setObjectName("project")
        self.horizontalLayout_9.addWidget(self.project)
        spacerItem6 = QtWidgets.QSpacerItem(175, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.add_project_btn = QtWidgets.QPushButton(self.widget_8)
        self.add_project_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.add_project_btn.setAutoDefault(True)
        self.add_project_btn.setObjectName("add_project_btn")
        self.horizontalLayout_9.addWidget(self.add_project_btn)
        self.manage_project_btn = QtWidgets.QPushButton(self.widget_8)
        self.manage_project_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.manage_project_btn.setAutoDefault(True)
        self.manage_project_btn.setObjectName("manage_project_btn")
        self.horizontalLayout_9.addWidget(self.manage_project_btn)
        self.verticalLayout_5.addWidget(self.widget_8)
        self.widget_6 = QtWidgets.QWidget(self.tasks_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(448, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.tasks_list = QtWidgets.QTableView(self.tasks_page)
        self.tasks_list.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tasks_list.setTabKeyNavigation(False)
        self.tasks_list.setAlternatingRowColors(True)
        self.tasks_list.setShowGrid(False)
        self.tasks_list.setObjectName("tasks_list")
        self.verticalLayout_5.addWidget(self.tasks_list)
        self.widget_5 = QtWidgets.QWidget(self.tasks_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(463, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.add_task_btn = QtWidgets.QPushButton(self.widget_5)
        self.add_task_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.add_task_btn.setAutoDefault(True)
        self.add_task_btn.setObjectName("add_task_btn")
        self.horizontalLayout_5.addWidget(self.add_task_btn)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.stackedWidget.addWidget(self.tasks_page)
        self.completed_tasks_page = QtWidgets.QWidget()
        self.completed_tasks_page.setObjectName("completed_tasks_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.completed_tasks_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.number_of_completed_tasks = QtWidgets.QLabel(self.completed_tasks_page)
        self.number_of_completed_tasks.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.number_of_completed_tasks.setFont(font)
        self.number_of_completed_tasks.setObjectName("number_of_completed_tasks")
        self.horizontalLayout_15.addWidget(self.number_of_completed_tasks)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.completed_tasks_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem10 = QtWidgets.QSpacerItem(401, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.completed_tasks = QtWidgets.QTableView(self.completed_tasks_page)
        self.completed_tasks.setFocusPolicy(QtCore.Qt.TabFocus)
        self.completed_tasks.setTabKeyNavigation(False)
        self.completed_tasks.setAlternatingRowColors(True)
        self.completed_tasks.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.completed_tasks.setShowGrid(False)
        self.completed_tasks.setObjectName("completed_tasks")
        self.verticalLayout_6.addWidget(self.completed_tasks)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem11)
        self.clear_all_btn = QtWidgets.QPushButton(self.completed_tasks_page)
        self.clear_all_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.clear_all_btn.setAutoDefault(True)
        self.clear_all_btn.setObjectName("clear_all_btn")
        self.horizontalLayout_14.addWidget(self.clear_all_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.stackedWidget.addWidget(self.completed_tasks_page)
        self.calendar_page = QtWidgets.QWidget()
        self.calendar_page.setObjectName("calendar_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.calendar_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.calendar_page)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.calendar = QtWidgets.QCalendarWidget(self.calendar_page)
        self.calendar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calendar.setObjectName("calendar")
        self.verticalLayout_8.addWidget(self.calendar)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 8, -1, 2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.schedules_for = QtWidgets.QLabel(self.calendar_page)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.schedules_for.setFont(font)
        self.schedules_for.setObjectName("schedules_for")
        self.horizontalLayout_10.addWidget(self.schedules_for)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.calendar_table = QtWidgets.QTableView(self.calendar_page)
        self.calendar_table.setFocusPolicy(QtCore.Qt.TabFocus)
        self.calendar_table.setObjectName("calendar_table")
        self.verticalLayout_8.addWidget(self.calendar_table)
        self.stackedWidget.addWidget(self.calendar_page)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_6.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
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
        MainWindow.setTabOrder(self.menu_btn, self.search_btn)
        MainWindow.setTabOrder(self.search_btn, self.user_btn)
        MainWindow.setTabOrder(self.user_btn, self.home_btn_1)
        MainWindow.setTabOrder(self.home_btn_1, self.tasks_btn_1)
        MainWindow.setTabOrder(self.tasks_btn_1, self.completed_tasks_btn_1)
        MainWindow.setTabOrder(self.completed_tasks_btn_1, self.calendar_btn_1)
        MainWindow.setTabOrder(self.calendar_btn_1, self.exit_btn_1)
        MainWindow.setTabOrder(self.exit_btn_1, self.home_btn_2)
        MainWindow.setTabOrder(self.home_btn_2, self.tasks_btn_2)
        MainWindow.setTabOrder(self.tasks_btn_2, self.completed_tasks_btn_2)
        MainWindow.setTabOrder(self.completed_tasks_btn_2, self.calendar_btn_2)
        MainWindow.setTabOrder(self.calendar_btn_2, self.exit_btn_2)
        MainWindow.setTabOrder(self.exit_btn_2, self.filtered_tasks)
        MainWindow.setTabOrder(self.filtered_tasks, self.project)
        MainWindow.setTabOrder(self.project, self.add_project_btn)
        MainWindow.setTabOrder(self.add_project_btn, self.manage_project_btn)
        MainWindow.setTabOrder(self.manage_project_btn, self.tasks_list)
        MainWindow.setTabOrder(self.tasks_list, self.add_task_btn)
        MainWindow.setTabOrder(self.add_task_btn, self.completed_tasks)
        MainWindow.setTabOrder(self.completed_tasks, self.clear_all_btn)
        MainWindow.setTabOrder(self.clear_all_btn, self.calendar)
        MainWindow.setTabOrder(self.calendar, self.calendar_table)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task Management System"))
        self.menu_btn.setToolTip(_translate("MainWindow", "Collapse menu"))
        self.menu_btn.setShortcut(_translate("MainWindow", "Alt+M"))
        self.menu_label.setText(_translate("MainWindow", "MENU"))
        self.home_btn_1.setToolTip(_translate("MainWindow", "Home (Alt+H)"))
        self.home_btn_1.setShortcut(_translate("MainWindow", "Alt+H"))
        self.tasks_btn_1.setToolTip(_translate("MainWindow", "Tasks (Alt+T)"))
        self.tasks_btn_1.setShortcut(_translate("MainWindow", "Alt+T"))
        self.completed_tasks_btn_1.setToolTip(_translate("MainWindow", "Completed Tasks (Alt+C)"))
        self.completed_tasks_btn_1.setShortcut(_translate("MainWindow", "Alt+C"))
        self.calendar_btn_1.setToolTip(_translate("MainWindow", "Calendar (Alt+L)"))
        self.calendar_btn_1.setShortcut(_translate("MainWindow", "Alt+L"))
        self.exit_btn_1.setToolTip(_translate("MainWindow", "Exit"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.home_btn_2.setShortcut(_translate("MainWindow", "Alt+H"))
        self.tasks_btn_2.setText(_translate("MainWindow", "Tasks"))
        self.tasks_btn_2.setShortcut(_translate("MainWindow", "Alt+T"))
        self.completed_tasks_btn_2.setText(_translate("MainWindow", "Completed Tasks"))
        self.completed_tasks_btn_2.setShortcut(_translate("MainWindow", "Alt+C"))
        self.calendar_btn_2.setText(_translate("MainWindow", "Calendar"))
        self.calendar_btn_2.setShortcut(_translate("MainWindow", "Alt+L"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "TASK MANAGEMENT SYSTEM"))
        self.search_btn.setToolTip(_translate("MainWindow", "Search for tasks"))
        self.search_btn.setProperty("groupName", _translate("MainWindow", "top_buttons"))
        self.user_btn.setToolTip(_translate("MainWindow", "Click to see user options"))
        self.user_btn.setProperty("groupName", _translate("MainWindow", "top_buttons"))
        self.no_of_tasks.setText(_translate("MainWindow", "Number of tasks"))
        self.no_of_overdue_tasks.setText(_translate("MainWindow", "Number of overdue tasks"))
        self.label_6.setText(_translate("MainWindow", "Recommended tasks"))
        self.label_5.setText(_translate("MainWindow", "Choose project:"))
        self.project.setToolTip(_translate("MainWindow", "Click to see other projects"))
        self.add_project_btn.setText(_translate("MainWindow", "Add Project"))
        self.add_project_btn.setProperty("groupName", _translate("MainWindow", "project_buttons"))
        self.manage_project_btn.setText(_translate("MainWindow", "Manage Project"))
        self.manage_project_btn.setProperty("groupName", _translate("MainWindow", "project_buttons"))
        self.label.setText(_translate("MainWindow", "Tasks List"))
        self.add_task_btn.setText(_translate("MainWindow", "Add Task"))
        self.add_task_btn.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.add_task_btn.setProperty("groupName", _translate("MainWindow", "common_buttons"))
        self.number_of_completed_tasks.setText(_translate("MainWindow", "Number of Completed Tasks"))
        self.label_2.setText(_translate("MainWindow", "Completed Tasks"))
        self.clear_all_btn.setToolTip(_translate("MainWindow", "Delete all completed tasks"))
        self.clear_all_btn.setText(_translate("MainWindow", "Clear All"))
        self.clear_all_btn.setProperty("groupName", _translate("MainWindow", "cancel_buttons"))
        self.label_4.setText(_translate("MainWindow", "Calendar View"))
        self.calendar.setToolTip(_translate("MainWindow", "Click to see tasks scheduled for this date"))
        self.schedules_for.setText(_translate("MainWindow", "Schedules on this day"))
import ui.resources_rc
