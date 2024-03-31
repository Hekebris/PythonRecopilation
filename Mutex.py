import threading

# Definir los estados de los filósofos
THINKING = 0
HUNGRY = 1
EATING = 2

estados = [THINKING] * 5
mutex = threading.Semaphore(1)
condiciones = [threading.Condition() for _ in range(5)]
palillos = [threading.Semaphore(1) for _ in range(5)]  # Representación de los palillos

# Función para que un filósofo intente comer
def filosofo(filosofo_id):
    while True:
        pensar(filosofo_id)
        comer(filosofo_id)

def pensar(filosofo_id):
    print(f"Filósofo {filosofo_id} está pensando.")

def comer(filosofo_id):
    global estados

    mutex.acquire()
    estados[filosofo_id] = HUNGRY
    probar(filosofo_id)
    mutex.release()

    condiciones[filosofo_id].acquire()
    while estados[filosofo_id] != EATING:
        condiciones[filosofo_id].wait()
    condiciones[filosofo_id].release()

    print(f"Filósofo {filosofo_id} está comiendo.")

    mutex.acquire()
    estados[filosofo_id] = THINKING
    probar((filosofo_id + 4) % 5)
    probar((filosofo_id + 1) % 5)
    mutex.release()

def probar(filosofo_id):
    global estados
    global condiciones
    global palillos

    if estados[filosofo_id] == HUNGRY and estados[(filosofo_id + 4) % 5] != EATING and estados[(filosofo_id + 1) % 5] != EATING:
        estados[filosofo_id] = EATING
        condiciones[filosofo_id].acquire()
        condiciones[filosofo_id].notify()
        condiciones[filosofo_id].release()

# Crear e iniciar los hilos para cada filósofo
filosofos = []
for i in range(5):
    filosofo_thread = threading.Thread(target=filosofo, args=(i,))
    filosofos.append(filosofo_thread)
    filosofo_thread.start()

# Esperar a que todos los hilos terminen
for filosofo_thread in filosofos:
    filosofo_thread.join()