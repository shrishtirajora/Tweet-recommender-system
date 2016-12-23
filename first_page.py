# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from sip import setapi
setapi("QDate", 2)
setapi("QDateTime", 2)
setapi("QTextStream", 2)
setapi("QTime", 2)
setapi("QVariant", 2)
setapi("QString", 2)
setapi("QUrl", 2)
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
        Form.setStyleSheet(_fromUtf8("#topFrame QPushButton:hover {\n"
"    background-color:#408c99;\n"
"\n"
"}\n"
"\n"
"#topFrame  QPushButton{\n"
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
"#topFrame QPushButton:pressed {\n"
"background-color:#fff;\n"
"position:relative;\n"
"    top:1px;\n"
"}\n"
"#topFrame{\n"
"background-color: #2c3e50; /* fallback for old browsers */\n"
" /*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);*/\n"
" /* fallback for old browsers */\n"
"/*background: -webkit-linear-gradient(to left, #2c3e50 , #3498db); /* Chrome 10-25, Safari 5.1-6 */\n"
"/*background: linear-gradient(to left, #2c3e50 , #3498db);  W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */\n"
"        \n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0  #2c3e50, stop: 1 #3498db);\n"
"}\n"
"#frame_2{\n"
"background-color: #2c3e50; /* fallback for old browsers */\n"
" /*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);*/\n"
"/* fallback for old browsers */\n"
"/*background: -webkit-linear-gradient(to left, #2c3e50 , #3498db); /* Chrome 10-25, Safari 5.1-6 */\n"
"/*background: linear-gradient(to left, #2c3e50 , #3498db);  W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */\n"
"        \n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0  #2c3e50, stop: 1 #3498db);\n"
"}"))
        self.topFrame = QtGui.QFrame(Form)
        self.topFrame.setGeometry(QtCore.QRect(-21, -11, 731, 521))
        self.topFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.topFrame.setObjectName(_fromUtf8("topFrame"))
        self.second = QtGui.QPushButton(self.topFrame)
        self.second.setGeometry(QtCore.QRect(230, 310, 271, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.second.setFont(font)
        self.second.setObjectName(_fromUtf8("second"))
        self.frame = QtGui.QFrame(self.topFrame)
        self.frame.setGeometry(QtCore.QRect(120, 50, 491, 141))
        self.frame.setStyleSheet(_fromUtf8("#frame{\n"
"image: url(/home/suryansh/Documents/ShowImage.png);\n"
"border:None;\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.lineEdit = QtGui.QLineEdit(self.topFrame)
        self.lineEdit.setGeometry(QtCore.QRect(230, 230, 271, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setAccessibleName(_fromUtf8(""))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(_fromUtf8("#lineEdit{\n"
"border:None;\n"
"border-radius:4px;\n"
"border-color:blue;\n"
"}"))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.second.setText(_translate("Form", "#tagthis!", None))
        self.lineEdit.setPlaceholderText(_translate("Form", "enter text here!", None))

