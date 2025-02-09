# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Corretor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Programa(object):
    def setupUi(self, Programa):
        Programa.setObjectName("Programa")
        Programa.setEnabled(True)
        Programa.resize(600, 469)
        Programa.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.centralwidget = QtWidgets.QWidget(Programa)
        self.centralwidget.setObjectName("centralwidget")
        self.cor = QtWidgets.QPushButton(self.centralwidget)
        self.cor.setGeometry(QtCore.QRect(390, 340, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cor.setFont(font)
        self.cor.setStyleSheet("background-color: rgb(80, 126, 66)")
        self.cor.setObjectName("cor")
        self.sair = QtWidgets.QPushButton(self.centralwidget)
        self.sair.setGeometry(QtCore.QRect(390, 410, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sair.setFont(font)
        self.sair.setStyleSheet("background-color: rgb(255, 125, 125)")
        self.sair.setObjectName("sair")
        self.arq = QtWidgets.QPushButton(self.centralwidget)
        self.arq.setGeometry(QtCore.QRect(20, 20, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.arq.setFont(font)
        self.arq.setStyleSheet("")
        self.arq.setObjectName("arq")
        self.arqShow = QtWidgets.QLineEdit(self.centralwidget)
        self.arqShow.setEnabled(True)
        self.arqShow.setGeometry(QtCore.QRect(110, 20, 461, 20))
        self.arqShow.setReadOnly(True)
        self.arqShow.setObjectName("arqShow")
        self.nmqLabel = QtWidgets.QLabel(self.centralwidget)
        self.nmqLabel.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.nmqLabel.setObjectName("nmqLabel")
        self.Q1 = QtWidgets.QWidget(self.centralwidget)
        self.Q1.setGeometry(QtCore.QRect(100, 80, 471, 41))
        self.Q1.setObjectName("Q1")
        self.a_1 = QtWidgets.QRadioButton(self.Q1)
        self.a_1.setEnabled(True)
        self.a_1.setGeometry(QtCore.QRect(301, 20, 29, 21))
        self.a_1.setAutoExclusive(False)
        self.a_1.setObjectName("a_1")
        self.qv_1 = QtWidgets.QLineEdit(self.Q1)
        self.qv_1.setGeometry(QtCore.QRect(100, 20, 51, 20))
        self.qv_1.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.qv_1.setObjectName("qv_1")
        self.q1Label2_1 = QtWidgets.QLabel(self.Q1)
        self.q1Label2_1.setGeometry(QtCore.QRect(10, 20, 83, 21))
        self.q1Label2_1.setObjectName("q1Label2_1")
        self.b_1 = QtWidgets.QRadioButton(self.Q1)
        self.b_1.setEnabled(True)
        self.b_1.setGeometry(QtCore.QRect(336, 20, 29, 21))
        self.b_1.setAutoExclusive(False)
        self.b_1.setObjectName("b_1")
        self.d_1 = QtWidgets.QRadioButton(self.Q1)
        self.d_1.setEnabled(True)
        self.d_1.setGeometry(QtCore.QRect(405, 20, 29, 21))
        self.d_1.setAutoExclusive(False)
        self.d_1.setObjectName("d_1")
        self.e_1 = QtWidgets.QRadioButton(self.Q1)
        self.e_1.setEnabled(True)
        self.e_1.setGeometry(QtCore.QRect(440, 20, 29, 21))
        self.e_1.setAutoExclusive(False)
        self.e_1.setObjectName("e_1")
        self.c_1 = QtWidgets.QRadioButton(self.Q1)
        self.c_1.setEnabled(True)
        self.c_1.setGeometry(QtCore.QRect(371, 20, 28, 21))
        self.c_1.setAutoExclusive(False)
        self.c_1.setObjectName("c_1")
        self.q1Label3_1 = QtWidgets.QLabel(self.Q1)
        self.q1Label3_1.setGeometry(QtCore.QRect(171, 20, 119, 20))
        self.q1Label3_1.setObjectName("q1Label3_1")
        self.Q2 = QtWidgets.QWidget(self.centralwidget)
        self.Q2.setGeometry(QtCore.QRect(100, 130, 471, 41))
        self.Q2.setObjectName("Q2")
        self.a_2 = QtWidgets.QRadioButton(self.Q2)
        self.a_2.setEnabled(True)
        self.a_2.setGeometry(QtCore.QRect(301, 20, 29, 21))
        self.a_2.setAutoExclusive(False)
        self.a_2.setObjectName("a_2")
        self.q1Label3_2 = QtWidgets.QLabel(self.Q2)
        self.q1Label3_2.setGeometry(QtCore.QRect(171, 20, 119, 20))
        self.q1Label3_2.setObjectName("q1Label3_2")
        self.b_2 = QtWidgets.QRadioButton(self.Q2)
        self.b_2.setEnabled(True)
        self.b_2.setGeometry(QtCore.QRect(336, 20, 29, 21))
        self.b_2.setAutoExclusive(False)
        self.b_2.setObjectName("b_2")
        self.d_2 = QtWidgets.QRadioButton(self.Q2)
        self.d_2.setEnabled(True)
        self.d_2.setGeometry(QtCore.QRect(405, 20, 29, 21))
        self.d_2.setAutoExclusive(False)
        self.d_2.setObjectName("d_2")
        self.q1Label2_2 = QtWidgets.QLabel(self.Q2)
        self.q1Label2_2.setGeometry(QtCore.QRect(10, 20, 83, 21))
        self.q1Label2_2.setObjectName("q1Label2_2")
        self.qv_2 = QtWidgets.QLineEdit(self.Q2)
        self.qv_2.setGeometry(QtCore.QRect(100, 20, 51, 20))
        self.qv_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.qv_2.setObjectName("qv_2")
        self.c_2 = QtWidgets.QRadioButton(self.Q2)
        self.c_2.setEnabled(True)
        self.c_2.setGeometry(QtCore.QRect(371, 20, 28, 21))
        self.c_2.setAutoExclusive(False)
        self.c_2.setObjectName("c_2")
        self.e_2 = QtWidgets.QRadioButton(self.Q2)
        self.e_2.setEnabled(True)
        self.e_2.setGeometry(QtCore.QRect(440, 20, 29, 21))
        self.e_2.setAutoExclusive(False)
        self.e_2.setObjectName("e_2")
        self.Q3 = QtWidgets.QWidget(self.centralwidget)
        self.Q3.setGeometry(QtCore.QRect(100, 180, 471, 41))
        self.Q3.setObjectName("Q3")
        self.a_3 = QtWidgets.QRadioButton(self.Q3)
        self.a_3.setEnabled(True)
        self.a_3.setGeometry(QtCore.QRect(301, 20, 29, 21))
        self.a_3.setAutoExclusive(False)
        self.a_3.setObjectName("a_3")
        self.qv_3 = QtWidgets.QLineEdit(self.Q3)
        self.qv_3.setGeometry(QtCore.QRect(100, 20, 51, 20))
        self.qv_3.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.qv_3.setObjectName("qv_3")
        self.q1Label2_3 = QtWidgets.QLabel(self.Q3)
        self.q1Label2_3.setGeometry(QtCore.QRect(10, 20, 83, 21))
        self.q1Label2_3.setObjectName("q1Label2_3")
        self.c_3 = QtWidgets.QRadioButton(self.Q3)
        self.c_3.setEnabled(True)
        self.c_3.setGeometry(QtCore.QRect(371, 20, 28, 21))
        self.c_3.setAutoExclusive(False)
        self.c_3.setObjectName("c_3")
        self.e_3 = QtWidgets.QRadioButton(self.Q3)
        self.e_3.setEnabled(True)
        self.e_3.setGeometry(QtCore.QRect(440, 20, 29, 21))
        self.e_3.setAutoExclusive(False)
        self.e_3.setObjectName("e_3")
        self.b_3 = QtWidgets.QRadioButton(self.Q3)
        self.b_3.setEnabled(True)
        self.b_3.setGeometry(QtCore.QRect(336, 20, 29, 21))
        self.b_3.setAutoExclusive(False)
        self.b_3.setObjectName("b_3")
        self.d_3 = QtWidgets.QRadioButton(self.Q3)
        self.d_3.setEnabled(True)
        self.d_3.setGeometry(QtCore.QRect(405, 20, 29, 21))
        self.d_3.setAutoExclusive(False)
        self.d_3.setObjectName("d_3")
        self.q1Label3_3 = QtWidgets.QLabel(self.Q3)
        self.q1Label3_3.setGeometry(QtCore.QRect(171, 20, 119, 20))
        self.q1Label3_3.setObjectName("q1Label3_3")
        self.Q4 = QtWidgets.QWidget(self.centralwidget)
        self.Q4.setGeometry(QtCore.QRect(100, 230, 471, 41))
        self.Q4.setObjectName("Q4")
        self.a_4 = QtWidgets.QRadioButton(self.Q4)
        self.a_4.setEnabled(True)
        self.a_4.setGeometry(QtCore.QRect(301, 20, 29, 21))
        self.a_4.setAutoExclusive(False)
        self.a_4.setObjectName("a_4")
        self.q1Label3_4 = QtWidgets.QLabel(self.Q4)
        self.q1Label3_4.setGeometry(QtCore.QRect(171, 20, 119, 20))
        self.q1Label3_4.setObjectName("q1Label3_4")
        self.qv_4 = QtWidgets.QLineEdit(self.Q4)
        self.qv_4.setGeometry(QtCore.QRect(100, 20, 51, 20))
        self.qv_4.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.qv_4.setObjectName("qv_4")
        self.e_4 = QtWidgets.QRadioButton(self.Q4)
        self.e_4.setEnabled(True)
        self.e_4.setGeometry(QtCore.QRect(440, 20, 29, 21))
        self.e_4.setAutoExclusive(False)
        self.e_4.setObjectName("e_4")
        self.c_4 = QtWidgets.QRadioButton(self.Q4)
        self.c_4.setEnabled(True)
        self.c_4.setGeometry(QtCore.QRect(371, 20, 28, 21))
        self.c_4.setAutoExclusive(False)
        self.c_4.setObjectName("c_4")
        self.b_4 = QtWidgets.QRadioButton(self.Q4)
        self.b_4.setEnabled(True)
        self.b_4.setGeometry(QtCore.QRect(336, 20, 29, 21))
        self.b_4.setAutoExclusive(False)
        self.b_4.setObjectName("b_4")
        self.d_4 = QtWidgets.QRadioButton(self.Q4)
        self.d_4.setEnabled(True)
        self.d_4.setGeometry(QtCore.QRect(405, 20, 29, 21))
        self.d_4.setAutoExclusive(False)
        self.d_4.setObjectName("d_4")
        self.q1Label2_4 = QtWidgets.QLabel(self.Q4)
        self.q1Label2_4.setGeometry(QtCore.QRect(10, 20, 83, 21))
        self.q1Label2_4.setObjectName("q1Label2_4")
        self.Q5 = QtWidgets.QWidget(self.centralwidget)
        self.Q5.setGeometry(QtCore.QRect(100, 280, 471, 41))
        self.Q5.setObjectName("Q5")
        self.a_5 = QtWidgets.QRadioButton(self.Q5)
        self.a_5.setEnabled(True)
        self.a_5.setGeometry(QtCore.QRect(301, 20, 29, 21))
        self.a_5.setAutoExclusive(False)
        self.a_5.setObjectName("a_5")
        self.q1Label2_5 = QtWidgets.QLabel(self.Q5)
        self.q1Label2_5.setGeometry(QtCore.QRect(10, 20, 83, 21))
        self.q1Label2_5.setObjectName("q1Label2_5")
        self.qv_5 = QtWidgets.QLineEdit(self.Q5)
        self.qv_5.setGeometry(QtCore.QRect(100, 20, 51, 20))
        self.qv_5.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.qv_5.setObjectName("qv_5")
        self.b_5 = QtWidgets.QRadioButton(self.Q5)
        self.b_5.setEnabled(True)
        self.b_5.setGeometry(QtCore.QRect(336, 20, 29, 21))
        self.b_5.setAutoExclusive(False)
        self.b_5.setObjectName("b_5")
        self.e_5 = QtWidgets.QRadioButton(self.Q5)
        self.e_5.setEnabled(True)
        self.e_5.setGeometry(QtCore.QRect(440, 20, 29, 21))
        self.e_5.setAutoExclusive(False)
        self.e_5.setObjectName("e_5")
        self.c_5 = QtWidgets.QRadioButton(self.Q5)
        self.c_5.setEnabled(True)
        self.c_5.setGeometry(QtCore.QRect(371, 20, 28, 21))
        self.c_5.setAutoExclusive(False)
        self.c_5.setObjectName("c_5")
        self.d_5 = QtWidgets.QRadioButton(self.Q5)
        self.d_5.setEnabled(True)
        self.d_5.setGeometry(QtCore.QRect(405, 20, 29, 21))
        self.d_5.setAutoExclusive(False)
        self.d_5.setObjectName("d_5")
        self.q1Label3_5 = QtWidgets.QLabel(self.Q5)
        self.q1Label3_5.setGeometry(QtCore.QRect(171, 20, 119, 20))
        self.q1Label3_5.setObjectName("q1Label3_5")
        self.q1Label1_1 = QtWidgets.QLabel(self.centralwidget)
        self.q1Label1_1.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.q1Label1_1.setObjectName("q1Label1_1")
        self.q1Label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.q1Label1_2.setGeometry(QtCore.QRect(20, 130, 61, 16))
        self.q1Label1_2.setObjectName("q1Label1_2")
        self.q1Label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.q1Label1_3.setGeometry(QtCore.QRect(20, 180, 61, 16))
        self.q1Label1_3.setObjectName("q1Label1_3")
        self.q1Label1_4 = QtWidgets.QLabel(self.centralwidget)
        self.q1Label1_4.setGeometry(QtCore.QRect(20, 230, 61, 16))
        self.q1Label1_4.setObjectName("q1Label1_4")
        self.q1Label1_5 = QtWidgets.QLabel(self.centralwidget)
        self.q1Label1_5.setGeometry(QtCore.QRect(20, 280, 61, 16))
        self.q1Label1_5.setObjectName("q1Label1_5")
        self.nmq = QtWidgets.QLineEdit(self.centralwidget)
        self.nmq.setEnabled(True)
        self.nmq.setGeometry(QtCore.QRect(110, 50, 31, 20))
        self.nmq.setMouseTracking(True)
        self.nmq.setAutoFillBackground(False)
        self.nmq.setStyleSheet("")
        self.nmq.setReadOnly(True)
        self.nmq.setObjectName("nmq")
        self.exibir = QtWidgets.QTextEdit(self.centralwidget)
        self.exibir.setGeometry(QtCore.QRect(20, 340, 351, 91))
        self.exibir.setMouseTracking(True)
        self.exibir.setTabletTracking(False)
        self.exibir.setStyleSheet("background-color:")
        self.exibir.setFrameShape(QtWidgets.QFrame.Box)
        self.exibir.setReadOnly(True)
        self.exibir.setObjectName("exibir")
        self.q_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.q_1.setGeometry(QtCore.QRect(20, 100, 71, 20))
        self.q_1.setText("")
        self.q_1.setReadOnly(True)
        self.q_1.setObjectName("q_1")
        self.q_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.q_2.setGeometry(QtCore.QRect(20, 150, 71, 20))
        self.q_2.setText("")
        self.q_2.setReadOnly(True)
        self.q_2.setObjectName("q_2")
        self.q_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.q_3.setGeometry(QtCore.QRect(20, 200, 71, 20))
        self.q_3.setText("")
        self.q_3.setReadOnly(True)
        self.q_3.setObjectName("q_3")
        self.q_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.q_4.setGeometry(QtCore.QRect(20, 250, 71, 20))
        self.q_4.setText("")
        self.q_4.setReadOnly(True)
        self.q_4.setObjectName("q_4")
        self.q_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.q_5.setGeometry(QtCore.QRect(20, 300, 71, 20))
        self.q_5.setStyleSheet("background-color: rgb(238, 238, 238)")
        self.q_5.setText("")
        self.q_5.setReadOnly(True)
        self.q_5.setObjectName("q_5")
        self.limpar = QtWidgets.QPushButton(self.centralwidget)
        self.limpar.setGeometry(QtCore.QRect(490, 410, 81, 23))
        self.limpar.setObjectName("limpar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 450, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Programa.setCentralWidget(self.centralwidget)

        self.retranslateUi(Programa)
        QtCore.QMetaObject.connectSlotsByName(Programa)

    def retranslateUi(self, Programa):
        _translate = QtCore.QCoreApplication.translate
        Programa.setWindowTitle(_translate("Programa", "Corretor Para Webex"))
        self.cor.setText(_translate("Programa", "CORRIGIR"))
        self.sair.setText(_translate("Programa", "Sair"))
        self.arq.setText(_translate("Programa", "Arquivo"))
        self.nmqLabel.setText(_translate("Programa", "N° de Questões:"))
        self.a_1.setText(_translate("Programa", "a"))
        self.q1Label2_1.setText(_translate("Programa", "Valor da Questão"))
        self.b_1.setText(_translate("Programa", "b"))
        self.d_1.setText(_translate("Programa", "d"))
        self.e_1.setText(_translate("Programa", "e"))
        self.c_1.setText(_translate("Programa", "c"))
        self.q1Label3_1.setText(_translate("Programa", "Alternativa(s) Correta(s)"))
        self.a_2.setText(_translate("Programa", "a"))
        self.q1Label3_2.setText(_translate("Programa", "Alternativa(s) Correta(s)"))
        self.b_2.setText(_translate("Programa", "b"))
        self.d_2.setText(_translate("Programa", "d"))
        self.q1Label2_2.setText(_translate("Programa", "Valor da Questão"))
        self.c_2.setText(_translate("Programa", "c"))
        self.e_2.setText(_translate("Programa", "e"))
        self.a_3.setText(_translate("Programa", "a"))
        self.q1Label2_3.setText(_translate("Programa", "Valor da Questão"))
        self.c_3.setText(_translate("Programa", "c"))
        self.e_3.setText(_translate("Programa", "e"))
        self.b_3.setText(_translate("Programa", "b"))
        self.d_3.setText(_translate("Programa", "d"))
        self.q1Label3_3.setText(_translate("Programa", "Alternativa(s) Correta(s)"))
        self.a_4.setText(_translate("Programa", "a"))
        self.q1Label3_4.setText(_translate("Programa", "Alternativa(s) Correta(s)"))
        self.e_4.setText(_translate("Programa", "e"))
        self.c_4.setText(_translate("Programa", "c"))
        self.b_4.setText(_translate("Programa", "b"))
        self.d_4.setText(_translate("Programa", "d"))
        self.q1Label2_4.setText(_translate("Programa", "Valor da Questão"))
        self.a_5.setText(_translate("Programa", "a"))
        self.q1Label2_5.setText(_translate("Programa", "Valor da Questão"))
        self.b_5.setText(_translate("Programa", "b"))
        self.e_5.setText(_translate("Programa", "e"))
        self.c_5.setText(_translate("Programa", "c"))
        self.d_5.setText(_translate("Programa", "d"))
        self.q1Label3_5.setText(_translate("Programa", "Alternativa(s) Correta(s)"))
        self.q1Label1_1.setText(_translate("Programa", "Questão 1"))
        self.q1Label1_2.setText(_translate("Programa", "Questão 2"))
        self.q1Label1_3.setText(_translate("Programa", "Questão 3"))
        self.q1Label1_4.setText(_translate("Programa", "Questão 4"))
        self.q1Label1_5.setText(_translate("Programa", "Questão 5"))
        self.limpar.setText(_translate("Programa", "Limpar"))
        self.label.setText(_translate("Programa", "Desenvolvido por João Pedro C. Moreira (mcjpedro@gmail.com)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Programa = QtWidgets.QMainWindow()
    ui = Ui_Programa()
    ui.setupUi(Programa)
    Programa.show()
    sys.exit(app.exec_())
