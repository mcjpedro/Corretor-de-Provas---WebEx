from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
from tkinter import filedialog as dlg
from tkinter import Tk, messagebox
from collections import Counter
import os, sys, re
import pandas as pd
import numpy as np

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
        self.Q1.setEnabled(False)
        self.Q2.setEnabled(False)
        self.Q3.setEnabled(False)
        self.Q4.setEnabled(False)
        self.Q5.setEnabled(False)
        self.arq.clicked.connect(self.diretorio)
        self.cor.clicked.connect(self.programa)
        self.sair.clicked.connect(lambda: quit())
        self.limpar.clicked.connect(self.limpa)
            
    def limpa(self):
        self.arqShow.setText("")
        self.nmq.setText("")
        self.qv_1.setText("")
        self.q_1.setText("")
        self.a_1.setChecked(False)
        self.b_1.setChecked(False)
        self.c_1.setChecked(False)
        self.d_1.setChecked(False)
        self.e_1.setChecked(False)
        self.qv_2.setText("")
        self.q_2.setText("")
        self.a_2.setChecked(False)
        self.b_2.setChecked(False)
        self.c_2.setChecked(False)
        self.d_2.setChecked(False)
        self.e_2.setChecked(False)
        self.qv_3.setText("")
        self.q_3.setText("")
        self.a_3.setChecked(False)
        self.b_3.setChecked(False)
        self.c_3.setChecked(False)
        self.d_3.setChecked(False)
        self.e_3.setChecked(False)
        self.qv_4.setText("")
        self.q_4.setText("")
        self.a_4.setChecked(False)
        self.b_4.setChecked(False)
        self.c_4.setChecked(False)
        self.d_4.setChecked(False)
        self.e_4.setChecked(False)
        self.qv_5.setText("")
        self.q_5.setText("")
        self.a_5.setChecked(False)
        self.b_5.setChecked(False)
        self.c_5.setChecked(False)
        self.d_5.setChecked(False)
        self.e_5.setChecked(False)
        self.exibir.setText("")
        self.Q1.setEnabled(False)
        self.Q2.setEnabled(False)
        self.Q3.setEnabled(False)
        self.Q4.setEnabled(False)
        self.Q5.setEnabled(False)

    # LEITURA E MANIPULAÇÃO DE DADOS
    def diretorio(self):
        global typequestion, nmq, margedata, margeopen, a
        erro1 = 0
        while  erro1 == 0:
            Tk().withdraw()
            directory = dlg.askopenfilename(filetypes = (("Arquivos de texto","*.txt"),("Arquivos","*")))
            self.arqShow.setText(directory)
            if directory[-4::] != '.txt':
                messagebox.showwarning('Aviso', 'Escolha um arquivo .txt.')
                break
            elif directory == '':
                messagebox.showwarning('Aviso', 'Selecione o diretório')
                break
            f = open(directory, 'r', encoding='utf-16-le') 
            txt = f.read().splitlines()
            row = len(txt)
            f.close()
            lines = []
            for i in range(0,row):
                txt[i] = txt[i].replace("\n", "")
                if txt[i] == '': txt[i] = 'xxxxx'
                if '-------------------------' in txt[i]:
                    lines.append(int(i))
            nmq = len(lines)
            self.nmq.setText(str(nmq))

            columns = []
            typequestion = []
            for i in range(0, nmq):
                columns.append(txt[int(lines[i])-1])
                columns[i] = columns[i].replace(" ", "")
                typequestion.append(columns[i])

            for i in range(0,nmq):
                if typequestion[i] == 'xxxxx':
                    typequestion[i] = 'open'

            lines.append(int(row + 1))
            for i in range(0,nmq):
                question = 'question' + str(i + 1)
                vars()[question] = []
                txtclean = txt[int(lines[i]):int(lines[i + 1]-1)]
                for j in range(0,len(txtclean)):
                    if typequestion[i] != 'open' and len(txtclean[j]) != 1:
                        if txtclean[j][-2] == '|':
                            vars()[question].append(txtclean[j])
                    elif typequestion[i] == 'open':
                        vars()[question].append(txtclean[j])

            for i in range(0,nmq):
                options = []
                colquestion = []
                question = 'question' + str(i + 1)
                data = 'data' + str(i + 1)
                if typequestion[i] != 'open':
                    options.append('Aluno')
                    for j in typequestion[i]:
                        options.append(j + str(i + 1))
                    for j in range(0,len(vars()[question])):
                        colquestion.append(vars()[question][j][-len(options)*4:-3].replace(" ", "").split('|'))
                        vars()[question][j] = vars()[question][j][0:len(vars()[question][j])-(len(options)*4)-2]
                    vars()[data] = pd.DataFrame(colquestion, columns = options)
                    vars()[data] = vars()[data].replace("X", 1).replace("", 0)
                    vars()[data]["Aluno"] = vars()[question]
                elif typequestion[i] == 'open':
                    localvb = []
                    student = []
                    answer = []
                    for j in range(0,len(vars()[question])):
                        cont1 = 0
                        for w in vars()[question][j]:
                            cont1 += 1
                            if w == '|':
                                localvb.append(int(cont1))
                    mstcm = Counter(localvb).most_common()[0]
                    splitvb = mstcm[0]
                    nstudents = mstcm[1]
                    cont2 = 0
                    lineopen = vars()[question]
                    for j in range(0,len(lineopen)):
                        if len(lineopen[j]) > int(splitvb-1):
                            if lineopen[j][splitvb-1] == '|' and cont2 + 1 != nstudents:
                                student.append(lineopen[j][0:splitvb-2])
                                answer.append(lineopen[j][splitvb:len(lineopen[j])])
                                ex = 0
                                while ex == 0:
                                    if len(lineopen[j+1]) < int(splitvb-1) or lineopen[j+1][splitvb-1] != '|':
                                        if lineopen[j+1][0:len(lineopen[j+1])] != 'xxxxx':
                                            answer[cont2] = answer[cont2] + lineopen[j+1][0:len(lineopen[j+1])]
                                    else:
                                        ex = 1
                                    j += 1
                                cont2 += 1
                            elif lineopen[j][splitvb-1] == '|' and cont2 + 1 == nstudents:
                                student.append(lineopen[j][0:splitvb-2])
                                answer.append(lineopen[j][splitvb:len(lineopen[j])])
                                ex = 0
                                while ex == 0 and j <= len(lineopen[j]):
                                    if lineopen[j+1][0] != str(nmq) and lineopen[j+1] != 'xxxxx':
                                        if lineopen[j+1][0:len(lineopen[j+1])] != 'xxxxx':
                                            answer[cont2] = answer[cont2] + lineopen[j+1][0:len(lineopen[j+1])]
                                    else:
                                        ex = 1
                                    j += 1
                                cont2 += 1
                        vars()[data] = pd.DataFrame([], columns = ['Aluno', 'Resposta' + str(i + 1)])
                        vars()[data]["Aluno"] = student
                        vars()[data]["Resposta" + str(i + 1)] = answer
                        vars()[data] = vars()[data].replace('xxxxx', '')
                        
            a = 0
            b = 0
            for i in range(0,nmq):
                data = 'data' + str(i + 1)
                if typequestion[i] != 'open' and a == 0:
                    margedata = vars()[data]
                    a = 1
                elif typequestion[i] != 'open' and a == 1:
                    margedata = pd.merge(margedata, vars()[data], how = 'inner', on = 'Aluno', suffixes=(None, None))
                if typequestion[i] == 'open' and b == 0:
                    margeopen = vars()[data]
                    b = 1
                elif typequestion[i] == 'open' and b == 1:
                    margeopen = pd.merge(margeopen, vars()[data], how = 'inner', on = 'Aluno', suffixes=(None, None))
            if a == 1:
                margedata.insert(0, 'Numero', margedata["Aluno"])
                margedata["Numero"] = margedata["Numero"].str.lower()
                margedata["Numero"] = margedata["Numero"].str.replace('[^0-9]','')
                margedata["Numero"] = margedata["Numero"].str.strip()
                margedata["Numero"] = margedata["Numero"].replace('','N')
                margedata["Aluno"] = margedata["Aluno"].str.lower()
                margedata["Aluno"] = margedata["Aluno"].str.replace('[^a-záàâãéèêíïóôõöúçñ ]','')
                margedata["Aluno"] = margedata["Aluno"].str.strip()
                margedata["Aluno"] = margedata["Aluno"].str.title()
                margedata = margedata.drop_duplicates()
                margedata = margedata.sort_values(by=["Numero"], ascending=True)
            if b == 1:
                margeopen.insert(0, 'Numero', margeopen["Aluno"])
                margeopen["Numero"] = margeopen["Numero"].str.lower()
                margeopen["Numero"] = margeopen["Numero"].str.replace('[^0-9]','')
                margeopen["Numero"] = margeopen["Numero"].str.strip()
                margeopen["Numero"] = margeopen["Numero"].replace('','N')
                margeopen["Aluno"] = margeopen["Aluno"].str.lower()
                margeopen["Aluno"] = margeopen["Aluno"].str.replace('[^a-záàâãéèêíïóôõöúçñ ]','')
                margeopen["Aluno"] = margeopen["Aluno"].str.strip()
                margeopen["Aluno"] = margeopen["Aluno"].str.title()
                margeopen = margeopen.drop_duplicates()
                margeopen = margeopen.sort_values(by=["Numero"], ascending=True)

            if nmq >= 1:
                if typequestion[0] == 'open':
                    self.Q1.setEnabled(False)
                    self.q_1.setText('Aberta')
                else:
                    self.Q1.setEnabled(True)
                    self.q_1.setText('Objetiva')
            if nmq >= 2:
                if typequestion[1] == 'open':
                    self.Q2.setEnabled(False)
                    self.q_2.setText('Aberta')
                else:
                    self.Q2.setEnabled(True)
                    self.q_2.setText('Objetiva')
            if nmq >= 3:
                if typequestion[2] == 'open':
                    self.Q3.setEnabled(False)
                    self.q_3.setText('Aberta')
                else:
                    self.Q3.setEnabled(True)
                    self.q_3.setText('Objetiva')
            if nmq >= 4:
                if typequestion[3] == 'open':
                    self.Q4.setEnabled(False)
                    self.q_4.setText('Aberta')
                else:
                    self.Q4.setEnabled(True)
                    self.q_4.setText('Objetiva')
            if nmq >= 5:
                if typequestion[4] == 'open':
                    self.Q5.setEnabled(False)
                    self.q_5.setText('Aberta')
                else:
                    self.Q5.setEnabled(True)
                    self.q_5.setText('Objetiva')

            erro1 = 1

        
    def programa(self):
        erro2 = 0
        while erro2 == 0:
            global typequestion, nmq, margedata, margeopen
            # Abre diretorio para salvar resultados
            Tk().withdraw()
            salvar = dlg.asksaveasfilename(filetypes = (("Arquivos HTML","*.html"),("Arquivos EXCEL","*.xlsx"),("Arquivos","*")))
            if salvar[-5::] == '.html' or salvar[-5::] == '.xlsx':
                salvar = salvar[:-5]
            elif salvar == '':
                messagebox.showwarning('Aviso', 'Digite o nome do arquivo que deseja salvar.')
                break

            # Valor da questão
            qv = []
            if nmq >= 1: 
                if typequestion[0] != 'open':
                    qv1 = self.qv_1.text()
                    if qv1 == "": 
                        messagebox.showwarning('Aviso', 'Insira o valor da Questão 1')
                        break
                    qv.append(qv1.replace(',','.'))
            if nmq >= 2: 
                if typequestion[1] != 'open':
                    qv2 = self.qv_2.text()
                    if qv2 == "": 
                        messagebox.showwarning('Aviso', 'Insira o valor da Questão 2')
                        break
                    qv.append(qv2.replace(',','.'))
            if nmq >= 3: 
                if typequestion[2] != 'open':
                    qv3 = self.qv_3.text()
                    if qv3 == "": 
                        messagebox.showwarning('Aviso', 'Insira o valor da Questão 3')
                        break
                    qv.append(qv3.replace(',','.'))
            if nmq >= 4: 
                if typequestion[3] != 'open':
                    qv4 = self.qv_4.text()
                    if qv4 == "": 
                        messagebox.showwarning('Aviso', 'Insira o valor da Questão 4')
                        break
                    qv.append(qv4.replace(',','.'))
            if nmq >= 5: 
                if typequestion[4] != 'open':
                    qv5 = self.qv_5.text()
                    if qv5 == "": 
                        messagebox.showwarning('Aviso', 'Insira o valor da Questão 5')
                        break
                    qv.append(qv5.replace(',','.'))
            qv = pd.to_numeric(qv)

            #Opções corretas
            qa1 = []
            qa2 = []
            qa3 = []
            qa4 = []
            qa5 = []
            qa = []
            if nmq >= 1: 
                if typequestion[0] != 'open':
                    if self.a_1.isChecked(): qa1.append(1)
                    else: qa1.append(0)
                    if self.b_1.isChecked(): qa1.append(1)
                    else: qa1.append(0)
                    if self.c_1.isChecked(): qa1.append(1)
                    else: qa1.append(0)
                    if self.d_1.isChecked(): qa1.append(1)
                    else: qa1.append(0)
                    if self.e_1.isChecked(): qa1.append(1)
                    else: qa1.append(0)
                    if sum(qa1) == 0: 
                        messagebox.showwarning('Aviso', 'Assinale a(s) alternativa(s) corretas(s) da Questão 1')
                        break
                    qa1 = pd.to_numeric(qa1)
                    qa.extend(qa1[0:len(typequestion[0])]*qv[0]/sum(qa1))
            if nmq >= 2: 
                if typequestion[1] != 'open':
                    if self.a_2.isChecked(): qa2.append(1)
                    else: qa2.append(0)
                    if self.b_2.isChecked(): qa2.append(1)
                    else: qa2.append(0)
                    if self.c_2.isChecked(): qa2.append(1)
                    else: qa2.append(0)
                    if self.d_2.isChecked(): qa2.append(1)
                    else: qa2.append(0)
                    if self.e_2.isChecked(): qa2.append(1)
                    else: qa2.append(0)
                    if sum(qa2) == 0: 
                        messagebox.showwarning('Aviso', 'Assinale a(s) alternativa(s) corretas(s) da Questão 1')
                        break
                    qa2 = pd.to_numeric(qa2)
                    qa.extend(qa2[0:len(typequestion[1])]*qv[1]/sum(qa2))
            if nmq >= 3: 
                if typequestion[2] != 'open':
                    if self.a_3.isChecked(): qa3.append(1)
                    else: qa3.append(0)
                    if self.b_3.isChecked(): qa3.append(1)
                    else: qa3.append(0)
                    if self.c_3.isChecked(): qa3.append(1)
                    else: qa3.append(0)
                    if self.d_3.isChecked(): qa3.append(1)
                    else: qa3.append(0)
                    if self.e_3.isChecked(): qa3.append(1)
                    else: qa3.append(0)
                    if sum(qa3) == 0: 
                        messagebox.showwarning('Aviso', 'Assinale a(s) alternativa(s) corretas(s) da Questão 1')
                        break
                    qa3 = pd.to_numeric(qa3)
                    qa.extend(qa3[0:len(typequestion[2])]*qv[2]/sum(qa3))
            if nmq >= 4: 
                if typequestion[3] != 'open':
                    if self.a_4.isChecked(): qa4.append(1)
                    else: qa4.append(0)
                    if self.b_4.isChecked(): qa4.append(1)
                    else: qa4.append(0)
                    if self.c_4.isChecked(): qa4.append(1)
                    else: qa4.append(0)
                    if self.d_4.isChecked(): qa4.append(1)
                    else: qa4.append(0)
                    if self.e_4.isChecked(): qa4.append(1)
                    else: qa4.append(0)
                    if sum(qa4) == 0: 
                        messagebox.showwarning('Aviso', 'Assinale a(s) alternativa(s) corretas(s) da Questão 1')
                        break
                    qa4 = pd.to_numeric(qa4)
                    qa.extend(qa4[0:len(typequestion[3])]*qv[3]/sum(qa4))
            if nmq >= 5: 
                if typequestion[4] != 'open':
                    if self.a_5.isChecked(): qa5.append(1)
                    else: qa5.append(0)
                    if self.b_5.isChecked(): qa5.append(1)
                    else: qa5.append(0)
                    if self.c_5.isChecked(): qa5.append(1)
                    else: qa5.append(0)
                    if self.d_5.isChecked(): qa5.append(1)
                    else: qa5.append(0)
                    if self.e_5.isChecked(): qa5.append(1)
                    else: qa5.append(0)
                    if sum(qa5) == 0: 
                        messagebox.showwarning('Aviso', 'Assinale a(s) alternativa(s) corretas(s) da Questão 1')
                        break
                    qa5 = pd.to_numeric(qa5)
                    qa.extend(qa5[0:len(typequestion[4])]*qv[4]/sum(qa5))
            qa = pd.to_numeric(qa)
            
            # Correção para questões bjetivas
            if a == 1: 
                score = []
                for i in range(0, len(margedata)):
                    check = margedata.iloc[i]
                    check = pd.to_numeric(check[2:])
                    score.append(sum(check*qa))
                margedata = margedata.replace(1,'X').replace(0,' ')
                margedata["Nota"] = score
                feed = ['-'] + ['GABARITO'] + list(qa) + [sum(qa)]
                feed = pd.DataFrame(feed).T
                feed.columns = margedata.columns
                margedata = margedata.append(feed, ignore_index = True)
                margedata = margedata.drop_duplicates()

                #Gerando resultados das questões objetivas  
                obj = margedata[["Numero", "Aluno", "Nota"]]
                obj.insert(3, 'Nota (Abertas)', 0)
                obj.insert(4, 'Nota Final', 0)
                for i in range(0,len(obj)):
                    obj.loc[[i],["Nota Final"]] = '=C' + str(i+2) + '+D' + str(i+2)
            else:
                margedata = 'Esta prova não possui questões objetivas'
                obj = 'Esta prova não possui questões objetivas'

            exfile = pd.ExcelWriter(salvar + '.xlsx')
            if a == 1:
                obj.to_excel(exfile, 'Questões Objetivas', startrow=0, startcol=0, header=True, index=False)
            
            html = open(salvar + '.html', 'w')
            html.write('<h1 style="color: #5e9ca0; text-align: center;"><span style="color: #008000;">CORRE&Ccedil;&Atilde;O DA PROVA</span>\
            </h1><hr /><ul><li><h2><strong>Relat&oacute;rio das quest&otilde;es objetivas:</strong></h2>')
            if a == 1:
                html.write(margedata.to_html(index=False))
            else:
                html.write(margedata)
            html.write('</li></ul><p>&nbsp;</p><hr /><ul><li><h2><strong>Relat&oacute;rio das quest&otilde;es abertas:</strong></h2>')

            # Correção para questões abertas
            for i in range(0,nmq):
                if typequestion[i] == 'open':
                    openq = margeopen[["Numero", "Aluno", "Resposta" + str(i + 1)]]
                    openq = openq.drop_duplicates()
                    openq = openq.sort_values(by=['Numero'], ascending=True)
                    html.write('</li></ul><h3>&nbsp; &nbsp; &nbsp; &nbsp;Quest&atilde;o ' + str(i + 1) + '</h3>')
                    html.write(openq.to_html(index=False))
                    openq.to_excel(exfile, 'Questão Aberta ' + str(i + 1), startrow=0, startcol=0, header=True, index=False)
            
            html.write('<p>&nbsp;</p><p>&nbsp;</p><pre><span style="background-color: #ffffff;">O programa CrWebex foi desenvolvido por Jo&atilde;o Pedro C. Moreira (<a style="background-color: #ffffff;" href="mailto:mcjpedro@gmail.com">mcjpedro@gmail.com</a>)</span></pre>')
            html.close()
            exfile.close()
            self.exibir.setText('- A CORREÇÃO FOI EFETUADA COM SUCESSO!\n\n- O arquivo Excel foi salvo como:\n    ' + salvar + '.xlsx\
                \n- O relatório HTML foi salvo como:\n    ' + salvar + '.html')
            erro2 = 1
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Programa = QtWidgets.QMainWindow()
    ui = Ui_Programa()
    ui.setupUi(Programa)
    Programa.show()
    sys.exit(app.exec_())