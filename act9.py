# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz_Procesos_Subprocesos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time
import sys
from collections import namedtuple

# Definir una namedtuple llamada Proceso para representar un proceso con nombre y propiedade
Proceso = namedtuple('Proceso', ['nombre', 'propiedades'])

# Clase que define la interfaz gráfica utilizando PyQt5
class Ui_Dialog(object):
    def setupUi(self, Dialog,random_names):
        Dialog.setObjectName("Dialog")
        Dialog.resize(711, 492)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(480, 450, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 531, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 40, 531, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(10, 70, 531, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_4.setGeometry(QtCore.QRect(10, 100, 531, 23))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        
        self.progress_bars = {
            random_names[0]: self.progressBar,
            random_names[1]: self.progressBar_2,
            random_names[2]: self.progressBar_3,
            random_names[3]: self.progressBar_4
        }
        
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 240, 71, 31))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 280, 71, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 320, 71, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 360, 71, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 400, 71, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 240, 71, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 280, 71, 31))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 320, 71, 31))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(90, 360, 71, 31))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 400, 71, 31))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(170, 240, 71, 31))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(170, 280, 71, 31))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(170, 320, 71, 31))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(170, 360, 71, 31))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(170, 400, 71, 31))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(330, 240, 71, 31))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(330, 280, 71, 31))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_18.setGeometry(QtCore.QRect(330, 320, 71, 31))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_19.setGeometry(QtCore.QRect(330, 360, 71, 31))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_20.setGeometry(QtCore.QRect(330, 400, 71, 31))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_21.setGeometry(QtCore.QRect(410, 240, 71, 31))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_22.setGeometry(QtCore.QRect(410, 280, 71, 31))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_23.setGeometry(QtCore.QRect(410, 320, 71, 31))
        self.lineEdit_23.setText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_24.setGeometry(QtCore.QRect(410, 360, 71, 31))
        self.lineEdit_24.setText("")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_25.setGeometry(QtCore.QRect(410, 400, 71, 31))
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_28 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_28.setGeometry(QtCore.QRect(550, 10, 101, 20))
        self.lineEdit_28.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_29.setGeometry(QtCore.QRect(550, 40, 101, 20))
        self.lineEdit_29.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_30.setGeometry(QtCore.QRect(550, 70, 101, 20))
        self.lineEdit_30.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_31 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_31.setGeometry(QtCore.QRect(550, 100, 101, 20))
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_32 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_32.setGeometry(QtCore.QRect(70, 200, 111, 20))
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_33 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_33.setGeometry(QtCore.QRect(420, 200, 111, 20))
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_34.setGeometry(QtCore.QRect(490, 240, 71, 31))
        self.lineEdit_34.setText("")
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_35 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_35.setGeometry(QtCore.QRect(490, 280, 71, 31))
        self.lineEdit_35.setText("")
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_36.setGeometry(QtCore.QRect(490, 320, 71, 31))
        self.lineEdit_36.setText("")
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_37 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_37.setGeometry(QtCore.QRect(490, 360, 71, 31))
        self.lineEdit_37.setText("")
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_38 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_38.setGeometry(QtCore.QRect(490, 400, 71, 31))
        self.lineEdit_38.setText("")
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_39 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_39.setGeometry(QtCore.QRect(570, 240, 71, 31))
        self.lineEdit_39.setText("")
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_40 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_40.setGeometry(QtCore.QRect(570, 280, 71, 31))
        self.lineEdit_40.setText("")
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_41 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_41.setGeometry(QtCore.QRect(570, 320, 71, 31))
        self.lineEdit_41.setText("")
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_42 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_42.setGeometry(QtCore.QRect(570, 360, 71, 31))
        self.lineEdit_42.setText("")
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_43 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_43.setGeometry(QtCore.QRect(570, 400, 71, 31))
        self.lineEdit_43.setText("")
        self.lineEdit_43.setObjectName("lineEdit_43")

        self.retranslateUi(Dialog,random_names)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog,random_names):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_28.setText(_translate("Dialog", random_names[0]))
        self.lineEdit_29.setText(_translate("Dialog", random_names[1]))
        self.lineEdit_30.setText(_translate("Dialog", random_names[2]))
        self.lineEdit_31.setText(_translate("Dialog", random_names[3]))
        self.lineEdit_32.setText(_translate("Dialog", "Real"))
        self.lineEdit_33.setText(_translate("Dialog", "Virtual"))

# Clase que maneja la asignación de memoria real
class MemoryManagerReal:
    def __init__(self, memoria_total):
        self.memoria_total = memoria_total
        self.memoria_libre = memoria_total
        self.espacios_llenos = set()

    def agregar_a_memoria_real(self, size):
        if self.memoria_libre >= size:
            self.espacios_llenos.add(size)
            self.memoria_libre -= size
            return True
        raise MemoryError("No hay suficiente memoria disponible.")


#Lo intente, lo juro, memoria virtual
class MemoryManagerVirtual:
    def __init__(self, memoria_total):
        self.memoria_total = memoria_total
        self.paginas = {}  # Tabla de páginas (página virtual: contenido)
        self.tamano_pagina = 10  # Tamaño de página en unidades
        self.memoria = [0] * memoria_total

    def cargar_pagina(self, pagina_virtual):
        if pagina_virtual in self.paginas:
            return self.paginas[pagina_virtual]
        else:
            raise ErrorDeFalloDePagina(pagina_virtual)

    def almacenar_pagina(self, pagina_virtual, contenido):
        self.paginas[pagina_virtual] = contenido

