import java.io.*;

public class MWISPathGraph {
    public static void main(String[] args) {
        String filename = "mwis.txt";
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            int numberOfVertices = Integer.parseInt(br.readLine().trim());
            int[] weights = new int[numberOfVertices + 1];
            for (int i = 1; i <= numberOfVertices; i++) {
                weights[i] = Integer.parseInt(br.readLine().trim());
            }
            br.close();

            // Step 2: Dynamic Programming to compute the maximum-weight independent set
            int[] A = new int[numberOfVertices + 1];
            A[0] = 0;
            A[1] = weights[1];
            for (int i = 2; i <= numberOfVertices; i++) {
                A[i] = Math.max(A[i-1], A[i-2] + weights[i]);
            }

            // Step 3: Reconstruction
            boolean[] isInMWIS = new boolean[numberOfVertices + 1];
            for (int i = numberOfVertices; i >= 1; i--) {
                if (i == 1 || A[i-1] >= A[i-2] + weights[i]) {
                    isInMWIS[i] = false;
                } else {
                    isInMWIS[i] = true;
                    i--; // Skip the adjacent vertex
                }
            }

            // Step 4: Generate the 8-bit string for specific vertices
            int[] verticesToCheck = {1, 2, 3, 4, 17, 117, 517, 997};
            StringBuilder result = new StringBuilder();
            for (int vertex : verticesToCheck) {
                if (vertex <= numberOfVertices && isInMWIS[vertex]) {
                    result.append("1");
                } else {
                    result.append("0");
                }
            }

            System.out.println("8-bit string: " + result.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
