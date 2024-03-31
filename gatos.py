# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:45:06 2024

@author: Heke
"""
import threading
import random
import time

# Número de gatos y platos de comida
num_gatos = 5
num_platos = 3

# Semáforo para controlar el acceso a los platos
semaforo = threading.Semaphore(num_platos)

# Función que simula un gato comiendo
def comer_gato(nombre_gato):
    # Adquirir el semáforo (esperar si es necesario)
    with semaforo:
        # Simular el tiempo que tarda en comer
        tiempo_comer = random.uniform(1, 3)
        time.sleep(tiempo_comer)
        print(f"El gato {nombre_gato} está comiendo. Tiempo: {tiempo_comer:.2f} segundos")

# Función para ejecutar el programa
def ejecutar_programa():
    # Crear y comenzar los hilos (gatos)
    hilos_gatos = []
    for i in range(num_gatos):
        hilo = threading.Thread(target=comer_gato, args=(f"Gato {i+1}",))
        hilos_gatos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos_gatos:
        hilo.join()

    print("Todos los gatos han comido.")

# Ejemplo de uso
ejecutar_programa()
