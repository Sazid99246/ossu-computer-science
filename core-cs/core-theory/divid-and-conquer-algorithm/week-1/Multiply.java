import java.math.BigInteger;

public class Multiply {
    public static void main(String[] args) {
        BigInteger n1 = new BigInteger("3141592653589793238462643383279502884197169399375105820974944592");
        System.out.println(n1.multiply(new BigInteger("2718281828459045235360287471352662497757247093699959574966967627")).toString());
    }
}
