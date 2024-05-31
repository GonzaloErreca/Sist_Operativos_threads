<?php
// Argumentos pasados desde el script principal
$name = $argv[1];        // Nombre del "hilo"
$interval = $argv[2];    // Intervalo de tiempo en segundos

// Función que simula un "hilo" de trabajo
function worker($name, $interval) {
    while (true) {
        // Obtener la hora actual
        $hora = date("H");
        $minuto = date("i");
        $segundo = date("s");

        // Formatear la hora en una cadena de texto hh:mm:ss
        $time = $hora . ":" . $minuto . ":" . $segundo;

        // Imprimir el nombre del "hilo" y la hora actual
        echo $name . " --> " . $time . PHP_EOL;

        // Esperar por el intervalo de tiempo especificado
        sleep($interval);
    }
}

// Llamar a la función worker con los argumentos proporcionados
worker($name, $interval);
?>
