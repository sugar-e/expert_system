# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\0College\0 3rd_2\人工智能\期末pj\professional.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_professional(object):
    def setupUi(self, professional):
        professional.setObjectName("professional")
        professional.resize(730, 662)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        professional.setFont(font)
        self.setWindowTitle('复旦校园花卉植物鉴别专家系统')
        self.setWindowIcon(QIcon('./src/花朵.png'))
        self.label = QtWidgets.QLabel(professional)
        self.label.setGeometry(QtCore.QRect(50, 10, 151, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(professional)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 591, 71))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        # self.radioButton = QtWidgets.QRadioButton(professional)
        # self.radioButton.setGeometry(QtCore.QRect(220, 180, 89, 81))
        # self.radioButton.setObjectName("radioButton")
        # self.radioButton_2 = QtWidgets.QRadioButton(professional)
        # self.radioButton_2.setGeometry(QtCore.QRect(360, 180, 89, 81))
        # self.radioButton_2.setObjectName("radioButton_2")
        # self.pushButton = QtWidgets.QPushButton(professional)
        # self.pushButton.setGeometry(QtCore.QRect(500, 200, 121, 41))
        # self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(professional)
        self.label_3.setGeometry(QtCore.QRect(120, 300, 501, 221))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(professional)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(professional)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 570, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(professional)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 190, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(professional)
        QtCore.QMetaObject.connectSlotsByName(professional)

    def retranslateUi(self, professional):
        _translate = QtCore.QCoreApplication.translate
        professional.setWindowTitle(_translate("professional", "复旦校园花卉植物鉴别专家系统"))
        self.label.setText(_translate("professional", "是否具有如下性状："))
        # self.radioButton.setText(_translate("professional", "是"))
        # self.radioButton_2.setText(_translate("professional", "否"))
        self.pushButton.setText(_translate("professional", "是"))
        self.pushButton_2.setText(_translate("professional", "返回主菜单"))
        self.pushButton_3.setText(_translate("professional", "否"))
