import threading
import time

# bandera para indicar si los hilos deben detenerse
stop_threads = False


def prepareMate():
    print("Start prepareMate()")
    global stop_threads              # Accede a la variable global
    while not stop_threads:
        time.sleep(1)                # Simula una operación en bucle
    print("End prepareMate()")
    return "Mate is ready"


def buyFacturas():
    print("Start buyFacturas()")
    global stop_threads             
    while not stop_threads:
        time.sleep(1)  
    print("End buyFacturas()")
    return "Facturas are ready"

# unción principal
def main():
    global stop_threads  

    try:
        start_time = time.time()

        # Crea dos hilos para ejecutar prepareMate y buyFacturas
        thread1 = threading.Thread(target=prepareMate)
        thread2 = threading.Thread(target=buyFacturas)

        # Inicia ambos hilos
        thread1.start()
        thread2.start()

        # Espera a que el usuario presione Ctrl+C para detener los hilos
        while True:
            time.sleep(1)  # Espera en bucle
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping threads...")
        stop_threads = True  # Cambia la bandera para detener los hilos

        # Espera a que ambos hilos terminen
        thread1.join()
        thread2.join()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total elapsed time: {elapsed_time:.2f} seconds")

# Ejecuta la función principal si este script se está ejecutando directamente
if __name__ == "__main__":
    main()
