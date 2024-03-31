#Codigo por Hekebris y Señor Gato
#Señor gato hizo todo
#221802921
#2024A I5904 SSP de Uso Adaptacion y Explotacion de Sistemas OperativosI5904



import os
import random
import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def reiniciar_programa(self):
        os.execv(sys.executable, [sys.executable] + sys.argv)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1047, 723)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(670, 680, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.reiniciar_programa)  # Conectar el botón Ok a la función de reiniciar_programa
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(110, 110, 100, 100))
        self.label_1.setScaledContents(True)  # Ajustar imagen al tamaño del label
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 110, 100, 100))
        self.label_2.setScaledContents(True)  # Ajustar imagen al tamaño del label
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(480, 110, 100, 100))
        self.label_3.setScaledContents(True)  # Ajustar imagen al tamaño del label
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(670, 110, 100, 100))
        self.label_4.setScaledContents(True)  # Ajustar imagen al tamaño del label
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(840, 110, 100, 100))
        self.label_5.setScaledContents(True)  # Ajustar imagen al tamaño del label
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 400, 100, 100))
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(480, 400, 100, 100))
        self.label_6.setObjectName("label_6")
        self.label_6.setScaledContents(True)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(760, 400, 100, 100))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(220, 560, 100, 100))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(470, 560, 100, 100))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(750, 560, 100, 100))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Cargar imágenes de los gatos
        self.cargar_imagenes()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Gato 1"))
        self.label_2.setText(_translate("Dialog", "Gato 2"))
        self.label_3.setText(_translate("Dialog", "Gato 3"))
        self.label_4.setText(_translate("Dialog", "Gato 4"))
        self.label_5.setText(_translate("Dialog", "Gato 5"))
        self.label.setText(_translate("Dialog", "Plato 1"))
        self.label_6.setText(_translate("Dialog", "Plato 2"))
        self.label_7.setText(_translate("Dialog", "Plato 3"))
        self.label_8.setText(_translate("Dialog", "Gato_Comiendo_1"))
        self.label_9.setText(_translate("Dialog", "Gato_Comiendo_2"))
        self.label_10.setText(_translate("Dialog", "Gato_Comiendo_3"))
    
    def cargar_imagenes(self):
        # Cargar imágenes de los gatos
        self.plato_pixmap = QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "plato.jpg"))
        
        # Asignar la misma imagen a los labels de los platos
        self.label.setPixmap(self.plato_pixmap)
        self.label_6.setPixmap(self.plato_pixmap)
        self.label_7.setPixmap(self.plato_pixmap)
        self.label_8.setPixmap(QtGui.QPixmap())  # Inicialmente vacío
        self.label_9.setPixmap(QtGui.QPixmap())  # Inicialmente vacío
        self.label_10.setPixmap(QtGui.QPixmap())  # Inicialmente vacío
        self.gato_pixmaps = []
        for i in range(1, num_gatos + 1):
            imagen_path = os.path.join(os.path.dirname(__file__), f"gato{i}.jpg")
            if os.path.isfile(imagen_path):
                pixmap = QtGui.QPixmap(imagen_path)
                self.gato_pixmaps.append(pixmap)
            else:
                print(f"La imagen gato{i}.jpg no se encontró en el directorio actual.")

               # Asignar imágenes a los labels
        self.label_1.setPixmap(self.gato_pixmaps[0] if self.gato_pixmaps else QtGui.QPixmap())
        self.label_2.setPixmap(self.gato_pixmaps[1] if len(self.gato_pixmaps) > 1 else QtGui.QPixmap())
        self.label_3.setPixmap(self.gato_pixmaps[2] if len(self.gato_pixmaps) > 2 else QtGui.QPixmap())
        self.label_4.setPixmap(self.gato_pixmaps[3] if len(self.gato_pixmaps) > 3 else QtGui.QPixmap())
        self.label_5.setPixmap(self.gato_pixmaps[4] if len(self.gato_pixmaps) > 4 else QtGui.QPixmap())

    def mostrar_gato_comiendo(self, nombre_gato, mostrar=True):
        
        if nombre_gato == "Gato 1":
            self.label_8.setPixmap(self.gato_pixmaps[0] if mostrar else QtGui.QPixmap())
        elif nombre_gato == "Gato 2":
            self.label_9.setPixmap(self.gato_pixmaps[1] if mostrar else QtGui.QPixmap())
        elif nombre_gato == "Gato 3":
            self.label_10.setPixmap(self.gato_pixmaps[2] if mostrar else QtGui.QPixmap())
        elif nombre_gato == "Gato 4":
            self.label_8.setPixmap(self.gato_pixmaps[3] if mostrar else QtGui.QPixmap())
        elif nombre_gato == "Gato 5":
            self.label_9.setPixmap(self.gato_pixmaps[4] if mostrar else QtGui.QPixmap())

# Número de gatos y platos de comida
num_gatos = 5
num_platos = 3

# Semáforo para controlar el acceso a los platos
semaforo = threading.Semaphore(num_platos)

# Función que simula un gato comiendo
def comer_gato(nombre_gato):
    # Adquirir el semáforo (esperar si es necesario)
    semaforo.acquire()
    
    # Mostrar al gato comiendo
    ui.mostrar_gato_comiendo(nombre_gato, mostrar=True)

    # Simular el tiempo que tarda en comer
    tiempo_comer = random.uniform(4, 7)
    time.sleep(tiempo_comer)
    print(f"El gato {nombre_gato} está comiendo. Tiempo: {tiempo_comer:.2f} segundos")

    # Ocultar al gato después de comer
    ui.mostrar_gato_comiendo(nombre_gato, mostrar=False)

    # Liberar el semáforo
    semaforo.release()

# Función para ejecutar el programa
def ejecutar_programa():
    # Crear una lista para almacenar todos los hilos de los gatos
    hilos_gatos = []

    # Crear y agregar los hilos de los gatos a la lista
    for i in range(num_gatos):
        hilo = threading.Thread(target=comer_gato, args=(f"Gato {i+1}",))
        hilos_gatos.append(hilo)

    # Iniciar todos los hilos de los gatos simultáneamente
    for hilo in hilos_gatos:
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos_gatos:
        hilo.join()

    print("Todos los gatos han comido.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    # Ejecutar los hilos en un hilo secundario
    t = threading.Thread(target=ejecutar_programa)
    t.start()

    sys.exit(app.exec_())

