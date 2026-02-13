import java.math.BigDecimal;

public class ConversiónEstrecha
{
	public static void main(String[] args) {
        double valorDouble = 3.14159e10; // Un número muy grande
        int valorInt = (int) valorDouble; // Casting explícito

        System.out.println("Valor Original: " + valorDouble);
        System.out.println("Valor Truncado: " + valorInt); 
        // Imprime 2147483647 (el máximo int) porque el double no cabe.
    }



}