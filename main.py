#Este es un ejemplo de un programa que no utiliza hilos (threads), las funciones prepareMate() y buyFacturas() se ejecutan de manera secuencial, una después de la otra.
# el programa espera a que prepareMate() termine completamente antes de comenzar buyFacturas().
#Este enfoque secuencial resulta en un tiempo total de ejecución que es la suma de los tiempos de las dos funciones, ya que cada una bloquea la ejecución de la otra hasta que termina.
# Debajo se encuentra el mismo programa pero utilizando threads, lo que significa que las dos tareas corren en paralelo y por lo tanto el programa es mas rapido y eficiente.


print(f"\n")
print(f"Los programas se ejecutan de forma secuencial:")
print(f"\n")

import time  # Importa el módulo time para trabajar con funciones relacionadas con el tiempo.

# Definimos la función prepareMate y buyFacturas
def prepareMate():
    print("Start prepareMate()")  
    time.sleep(3)  		# Simula una tarea que toma 3 segundos en completarse
    print("End prepareMate()")  
    return "Mate is ready" 

def buyFacturas():
    print("Start buyFacturas()")  
    time.sleep(5)  # Simula una tarea que toma 5 segundos en completarse
    print("End buyFacturas()") 
    return "Facturas are ready"  

# función principal main
def main():
    start_time = time.time()  # Marca el tiempo de inicio antes de ejecutar las tareas
    
	# Llamamos a la función prepareMate() y buyFacturas y guardamos su resultado

    result_mate = prepareMate()  
    result_facturas = buyFacturas()  

    end_time = time.time()  		# Guarda el tiempo de fin después de que ambas tareas hayan terminado
    tiempoTranscurrido = end_time - start_time  # Calcula el tiempo total transcurrido restando el tiempo de inicio al tiempo de fin

    # Imprime los resultados de las tareas y el tiempo total transcurrido.
    print(f"Result for prepareMate: {result_mate}")
    print(f"Result for buyFacturas: {result_facturas}")
    print(f"Total elapsed time: {tiempoTranscurrido:.2f} seconds")

# Si el archivo se está ejecutando directamente (no importado como un módulo), ejecuta la función main()
if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------
print(f"\n")
print(f"Los programas se ejecutan como threads:")
print(f"\n")

import threading  # Importa el módulo threading para trabajar con hilos.
#import time  # Importa el módulo time para trabajar con el tiempo.

# función para preparar el mate
def prepareMate():
    print("Start prepareMate()")  
    time.sleep(3)  
    print("End prepareMate()")  
    return "Mate is ready"  

# Define una función para comprar facturas
def buyFacturas():
    print("Start buyFacturas()")  
    time.sleep(5)  
    print("End buyFacturas()")  
    return "Facturas are ready"  

# función principal
def main():
    start_time = time.time()  # Marca el tiempo de inicio antes de ejecutar las tareas.

    # Crea dos hilos para ejecutar prepareMate y buyFacturas
    thread1 = threading.Thread(target=prepareMate)  # Crea un hilo para la función prepareMate()
    thread2 = threading.Thread(target=buyFacturas)  # Crea un hilo para la función buyFacturas()

    # Inicio ambos hilos
    thread1.start()
    thread2.start()

    # Espera a que ambos hilos terminen
    thread1.join()
    thread2.join()

    end_time = time.time()  # tiempo después de que ambas tareas terminaron.
    elapsed_time = end_time - start_time  # guarda el tiempo total transcurrido.

    # Imprime los resultados de las tareas y el tiempo total transcurrido.
    print(f"Result for prepareMate: Mate is ready")
    print(f"Result for buyFacturas: Facturas are ready")
    print(f"Total elapsed time: {elapsed_time:.2f} seconds")

# Ejecuta la función principal si este script se está ejecutando directamente
if __name__ == "__main__":
    main()
    
print(f"\n")
print(f"se ve una diferencia de velocidad de 3 segundos entre el sistema que corrio los programas en secuencia VS el que los corrio usando threads")
print(f"\n")