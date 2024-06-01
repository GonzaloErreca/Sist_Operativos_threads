#Este es un ejemplo de un programa que no utiliza hilos (threads), las funciones prepareMate() y buyFacturas() se ejecutan de manera secuencial, una después de la otra.
#Esto significa que el programa espera a que prepareMate() termine completamente antes de comenzar buyFacturas().
#Este enfoque secuencial resulta en un tiempo total de ejecución que es la suma de los tiempos de las dos funciones, ya que cada una bloquea la ejecución de la otra hasta que termina.

import time  # Importa el módulo time para trabajar con funciones relacionadas con el tiempo.

# Definimos la función prepareMate y buyFacturas
def prepareMate():
    print("Start prepareMate()")  
    time.sleep(3)  		# Simula una tarea que toma 3 segundos en completarse.
    print("End prepareMate()")  
    return "Mate is ready" 

def buyFacturas():
    print("Start buyFacturas()")  
    time.sleep(5)  # Simula una tarea que toma 5 segundos en completarse.
    print("End buyFacturas()") 
    return "Facturas are ready"  

# función principal main
def main():
    start_time = time.time()  # Marca el tiempo de inicio antes de ejecutar las tareas.
    
	# Llamamos a la función prepareMate() y buyFacturas y guardamos su resultado.

    result_mate = prepareMate()  
    result_facturas = buyFacturas()  

    end_time = time.time()  		# Marca el tiempo de fin después de que ambas tareas hayan terminado.
    tiempoTranscurrido = end_time - start_time  # Calcula el tiempo total transcurrido restando el tiempo de inicio al tiempo de fin.

    # Imprime los resultados de las tareas y el tiempo total transcurrido.
    print(f"Result for prepareMate: {result_mate}")
    print(f"Result for buyFacturas: {result_facturas}")
    print(f"Total elapsed time: {tiempoTranscurrido:.2f} seconds")

# Si el archivo se está ejecutando directamente (no importado como un módulo), ejecuta la función main()
if __name__ == "__main__":
    main()

