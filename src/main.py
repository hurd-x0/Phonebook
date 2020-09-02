import gui
import sqlite3 as db
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot
import xlsxwriter

class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.load_table('SELECT * FROM phones')

    def clear_table(self):
        self.table.setRowCount(0)

    def load_table(self,sql):
        output = LoadData(sql)
        for row in output:
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)
            for i, column in enumerate(row, 0):
                self.table.setItem(row_pos, i, QtWidgets.QTableWidgetItem(column))

    def error(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("مشکل")
        msg.setInformativeText(text)
        msg.setWindowTitle("مشکل")
        msg.exec_()
    
    def info(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("اطالاعات")
        msg.setInformativeText(text)
        msg.setWindowTitle("اطالاعات")
        msg.exec_()
    
    def savefile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Export", "","Xls Files (*.xlsx)", options=options)
        if fileName:
            fileName += '.xlsx'
            workbook = xlsxwriter.Workbook(fileName)
            worksheet = workbook.add_worksheet()
            for i in range(self.table.columnCount()):
                for j in range(self.table.rowCount()):
                    text = self.table.item(j, i).text()
                    worksheet.write(j, i,text)
            workbook.close()
            self.info('خروجی با موفقیت ایجاد شد !')
    
    @pyqtSlot()
    def add_button(self):
        datas = {
            'name' : self.name.text(),
            'family' : self.family.text(),
            'phone1' : self.phone1.text(),
            'phone2' : self.phone2.text(),
            'phone3' : self.phone3.text(),
            'home1' : self.home1.text(),
            'home2' : self.home2.text(),
            'home3' : self.home3.text(),
            'home_path' : self.home_path.text(),
            'fax' : self.fax.text(),
            'website' : self.website.text(),
            'email' : self.email.text(),
            'messager' : self.messager.currentText(),
            'phone_msg' : self.phone_msg.text(),
            'workpath' : self.workpath.text()
        }
        if datas['name'] and datas['family']:
            try:
                AddData(list(datas.values()))
                self.clear_table()
                self.load_table('SELECT * FROM phones')
            except db.IntegrityError:
                self.error('اطالاعات مورد نظر در پایگاه داده موجود است')
        else:
            self.error('لطفا نام و نام خانوادگی را پرکنید')
    
    @pyqtSlot()
    def search_button(self):
        datas = {
            'name' : self.name.text(),
            'family' : self.family.text(),
            'phone1' : self.phone1.text(),
            'phone2' : self.phone2.text(),
            'phone3' : self.phone3.text(),
            'home1' : self.home1.text(),
            'home2' : self.home2.text(),
            'home3' : self.home3.text(),
            'home_path' : self.home_path.text(),
            'fax' : self.fax.text(),
            'website' : self.website.text(),
            'email' : self.email.text(),
            'messager' : self.messager.currentText(),
            'phone_msg' : self.phone_msg.text(),
            'workpath' : self.workpath.text()
        }
        sql = """
        SELECT * FROM Phones WHERE 
        name LIKE '%{0}%' AND 
        family LIKE '%{1}%' AND 
        phone1 LIKE '%{2}%' AND 
        phone2 LIKE '%{3}%' AND
        phone3 LIKE '%{4}%' AND
        home1 LIKE '%{5}%' AND
        home2 LIKE '%{6}%' AND
        home3 LIKE '%{7}%' AND
        home_path LIKE '%{8}%' AND
        fax LIKE '%{9}%' AND
        website LIKE '%{10}%' AND
        email LIKE '%{11}%' AND
        messager LIKE '%{12}%' AND
        phone_msg LIKE '%{13}%' AND
        workpath LIKE '%{14}%'
        """.format(
            datas['name'],
            datas['family'],
            datas['phone1'],
            datas['phone2'],
            datas['phone3'],
            datas['home1'],
            datas['home2'],
            datas['home3'],
            datas['home_path'],
            datas['fax'],
            datas['website'],
            datas['email'],
            datas['messager'],
            datas['phone_msg'],
            datas['workpath']
        )
        self.clear_table()
        self.load_table(sql)
    
    @pyqtSlot()
    def delete_button(self):
        datas = {
            'name' : self.name.text(),
            'family' : self.family.text(),
            'phone1' : self.phone1.text(),
            'phone2' : self.phone2.text(),
            'phone3' : self.phone3.text(),
            'home1' : self.home1.text(),
            'home2' : self.home2.text(),
            'home3' : self.home3.text(),
            'home_path' : self.home_path.text(),
            'fax' : self.fax.text(),
            'website' : self.website.text(),
            'email' : self.email.text(),
            'messager' : self.messager.currentText(),
            'phone_msg' : self.phone_msg.text(),
            'workpath' : self.workpath.text()
        }
        sql = """
        DELETE FROM Phones WHERE 
        name LIKE '%{0}%' AND 
        family LIKE '%{1}%' AND 
        phone1 LIKE '%{2}%' AND 
        phone2 LIKE '%{3}%' AND
        phone3 LIKE '%{4}%' AND
        home1 LIKE '%{5}%' AND
        home2 LIKE '%{6}%' AND
        home3 LIKE '%{7}%' AND
        home_path LIKE '%{8}%' AND
        fax LIKE '%{9}%' AND
        website LIKE '%{10}%' AND
        email LIKE '%{11}%' AND
        messager LIKE '%{12}%' AND
        phone_msg LIKE '%{13}%' AND
        workpath LIKE '%{14}%'
        """.format(
            datas['name'],
            datas['family'],
            datas['phone1'],
            datas['phone2'],
            datas['phone3'],
            datas['home1'],
            datas['home2'],
            datas['home3'],
            datas['home_path'],
            datas['fax'],
            datas['website'],
            datas['email'],
            datas['messager'],
            datas['phone_msg'],
            datas['workpath']
        )
        if datas['name']:
            cur = con.cursor()
            cur.execute(sql)
            if cur.rowcount <= 0:
                self.error('کاربری با این مشخصات پیدا نشد !')
            else:
                self.info('کاربر با موفقیت حذف شد !')
                con.commit()
                self.clear_table()
                self.load_table('SELECT * FROM phones')
        else:
            self.error('لطفا فیلد نام را پر کنید !')
    @pyqtSlot()
    def export(self):
        self.savefile()

def CreateTable():
    global con
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS `phones`(
            name TEXT,
            family TEXT,
            phone1 TEXT,
            phone2 TEXT,
            phone3 TEXT,
            home1 TEXT,
            home2 TEXT,
            home3 TEXT,
            home_path TEXT,
            fax TEXT,
            website TEXT,
            email TEXT,
            messager TEXT,
            phone_msg TEXT,
            workpath TEXT
        )
        ''')
    return True

def LoadData(sql):
    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchall()

def AddData(values):
    cur = con.cursor()
    cur.execute('''
    INSERT INTO `phones`(name,family,phone1,phone2,phone3,home1,home2,home3,home_path,fax,website,email,messager,phone_msg,workpath)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''',values)
    con.commit()
    return True

def main():
    global con
    con = db.connect('phones.sqlite3')
    CreateTable()
    mainApp = QApplication(['دفترچه تلفن'])
    mainWindow = App()
    mainWindow.show()
    mainApp.exec_()
    con.close()

if __name__ == "__main__" : main()