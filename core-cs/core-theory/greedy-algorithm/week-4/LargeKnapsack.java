import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class LargeKnapsack {
    public static void main(String[] args) throws IOException {
        String filePath = "knapsack_big.txt";
        int result = solveLargeKnapsack(filePath);
        System.out.println(result);
    }

    public static int solveLargeKnapsack(String filePath) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(filePath));
        String[] firstLine = br.readLine().split(" ");
        int knapsackSize = Integer.parseInt(firstLine[0]);
        int numberOfItems = Integer.parseInt(firstLine[1]);

        int[][] items = new int[numberOfItems][2];
        String line;
        int index = 0;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split(" ");
            int value = Integer.parseInt(parts[0]);
            int weight = Integer.parseInt(parts[1]);
            items[index][0] = value;
            items[index][1] = weight;
            index++;
        }
        br.close();

        Map<String, Integer> memo = new HashMap<>();
        return knapsack(numberOfItems, knapsackSize, items, memo);
    }

    public static int knapsack(int i, int w, int[][] items, Map<String, Integer> memo) {
        if (i == 0 || w == 0) return 0;
        String key = i + "," + w;
        if (memo.containsKey(key)) return memo.get(key);

        int value = items[i - 1][0];
        int weight = items[i - 1][1];

        int result;
        if (weight > w) {
            result = knapsack(i - 1, w, items, memo);
        } else {
            result = Math.max(knapsack(i - 1, w, items, memo),
                              knapsack(i - 1, w - weight, items, memo) + value);
        }

        memo.put(key, result);
        return result;
    }
}