class ErrorDeFalloDePagina(Exception):
    def __init__(self, pagina_virtual):
        self.pagina_virtual = pagina_virtual
 

# Función para generar propiedades aleatorias para un proceso        
def generar_propiedades_aleatorias():
    return {
        "tamaño": 10,
        "procesos": random.randint(2,9),
        # Agrega cualquier otra propiedad 
    } 

      
#ESTO SIRVE PARA ASIGNAR MEMORIA REAL EN TRHEAD, CHAT GPT HIZO COSAS
# Clase que representa un hilo para la asignación de memoria
class AsignacionMemoriaThread(QtCore.QThread):
    proceso_counter = 1  # Contador global para el nombre de los procesos
    

    def __init__(self, proceso, memory_manager_real, ui):
        super().__init__()
        self.proceso = proceso
        self.memory_manager_real = memory_manager_real
        self.ui = ui
        self.proceso_index = None

    def run(self):
        for _ in range(self.proceso.propiedades['procesos']):
            if self.proceso.propiedades['tamaño'] <= self.memory_manager_real.memoria_libre:
                self.memory_manager_real.agregar_a_memoria_real(self.proceso.propiedades['tamaño'])
                
                # Obtener el nombre del proceso y el índice del lineEdit_1
                proceso_nombre = self.proceso.nombre
                self.proceso_index = AsignacionMemoriaThread.proceso_counter
                AsignacionMemoriaThread.proceso_counter += 1
                
                # Actualizar el texto del lineEdit_1 correspondiente con el nombre del proceso
                line_edit_name = getattr(self.ui, f"lineEdit_{self.proceso_index}")
                line_edit_name.setText(proceso_nombre)
                
                # También puedes imprimir el mensaje en la consola si lo necesitas
                print(f"{proceso_nombre} asignado a memoria real. Se ocuparon {self.proceso.propiedades['tamaño']}")
                
                # Obtener la barra de progreso correspondiente al proceso
                progress_bar = self.ui.progress_bars[self.proceso.nombre]
                progress_bar.setValue((progress_bar.value() + (100 / self.proceso.propiedades['procesos'])))
                
                time.sleep(1.5)  # Simular operación de E/S
            else:
                proceso_nombre = self.proceso.nombre
                self.proceso_index = AsignacionMemoriaThread.proceso_counter
                AsignacionMemoriaThread.proceso_counter += 1
                if AsignacionMemoriaThread.proceso_counter == 26:
                    AsignacionMemoriaThread.proceso_counter = 34
                
                # Actualizar el texto del lineEdit_1 correspondiente con el nombre del proceso
                line_edit_name = getattr(self.ui, f"lineEdit_{self.proceso_index}")
                line_edit_name.setText(proceso_nombre)
                
                # También puedes imprimir el mensaje en la consola si lo necesitas
                print(f"{proceso_nombre} asignado a memoria virtual. Se ocuparon {self.proceso.propiedades['tamaño']}")
                # Obtener la barra de progreso correspondiente al proceso
                progress_bar = self.ui.progress_bars[self.proceso.nombre]
                progress_bar.setValue((progress_bar.value() + (100 / self.proceso.propiedades['procesos'])))
                print(f"No hay suficiente espacio para {self.proceso.nombre} en memoria real. Yendo a la virtual")
                

                
# Clase que representa un proceso                
class Proceso:
    def __init__(self, nombre, propiedades):
        self.nombre = nombre
        self.propiedades = propiedades   
        
# Función principal que ejecuta la aplicación        
if __name__ == "__main__":
    
    line_edits_range = ["lineEdit_1", "lineEdit_2", "lineEdit_3", "lineEdit_4", "lineEdit_5", "lineEdit_6", "lineEdit_7", "lineEdit_8", "lineEdit_9", "lineEdit_10", "lineEdit_11", "lineEdit_12", "lineEdit_13", "lineEdit_14", "lineEdit_15", "lineEdit_16", "lineEdit_17", "lineEdit_18", "lineEdit_19", "lineEdit_20", "lineEdit_21", "lineEdit_22", "lineEdit_23", "lineEdit_24", "lineEdit_25","lineEdit_34", "lineEdit_35", "lineEdit_36", "lineEdit_37", "lineEdit_38", "lineEdit_39", "lineEdit_40", "lineEdit_41", "lineEdit_42", "lineEdit_43"]
    software_names = ["Photoshop", "Visual Studio", "Duolingo", "Illustrator", "Eclipse", "Premiere Pro", "Unity", "AutoCAD"]
    random_names = random.sample(software_names, 4)
    proceso1,proceso2,proceso3,proceso4 = random_names
    procesos = [Proceso(nombre, generar_propiedades_aleatorias()) for nombre in random_names]
    memory_manager_real = MemoryManagerReal(memoria_total=150)
    memory_manager_virtual = MemoryManagerVirtual(memoria_total=200)
    print(memory_manager_real.memoria_libre)
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog,random_names)
    Dialog.show()
    QtWidgets.QApplication.processEvents()
    threads = []
    for proceso in procesos:
        thread = AsignacionMemoriaThread(proceso, memory_manager_real, ui)
        time.sleep(0.2)
        threads.append(thread)
        thread.start()
        QtWidgets.QApplication.processEvents()
        
        
    # Esperar a que todos los threads terminen antes de continuar
    for thread in threads:
        time.sleep(0.2)
        QtWidgets.QApplication.processEvents() 

        thread.wait()
        

    
    print(memory_manager_real.memoria_libre)
     
    sys.exit(app.exec_())

