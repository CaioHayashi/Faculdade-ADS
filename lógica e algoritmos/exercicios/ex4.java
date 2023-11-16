import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        float productValue;

        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Informe o valor do produto: ");

            productValue = sc.nextFloat();
        }

        System.out.println("O valor final com o desconto é: R$100" + calcDiscount(productValue));
    }

    public static Double calcDiscount(Float value) {
        double descont = value * 0.09;

        return value - descont;
    }
}