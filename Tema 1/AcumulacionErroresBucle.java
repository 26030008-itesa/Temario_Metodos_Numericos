import java.math.BigDecimal;

public class AcumulacionErroresBucle{
	public static void main(String[] args) {
        int iteraciones = 1000000; // Un millón de sumas
        double incremento = 0.1;
        
        // 1. Acumulación usando 'double'
        double sumaDouble = 0.0;
        for (int i = 0; i < iteraciones; i++) {
            sumaDouble += incremento;
        }

        // El resultado esperado debería ser exactamente 100,000.0
        double esperado = iteraciones * incremento;

        System.out.println("--- Acumulación en Bucle (1,000,000 de iteraciones) ---");
        System.out.println("Resultado esperado: " + esperado);
        System.out.println("Resultado double:   " + sumaDouble);
        System.out.println("Diferencia (Error): " + (sumaDouble - esperado));

        // 2. Solución usando 'BigDecimal' para precisión absoluta
        BigDecimal sumaBD = BigDecimal.ZERO;
        BigDecimal incrementoBD = new BigDecimal("0.1");

        for (int i = 0; i < iteraciones; i++) {
            sumaBD = sumaBD.add(incrementoBD);
        }

        System.out.println("\n--- Solución con BigDecimal ---");
        System.out.println("Resultado exacto:   " + sumaBD.toPlainString());
        
        // 3. Verificación de error
        if (sumaDouble != esperado) {
            System.out.println("\nNOTA: El error de 'double' es notable tras un millón de sumas.");
        }
    }



}