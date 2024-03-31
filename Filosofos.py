# -*- coding: utf-8 -*-
#Borre los creditos de Pyqt y no se que decian jajaja
#Codigo por Hekebris, es un codigo cuántico, a veces funciona y a veces no

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import threading
import sys
import time

# Form implementation generated from reading ui file 'Interfaz_Filosofos.ui'
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(930, 726)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(580, 690, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        factor_escala=7;
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(320, 550, 47*factor_escala, 13*factor_escala))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 300, 47*factor_escala, 13*factor_escala))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(580, 550, 47*factor_escala, 13*factor_escala))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(680, 290, 47*factor_escala, 13*factor_escala))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(450, 110, 47*factor_escala, 13*factor_escala))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 330, 47, 13))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Problema de los filósofos"))
        self.label_1.setText(_translate("Dialog", "filo 4"))
        self.label_2.setText(_translate("Dialog", "filo 5"))
        self.label_3.setText(_translate("Dialog", "filo 3"))
        self.label_4.setText(_translate("Dialog", "filo 2"))
        self.label_5.setText(_translate("Dialog", "filo 1"))
        self.label_6.setText(_translate("Dialog", "mesa"))

# Definir los estados de los filósofos
THINKING = 0
HUNGRY = 1
EATING = 2

estados = [THINKING] * 5
mutex = threading.Semaphore(1)
condiciones = [threading.Condition() for _ in range(5)]
palillos = [threading.Semaphore(1) for _ in range(5)]  # Representación de los palillos

# Función para que un filósofo intente comer
def filosofo(filosofo_id, ventana):
    while True:
        pensar(filosofo_id, ventana)
        comer(filosofo_id, ventana)

def pensar(filosofo_id, ventana):
    print(f"Filósofo {filosofo_id} está pensando.")
    time.sleep(0.5)

    # Actualizar imágenes de los labels
    ventana.actualizar_colores()

def probar(filosofo_id):
    global estados
    global condiciones
    global palillos

    if estados[filosofo_id] == HUNGRY and estados[(filosofo_id + 4) % 5] != EATING and estados[(filosofo_id + 1) % 5] != EATING:
        estados[filosofo_id] = EATING
        condiciones[filosofo_id].acquire()
        condiciones[filosofo_id].notify()
        condiciones[filosofo_id].release()

def comer(filosofo_id, ventana):
    global estados

    mutex.acquire()
    estados[filosofo_id] = HUNGRY
    probar(filosofo_id)
    mutex.release()

    condiciones[filosofo_id].acquire()
    while estados[filosofo_id] != EATING:
        condiciones[filosofo_id].wait()
    condiciones[filosofo_id].release()

    # Adquirir los palillos
    palillo_izquierdo = filosofo_id
    palillo_derecho = (filosofo_id + 1) % 5
    palillos[palillo_izquierdo].acquire()
    palillos[palillo_derecho].acquire()

    print(f"Filósofo {filosofo_id} está comiendo.")
    time.sleep(1)

    # Actualizar imágenes de los labels
    ventana.actualizar_colores()

    # Liberar los palillos
    palillos[palillo_izquierdo].release()
    palillos[palillo_derecho].release()

    mutex.acquire()
    estados[filosofo_id] = THINKING
    probar((filosofo_id + 4) % 5)
    probar((filosofo_id + 1) % 5)
    mutex.release()

    # Actualizar imágenes de los labels
    ventana.actualizar_colores()

class FilosofoThread(QtCore.QThread):
    def __init__(self, filosofo_id, ventana):
        super().__init__()
        self.filosofo_id = filosofo_id
        self.ventana = ventana

    def run(self):
        filosofo(self.filosofo_id, self.ventana)

class VentanaFilosofos(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_1 = self.findChild(QtWidgets.QLabel, "label_1")
        self.label_2 = self.findChild(QtWidgets.QLabel, "label_2")
        self.label_3 = self.findChild(QtWidgets.QLabel, "label_3")
        self.label_4 = self.findChild(QtWidgets.QLabel, "label_4")
        self.label_5 = self.findChild(QtWidgets.QLabel, "label_5")

        self.pensando_icon = QtGui.QIcon('pensando.jpg')
        self.esperando_icon = QtGui.QIcon('esperando.jpg')
        self.comiendo_icon = QtGui.QIcon('comiendo.jpg')

        # Crear e iniciar los hilos para cada filósofo
        self.filosofos = []
        for i in range(5):
            filosofo_thread = FilosofoThread(i, self)
            self.filosofos.append(filosofo_thread)
            filosofo_thread.start()

    def actualizar_colores(self):
        for i in range(5):
            label = getattr(self, f"label_{i + 1}")
            if estados[i] == EATING:
                label.setPixmap(self.comiendo_icon.pixmap(label.size()))
            elif estados[i] == THINKING:
                label.setPixmap(self.pensando_icon.pixmap(label.size()))
            else:
                label.setPixmap(self.esperando_icon.pixmap(label.size()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaFilosofos()
    ventana.show()
    sys.exit(app.exec_())
