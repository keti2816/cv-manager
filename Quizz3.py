import sys
from Quiz3 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("CV Manager")

        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_register.clicked.connect(self.register)
        self.pushButton_register.clicked.connect(self.clear) #table-shi damatebis mere rom waishalos sheyvanili monacemebi
        self.pushButton_cleartable.clicked.connect(self.clear_table)
        self.pushButton_close.clicked.connect(self.close)


    def clear(self):
        #personal info
        self.lineEdit_phone.clear()
        self.lineEdit_email.clear()
        self.lineEdit_lastname.clear()
        self.lineEdit_name.clear()

        #skills
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)

        #About me
        self.textEdit.clear()

    def deselect_button(self):
        pass

    def register(self):
        firstname = self.lineEdit_name.text()
        lastname = self.lineEdit_lastname.text()
        phone = self.lineEdit_phone.text()
        email = self.lineEdit_email.text()
        if self.radioButton_f.isChecked():
            gender = self.radioButton_f.text()
        elif self.radioButton_m.isChecked():
            gender = self.radioButton_m.text()
        else:
            gender = None
        #skillebis damateba listshi
        skills = []
        if self.checkBox.isChecked():
            skills.append(self.checkBox.text())
        if self.checkBox_2.isChecked():
            skills.append(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            skills.append(self.checkBox_3.text())
        if self.checkBox_4.isChecked():
            skills.append(self.checkBox_4.text())
        if self.checkBox_5.isChecked():
            skills.append(self.checkBox_5.text())
        if self.checkBox_6.isChecked():
            skills.append(self.checkBox_6.text())
        if self.checkBox_7.isChecked():
            skills.append(self.checkBox_7.text())
        if self.checkBox_8.isChecked():
            skills.append(self.checkBox_8.text())
        if self.checkBox_9.isChecked():
            skills.append(self.checkBox_9.text())
        if self.checkBox_10.isChecked():
            skills.append(self.checkBox_10.text())

        str_skills = ""
        for skill in skills:
            str_skills += skill + "\n"
        print(str_skills)
        #read only radgan iq chawerisas ar sheicvalos monacemebi
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        print("register clicked!")
        print(f"firstname: {firstname}, lastname: {lastname}, "
              f"phone: {phone}, "
              f"email: {email}, "
              f"gender: {gender}, "
              f"skills:{skills}")

        about_me = self.textEdit.toPlainText()
        print(about_me)

        #tablewidget-shi svetebis damateba da monacemebis sheyvana
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(firstname))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(lastname))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(phone))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(email))
        self.tableWidget.setItem(row, 4, QTableWidgetItem(gender))
        self.tableWidget.setItem(row, 5, QTableWidgetItem(str_skills))
        self.tableWidget.setItem(row, 6, QTableWidgetItem(about_me))

    def clear_table(self):
        self.tableWidget.setRowCount(0)


app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
