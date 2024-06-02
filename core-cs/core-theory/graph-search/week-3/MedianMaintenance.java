import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.PriorityQueue;
import java.util.Collections;

public class MedianMaintenance {

    public static void main(String[] args) {
        String filename = "Median.txt";
        System.out.println("Sum of medians modulo 10000: " + calculateMedianSum(filename));
    }

    public static int calculateMedianSum(String filename) {
        PriorityQueue<Integer> lowerHalf = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> upperHalf = new PriorityQueue<>();
        
        int medianSum = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                int number = Integer.parseInt(line);
                
                if (lowerHalf.isEmpty() || number <= lowerHalf.peek()) {
                    lowerHalf.offer(number);
                } else {
                    upperHalf.offer(number);
                }

                if (lowerHalf.size() > upperHalf.size() + 1) {
                    upperHalf.offer(lowerHalf.poll());
                } else if (upperHalf.size() > lowerHalf.size()) {
                    lowerHalf.offer(upperHalf.poll());
                }

                int median;
                if (lowerHalf.size() >= upperHalf.size()) {
                    median = lowerHalf.peek();
                } else {
                    median = upperHalf.peek();
                }

                medianSum += median;
                medianSum %= 10000;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return medianSum;
    }
}
