# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\bisa-tidor\View.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from course import Course
from coursetime import CourseTime
from courselogic import CourseLogic

class Ui_View(object):
    def setupUi(self, View):
        View.setObjectName("View")
        View.resize(400, 281)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        View.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(View)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.courseCB = QtWidgets.QComboBox(View)
        self.courseCB.setGeometry(QtCore.QRect(100, 140, 241, 22))
        self.courseCB.setObjectName("courseCB")
        self.usernameL = QtWidgets.QLabel(View)
        self.usernameL.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.usernameL.setObjectName("usernameL")
        self.headerL = QtWidgets.QLabel(View)
        self.headerL.setGeometry(QtCore.QRect(140, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.headerL.setFont(font)
        self.headerL.setObjectName("headerL")
        self.passwordL = QtWidgets.QLabel(View)
        self.passwordL.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.passwordL.setObjectName("passwordL")
        self.usernameLE = QtWidgets.QLineEdit(View)
        self.usernameLE.setGeometry(QtCore.QRect(100, 80, 171, 21))
        self.usernameLE.setObjectName("usernameLE")
        self.passwordLE = QtWidgets.QLineEdit(View)
        self.passwordLE.setGeometry(QtCore.QRect(100, 110, 171, 20))
        self.passwordLE.setInputMask("")
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLE.setObjectName("passwordLE")
        self.courseL = QtWidgets.QLabel(View)
        self.courseL.setGeometry(QtCore.QRect(20, 140, 61, 16))
        self.courseL.setObjectName("courseL")
        self.loginInfoL = QtWidgets.QLabel(View)
        self.loginInfoL.setGeometry(QtCore.QRect(100, 190, 231, 16))
        self.loginInfoL.setObjectName("loginInfoL")
        self.loginInfoL.hide()
        self.creditL = QtWidgets.QLabel(View)
        self.creditL.setGeometry(QtCore.QRect(10, 260, 131, 16))
        self.creditL.setObjectName("creditL")
        self.loginNowCB = QtWidgets.QCheckBox(View)
        self.loginNowCB.setGeometry(QtCore.QRect(100, 170, 111, 17))
        self.loginNowCB.setObjectName("loginNowCB")

        self.retranslateUi(View)
        self.buttonBox.accepted.connect(View.accept)
        self.buttonBox.rejected.connect(View.reject)
        QtCore.QMetaObject.connectSlotsByName(View)

        self.loadCourse()

    def retranslateUi(self, View):
        _translate = QtCore.QCoreApplication.translate
        View.setWindowTitle(_translate("View", "Bisa Tidor"))
        self.usernameL.setText(_translate("View", "Username"))
        self.headerL.setText(_translate("View", "Bisa Tidor"))
        self.passwordL.setText(_translate("View", "Password"))
        self.usernameLE.setPlaceholderText(_translate("View", "username@it.student.pens.ac.id"))
        self.passwordLE.setPlaceholderText(_translate("View", "password"))
        self.courseL.setText(_translate("View", "Course"))
        self.loginInfoL.setText(_translate("View", "You will be automatically logged in at XX:XX AM."))
        self.creditL.setText(_translate("View", "Made by chz & ilyasofficial."))
        self.loginNowCB.setText(_translate("View", "Log in immediately"))

    def loadCourse(self):
        courseNameList = []
        courseLogic = CourseLogic()

        courseLogic.loadFile()
        courseList = courseLogic.getCourseList()

        for course in courseList:
            courseNameList.append(course.getDetailName())

        print(courseNameList)

        self.courseCB.addItems(courseNameList)
