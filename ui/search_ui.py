# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\VicMbugua\Projects\TaskManagementSystem\ui\search.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchDialog(object):
    def setupUi(self, SearchDialog):
        SearchDialog.setObjectName("SearchDialog")
        SearchDialog.resize(518, 401)
        font = QtGui.QFont()
        font.setPointSize(10)
        SearchDialog.setFont(font)
        SearchDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SearchDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.task_search = QtWidgets.QLineEdit(SearchDialog)
        self.task_search.setObjectName("task_search")
        self.horizontalLayout.addWidget(self.task_search)
        self.search_btn_2 = QtWidgets.QPushButton(SearchDialog)
        self.search_btn_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.search_btn_2.setObjectName("search_btn_2")
        self.horizontalLayout.addWidget(self.search_btn_2)
        self.show_all_btn = QtWidgets.QPushButton(SearchDialog)
        self.show_all_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.show_all_btn.setObjectName("show_all_btn")
        self.horizontalLayout.addWidget(self.show_all_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(SearchDialog)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.labels = QtWidgets.QComboBox(SearchDialog)
        self.labels.setMinimumSize(QtCore.QSize(90, 0))
        self.labels.setObjectName("labels")
        self.horizontalLayout_2.addWidget(self.labels)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(SearchDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.due_date = QtWidgets.QComboBox(SearchDialog)
        self.due_date.setMinimumSize(QtCore.QSize(90, 0))
        self.due_date.setObjectName("due_date")
        self.due_date.addItem("")
        self.due_date.addItem("")
        self.due_date.addItem("")
        self.horizontalLayout_2.addWidget(self.due_date)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(SearchDialog)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.status = QtWidgets.QComboBox(SearchDialog)
        self.status.setObjectName("status")
        self.status.addItem("")
        self.status.addItem("")
        self.status.addItem("")
        self.horizontalLayout_5.addWidget(self.status)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(SearchDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tasks_list = QtWidgets.QTableView(SearchDialog)
        self.tasks_list.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tasks_list.setTabKeyNavigation(False)
        self.tasks_list.setObjectName("tasks_list")
        self.verticalLayout.addWidget(self.tasks_list)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.cancel_btn = QtWidgets.QPushButton(SearchDialog)
        self.cancel_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SearchDialog)
        self.cancel_btn.clicked.connect(SearchDialog.close) # type: ignore
        self.task_search.returnPressed.connect(self.search_btn_2.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SearchDialog)
        SearchDialog.setTabOrder(self.task_search, self.search_btn_2)
        SearchDialog.setTabOrder(self.search_btn_2, self.show_all_btn)
        SearchDialog.setTabOrder(self.show_all_btn, self.labels)
        SearchDialog.setTabOrder(self.labels, self.due_date)
        SearchDialog.setTabOrder(self.due_date, self.status)
        SearchDialog.setTabOrder(self.status, self.tasks_list)
        SearchDialog.setTabOrder(self.tasks_list, self.cancel_btn)

    def retranslateUi(self, SearchDialog):
        _translate = QtCore.QCoreApplication.translate
        SearchDialog.setWindowTitle(_translate("SearchDialog", "Search"))
        self.label.setText(_translate("SearchDialog", "Search tasks:"))
        self.task_search.setPlaceholderText(_translate("SearchDialog", "Type here to search..."))
        self.search_btn_2.setText(_translate("SearchDialog", "Search"))
        self.search_btn_2.setProperty("groupName", _translate("SearchDialog", "common_buttons"))
        self.show_all_btn.setToolTip(_translate("SearchDialog", "Show all tasks"))
        self.show_all_btn.setText(_translate("SearchDialog", "Show all"))
        self.show_all_btn.setProperty("groupName", _translate("SearchDialog", "common_buttons"))
        self.label_2.setText(_translate("SearchDialog", "Group by Label:"))
        self.label_3.setText(_translate("SearchDialog", "Group by Due Date:"))
        self.due_date.setItemText(0, _translate("SearchDialog", "All"))
        self.due_date.setItemText(1, _translate("SearchDialog", "Passed"))
        self.due_date.setItemText(2, _translate("SearchDialog", "Not Passed"))
        self.label_5.setText(_translate("SearchDialog", "Group by Status:"))
        self.status.setItemText(0, _translate("SearchDialog", "All"))
        self.status.setItemText(1, _translate("SearchDialog", "Started"))
        self.status.setItemText(2, _translate("SearchDialog", "Not Started"))
        self.label_4.setText(_translate("SearchDialog", "Task List:"))
        self.cancel_btn.setText(_translate("SearchDialog", "Cancel"))
        self.cancel_btn.setProperty("groupName", _translate("SearchDialog", "cancel_buttons"))
