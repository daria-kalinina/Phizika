import sys
from random import randint, shuffle
import sqlite3
from PyQt5 import uic, QtCore, QtGui  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser
import docx

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.calculator_run)
        self.pushButton_2.clicked.connect(self.urov_run)


    def urov_run(self):
        uic.loadUi('urov.ui', self)
        self.pushButton.clicked.connect(self.zadachi_run1)
        self.pushButton_2.clicked.connect(self.zadachi_run2)
        self.pushButton_3.clicked.connect(self.zadachi_run3)
        self.pushButton_5.clicked.connect(self.zadachi_run4)
        self.pushButton_4.clicked.connect(self.run)


    def zadachi_run1(self):
        uic.loadUi('zadachi.ui', self)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.zadachi_run1)
        con = sqlite3.connect('Эдуардик.db')
        cur = con.cursor()
        i = randint(1, 10)
        self.result = cur.execute("""SELECT ot FROM Задачи1
                               WHERE num = """ + str(i)).fetchall()
        text = cur.execute("""SELECT tex FROM Задачи1
                               WHERE num = """ + str(i)).fetchall()
        text = str(text)[3:-4]
        self.textEdit.setText(text)
        self.result = str(self.result)[3:-4]
        print(self.result)
        self.pushButton.clicked.connect(self.zadachi_run_p1)


    def zadachi_run_p1(self):
        text = self.lineEdit.text()
        if text == self.result:
            self.pushButton.setStyleSheet('QPushButton {background-color: green; color: black;}')
        else:
            self.pushButton.setStyleSheet('QPushButton {background-color: red; color: black;}')
        self.pushButton.setText(self.result)


    def zadachi_run2(self):
        uic.loadUi('zadachi.ui', self)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.zadachi_run1)
        con = sqlite3.connect('Эдуардик.db')
        cur = con.cursor()
        i = randint(1, 10)
        self.result = cur.execute("""SELECT ot FROM Задачи2
                               WHERE num = """ + str(i)).fetchall()
        text = cur.execute("""SELECT tex FROM Задачи2
                               WHERE num = """ + str(i)).fetchall()
        text = str(text)[3:-4]
        self.textEdit.setText(text)
        self.result = str(self.result)[3:-4]
        print(self.result)
        self.pushButton.clicked.connect(self.zadachi_run_p2)


    def zadachi_run_p2(self):
        text = self.lineEdit.text()
        if text == self.result:
            self.pushButton.setStyleSheet('QPushButton {background-color: green; color: black;}')
        else:
            self.pushButton.setStyleSheet('QPushButton {background-color: red; color: black;}')
        self.pushButton.setText(self.result)


    def zadachi_run3(self):
        uic.loadUi('zadachi.ui', self)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.zadachi_run1)
        con = sqlite3.connect('Эдуардик.db')
        cur = con.cursor()
        i = randint(1, 10)
        self.result = cur.execute("""SELECT ot FROM Задачи3
                               WHERE num = """ + str(i)).fetchall()
        text = cur.execute("""SELECT tex FROM Задачи3
                               WHERE num = """ + str(i)).fetchall()
        text = str(text)[3:-4]
        self.textEdit.setText(text)
        self.result = str(self.result)[3:-4]
        print(self.result)
        self.pushButton.clicked.connect(self.zadachi_run_p3)


    def zadachi_run_p3(self):
        text = self.lineEdit.text()
        if text == self.result:
            self.pushButton.setStyleSheet('QPushButton {background-color: green; color: black;}')
        else:
            self.pushButton.setStyleSheet('QPushButton {background-color: red; color: black;}')
        self.pushButton.setText(self.result)


    def zadachi_run4(self):
        uic.loadUi('zadachi.ui', self)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.zadachi_run1)
        con = sqlite3.connect('Эдуардик.db')
        cur = con.cursor()
        i = randint(1, 10)
        self.result = cur.execute("""SELECT ot FROM Задачи4
                               WHERE num = """ + str(i)).fetchall()
        text = cur.execute("""SELECT tex FROM Задачи4
                               WHERE num = """ + str(i)).fetchall()
        text = str(text)[3:-4]
        self.textEdit.setText(text)
        self.result = str(self.result)[3:-4]
        print(self.result)
        self.pushButton.clicked.connect(self.zadachi_run_p4)


    def zadachi_run_p4(self):
        text = self.lineEdit.text()
        if text == self.result:
            self.pushButton.setStyleSheet('QPushButton {background-color: green; color: black;}')
        else:
            self.pushButton.setStyleSheet('QPushButton {background-color: red; color: black;}')
        self.pushButton.setText(self.result)


    def calculator_run(self):
        uic.loadUi('calc.ui', self)
        self.pushButton.clicked.connect(self.calculator_run1)
        self.pushButton_4.clicked.connect(self.run)


    def calculator_run1(self):
        pc = self.comboBox_1.currentText()
        mc = self.comboBox_2.currentText()
        vc = self.comboBox_3.currentText()
        Fc = self.comboBox_4.currentText()
        tc = self.comboBox_5.currentText()
        Sc = self.comboBox_6.currentText()
        Pc = self.comboBox_7.currentText()
        Ekc = self.comboBox_8.currentText()
        Ac = self.comboBox_9.currentText()
        Nc = self.comboBox_10.currentText()
        gc = self.comboBox_11.currentText()
        hc = self.comboBox_12.currentText()
        Epc = self.comboBox_13.currentText()
        p = self.lineEdit_1.text()
        if p != '' and p != '?':
            p=float(p)
            p = self.perevod(p, self.comboBox_14.currentText())
        m = self.lineEdit_2.text()
        if m != '' and m != '?':
            m=float(m)
            m = self.perevod(m, self.comboBox_14.currentText())
        v = self.lineEdit_3.text()
        if v != '' and v != '?':
            v=float(v)
            v = self.perevod(v, self.comboBox_14.currentText())
        F = self.lineEdit_5.text()
        if F != '' and F != '?':
            F=float(F)
            F = self.perevod(F, self.comboBox_14.currentText())
        t = self.lineEdit_6.text()
        if t != '' and t != '?':
            t=float(t)
            t = self.perevod(t, self.comboBox_14.currentText())
        S = self.lineEdit_7.text()
        if S != '' and S != '?':
            S=float(S)
            S = self.perevod(S, self.comboBox_14.currentText())
        P = self.lineEdit_8.text()
        if P != '' and P != '?':
            P=float(P)
            P = self.perevod(P, self.comboBox_14.currentText())
        Ek = self.lineEdit_9.text()
        if Ek != '' and Ek != '?':
            Ek=float(Ek)
            Ek = self.perevod(Ek, self.comboBox_14.currentText())
        A = self.lineEdit_10.text()
        if A != '' and A != '?':
            A=float(A)
            A = self.perevod(A, self.comboBox_14.currentText())
        N = self.lineEdit_11.text()
        if N != '' and N != '?':
            N=float(N)
            N = self.perevod(N, self.comboBox_14.currentText())
        g = self.lineEdit_12.text()
        if g != '' and g != '?':
            g=float(g)
            g = self.perevod(g, self.comboBox_14.currentText())
        h = self.lineEdit_13.text()
        if h != '' and h != '?':
            h=float(h)
            h = self.perevod(h, self.comboBox_14.currentText())
        Ep = self.lineEdit_14.text()
        if Ep != '' and Ep != '?':
            Ep=float(Ep)
            Ep = self.perevod(Ep, self.comboBox_14.currentText())
        y1 = [pc, mc, vc, Fc, tc, Sc, Pc, Ekc, Ac, Nc, gc, hc, Epc]
        y2 = ['p', 'm', 'v', 'F', 't', 'S', 'P', 'Ek', 'A', 'N', 'g', 'h', 'Ep']
        y3 = [p, m, v, F, t, S, P, Ek, A, N, g, h, Ep]
        c = []
        z = ''
        for i in range(len(y1)):
            if y3[i] == '?':
                    z = y2[i]
            elif y1[i] != '---':
                c.append(y2[i])
        c = sorted(c)
        c = ','.join(c)
        c = "'"+c+"'"
        z = "'"+z+"'"
        con = sqlite3.connect('арсюша.db')
        cur = con.cursor()
        text = cur.execute("""SELECT form FROM формула
                                       WHERE per = """ +str(c)+""" AND isk = """ +str(z)).fetchall()
        text = str(text)[3:-4]
        z = z[1:-1]
        if z == 'p':
            p = eval(text)
            self.lineEdit_4.setText(str(p))
        if z == 'm':
            m = eval(text)
            self.lineEdit_4.setText(str(m))
        if z == 'v':
            v = eval(text)
            self.lineEdit_4.setText(str(v))
        if z == 'F':
            F = eval(text)
            self.lineEdit_4.setText(str(F))
        if z == 't':
            t = eval(text)
            self.lineEdit_4.setText(str(t))
        if z == 'S':
            S = eval(text)
            self.lineEdit_4.setText(str(S))
        if z == 'P':
            P = eval(text)
            self.lineEdit_4.setText(str(P))
        if z == 'Ek':
            Ek = eval(text)
            self.lineEdit_4.setText(str(Ek))
        if z == 'A':
            A = eval(text)
            self.lineEdit_4.setText(str(A))
        if z == 'N':
            N = eval(text)
            self.lineEdit_4.setText(str(N))
        if z == 'g':
            g = eval(text)
            self.lineEdit_4.setText(str(g))
        if z == 'h':
            h = eval(text)
            self.lineEdit_4.setText(str(h))
        if z == 'Ep':
            Ep = eval(text)
            self.lineEdit_4.setText(str(Ep))


    def perevod(self,per,comb):
        con = sqlite3.connect('даша.db')
        cur = con.cursor()
        comb = "'"+comb+"'"
        print(comb)
        text = cur.execute("""SELECT ci FROM СИ
                                    WHERE per='кг'""").fetchall()
        text = str(text)[3:-4]
        print(text)
        return per*float(text)*0.1


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())