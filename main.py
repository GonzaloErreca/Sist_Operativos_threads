#Este es un ejemplo de un programa que no utiliza hilos (threads), las funciones prepareMate() y buyFacturas() se ejecutan de manera secuencial, una después de la otra.
#Esto significa que el programa espera a que prepareMate() termine completamente antes de comenzar buyFacturas().
#Este enfoque secuencial resulta en un tiempo total de ejecución que es la suma de los tiempos de las dos funciones, ya que cada una bloquea la ejecución de la otra hasta que termina.
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
print(f"Los programas se ejecutan de forma asíncrona:")
print(f"\n")
import asyncio      # Importa el módulo asyncio, que permite la programación asíncrona
import time     

# Definimos una función asíncrona (co-rutina) llamada prepareMate()
async def prepareMate():
    print("Start prepareMate()") 
    await asyncio.sleep(3)   # Usamos asyncio.sleep para simular una espera de 3 segundos de forma asíncrona
    print("End prepareMate()")  
    return "Mate is ready"  

# lo mismo con la función asíncrona buyFacturas()
async def buyFacturas():
    print("Start buyFacturas()")  
    await asyncio.sleep(5)  # simulamos una espera de 5 segundos
    print("End buyFacturas()")  
    return "Facturas are ready" 

#Función  principal asíncrona
async def main():
    start_time = time.time()  # Guarda el tiempo de inicio antes de ejecutar las tareas

    # Se usa asyncio.gather para ejecutar prepareMate() y buyFacturas() concurrentemente en batch

    batch = asyncio.gather(prepareMate(), buyFacturas())
    result_mate, result_facturas = await batch           # Espera a que ambas tareas se completen y obtiene sus resultados.

    end_time = time.time()  # Marca el tiempo de fin después de que ambas tareas hayan terminado.
    tiempoTranscurrido = end_time - start_time  # Calcula el tiempo total transcurrido restando el tiempo de inicio al tiempo de fin.

    # Imprime los resultados de las tareas y el tiempo total transcurrido.
    print(f"Result for prepareMate: {result_mate}")
    print(f"Result for buyFacturas: {result_facturas}")
    print(f"Total elapsed time: {tiempoTranscurrido:.2f} seconds")

# Si el archivo se está ejecutando directamente (no importado como un módulo), ejecuta la función main() usando asyncio.run()
if __name__ == "__main__":
    asyncio.run(main())  # Ejecuta la función main de forma asíncrona.
