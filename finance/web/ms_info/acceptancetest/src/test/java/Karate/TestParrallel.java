package Karate;

import com.intuit.karate.Results;
import com.intuit.karate.Runner;

class TestParrallel {

    public static void main(String[] args) {
        // Ejecutar todos los escenarios en todos los archivos .feature dentro de la carpeta Karate
        Results results = Runner.path("classpath:Karate") // O especifica la ruta de tus archivos .feature
                .parallel(2); // Ejecuta en paralelo con 2 hilos (puedes cambiar el número de hilos)
        // Imprimir el directorio de resultados
        System.out.println("Resultados: " + results.getReportDir());
        // Retorna un código de salida para indicar si hay fallos en las pruebas
        System.exit(results.getFailCount());
    }
}
