# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\0College\0 3rd_2\人工智能\徐怡然_19307130289_花卉分类专家系统\character.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ctypes import sizeof
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_character(object):
    def setupUi(self, character):
        character.setObjectName("character")
        character.resize(657, 442)
        self.setWindowIcon(QtGui.QIcon('./src/花朵.png'))

        self.charactertext=''

        self.pushButton = QtWidgets.QPushButton(character)
        self.pushButton.setGeometry(QtCore.QRect(280, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(character)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.editor = QtWidgets.QLineEdit(character)
        self.editor.setGeometry(90, 150, 491, 121)
        self.editor.setPlaceholderText(" Inter The Input Here ")
        # self.textBrowser = QtWidgets.QTextBrowser(character)
        # self.textBrowser.setGeometry(QtCore.QRect(90, 150, 491, 121))
        # self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(character)
        self.label.setGeometry(QtCore.QRect(90, 60, 481, 71))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(character)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(character)
        QtCore.QMetaObject.connectSlotsByName(character)

    def retranslateUi(self, character):
        _translate = QtCore.QCoreApplication.translate
        character.setWindowTitle(_translate("character", "复旦校园花卉植物鉴别专家系统"))
        character.setWindowTitle(_translate("character", "Dialog"))
        self.pushButton.setText(_translate("character", "确认"))
        self.pushButton_2.setText(_translate("character", "返回主菜单"))
        self.label_2.setText(_translate("character", "请选择满足的性状(以英文逗号分隔)"))
        message=''
        with open('性状矩阵.csv','r',encoding='utf-8') as f:
            for line in f:
                items=line.split(',')
                j=0
                for i in items:
                    if j>0:
                        message=message+str(j)+i+'; '
                    if j%5==0:
                        message+='\n'
                    j+=1
                break
        self.label.setText(_translate("character",message))