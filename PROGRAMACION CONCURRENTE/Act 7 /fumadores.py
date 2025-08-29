import threading
import random
import time

# Semáforos para la disponibilidad de ingredientes
tabaco = threading.Semaphore(0)
papel = threading.Semaphore(0)
fósforos = threading.Semaphore(0)

# Semáforo para la acción del agente
mutex = threading.Semaphore(1)

# Función para los fumadores
def fumador(ingrediente):
    while True:
        if ingrediente == 'tabaco':
            tabaco.acquire()  # Espera si no hay tabaco
            print(f"Fumador con {ingrediente} empieza a fumar")
        elif ingrediente == 'papel':
            papel.acquire()  # Espera si no hay papel
            print(f"Fumador con {ingrediente} empieza a fumar")
        else:
            fósforos.acquire()  # Espera si no hay fósforos
            print(f"Fumador con {ingrediente} empieza a fumar")

        # Fumar durante un tiempo
        time.sleep(random.randint(1, 3))
        print(f"Fumador con {ingrediente} terminó de fumar\n")

# Función para el agente
def agente():
    while True:
        # El agente coloca dos ingredientes al azar en la mesa
        ingrediente = random.choice(['tabaco', 'papel', 'fósforos'])
        if ingrediente == 'tabaco':
            papel.release()
            fósforos.release()
        elif ingrediente == 'papel':
            tabaco.release()
            fósforos.release()
        else:
            tabaco.release()
            papel.release()
        
        print(f"Agente puso {ingrediente} en la mesa.")
        time.sleep(random.randint(1, 3))

# Crear y ejecutar los hilos
def main():
    threads = []

    # Crear los hilos para los fumadores
    for ingrediente in ['tabaco', 'papel', 'fósforos']:
        t = threading.Thread(target=fumador, args=(ingrediente,))
        threads.append(t)
        t.start()

    # Crear y ejecutar el hilo para el agente
    t_agente = threading.Thread(target=agente)
    threads.append(t_agente)
    t_agente.start()

    # Esperar a que todos los hilos terminen
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
