import java.math.BigDecimal;

public class DesbordamientoSilencioso
{
	public static void main(String[] args) {
        int max = Integer.MAX_VALUE; // 2,147,483,647
        int resultado = max + 1;

        System.out.println("Máximo int: " + max);
        System.out.println("Máximo + 1: " + resultado); // Imprime -2147483648

        // Solución: Usar Math.addExact para lanzar una excepción si ocurre
        try {
            Math.addExact(max, 1);
        } catch (ArithmeticException e) {
            System.out.println("Error detectado: ¡Desbordamiento!");
        }
    }


}