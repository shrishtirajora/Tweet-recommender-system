from sip import setapi
setapi("QDate", 2)
setapi("QDateTime", 2)
setapi("QTextStream", 2)
setapi("QTime", 2)
setapi("QVariant", 2)
setapi("QString", 2)
setapi("QUrl", 2)

from PyQt4 import QtGui
import sys
import os
import first_page
import second_page
import tfidfclassification
import kmeans

class secWin(QtGui.QMainWindow, second_page.Ui_Form):
    def __init__(self, parent=None):
        super(secWin, self).__init__(parent)
        self.setupUi(self)
        self.textEdit.setStyleSheet("QTextEdit {color:#fff;font-family:Georgia;}")
        self.textEdit_2.setStyleSheet("QTextEdit {color:#fff;font-family:Georgia;}")
        self.textEdit_3.setStyleSheet("QTextEdit {color:#fff}")
        self.textEdit_4.setStyleSheet("QTextEdit {color:#fff;}")
        self.textEdit_3.insertPlainText("Hash-Tags")
        self.textEdit_4.insertPlainText("articles")
        self.pushButton.clicked.connect(self.back)
        self.wind1 = "dd"
        self.wind2 = "dasd"
    def back(self):
        self.textEdit.insertPlainText(self.wind1)
        self.textEdit_2.insertPlainText(self.wind2)
        # firWin(self).show()
        # self.close()
        # print dir(s elf.textEdit.font)
    # def browse_folder(self):
    #     # form = ExampleApp()
    #     self.hide()    
    #     directory = QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder")
    #     if directory:
    #         for file_name in os.listdir(directory): 
    #             self.listWidget.addItem(file_name)
    #     self.show()
class firWin(QtGui.QWidget, first_page.Ui_Form):
    def __init__(self, parent=None):
        super(firWin, self).__init__(parent)
        self.setupUi(self)
        # wind = None
        self.second.clicked.connect(self.handleButton)

    def handleButton(self):
        # print blah
        # print party.blah(1)
        # print dir(self.lineEdit)
        # if self.wind is None:
        strt = tfidfclassification.blah(self.lineEdit.text())
        strr = kmeans.main(self.lineEdit.text())
        wind = secWin(self)
        wind.wind1 = strt
        wind.wind2 = strr
        self.hide()
        wind.show()
  
def main():
    app = QtGui.QApplication(sys.argv)
    form = firWin()
    # form1 = secWin()

    # print dir(form)
    # print dir(event)
    form.show()
    # while(1):
    # form.second.clicked.connect(rand)
    # break
    
    # form.hide()
    # print form.isFullScreen()
    app.exec_()
    # app.setStyle()


if __name__ == '__main__':
    main()
