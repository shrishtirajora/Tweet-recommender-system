# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setGeometry(100,100,687, 507)
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(687, 507)
        Form.setMinimumSize(QtCore.QSize(687, 507))
        Form.setStyleSheet(_fromUtf8("#Form QPushButton:hover {\n"
"    background-color:#408c99;\n"
"\n"
"}\n"
"#Form QTextEdit{\n"
"border-radius:18px;\n"
"background: rgba(255,255,255,10%);\n"
"font-family:Purisa;\n"
"}\n"
"#Form  QPushButton{\n"
"    box-shadow: 0px 10px 14px -7px #276873;\n"
"    background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #599bb3, stop:1 #408c99);\n"
"    background-color:#599bb3;\n"
"    -moz-border-radius:8px;\n"
"    -webkit-border-radius:8px;\n"
"    border-radius:8px;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Purisa;\n"
"    font-size:20px;\n"
"    font-weight:bold;\n"
"    padding:13px 32px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #3d768a;\n"
"}\n"
"\n"
"#Form QPushButton:pressed {\n"
"background-color:#fff;\n"
"position:relative;\n"
"    top:1px;\n"
"}\n"
"#Form{\n"
"background-color: #2c3e50; \n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0  #2c3e50, stop: 1 #3498db);\n"
"}"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 430, 641, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 241, 321))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(390, 80, 261, 321))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(50, 30, 151, 31))
        self.textEdit_3.setStyleSheet(_fromUtf8("border-radius:18px;\n"
"background: rgba(255,255,255,0%);\n"
"font-family:Purisa;"))
        self.textEdit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(440, 30, 151, 31))
        self.textEdit_4.setAcceptDrops(True)
        self.textEdit_4.setStyleSheet(_fromUtf8("border-radius:18px;\n"
"background: rgba(255,255,255,0%);\n"
"font-family:Purisa;"))
        self.textEdit_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Show", None))

