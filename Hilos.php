<?php
echo "Inicio del programa" ;

// Ejecutar el primer "hilo" en segundo plano
exec('start /B php worker.php "Work 1" 1');

// Ejecutar el segundo "hilo" en segundo plano
exec('start /B php worker.php "Work 2" 3');

echo "Fin del programa" ;
?>
