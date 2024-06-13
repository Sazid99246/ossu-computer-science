import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SmallKnapsack {
    public static void main(String[] args) throws IOException {
        String filePath = "knapsack1.txt";
        int result = solveSmallKnapsack(filePath);
        System.out.println(result);
    }

    public static int solveSmallKnapsack(String filePath) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(filePath));
        String[] firstLine = br.readLine().split(" ");
        int knapsackSize = Integer.parseInt(firstLine[0]);
        int numberOfItems = Integer.parseInt(firstLine[1]);

        List<int[]> items = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split(" ");
            int value = Integer.parseInt(parts[0]);
            int weight = Integer.parseInt(parts[1]);
            items.add(new int[]{value, weight});
        }
        br.close();

        int[][] dp = new int[numberOfItems + 1][knapsackSize + 1];

        for (int i = 1; i <= numberOfItems; i++) {
            int value = items.get(i - 1)[0];
            int weight = items.get(i - 1)[1];
            for (int w = 0; w <= knapsackSize; w++) {
                if (weight > w) {
                    dp[i][w] = dp[i - 1][w];
                } else {
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weight] + value);
                }
            }
        }

        return dp[numberOfItems][knapsackSize];
    }
}
