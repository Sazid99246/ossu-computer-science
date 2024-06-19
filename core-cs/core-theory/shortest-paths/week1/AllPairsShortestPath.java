import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class AllPairsShortestPath {
    
    static final int INF = Integer.MAX_VALUE;
    
    public static void main(String[] args) {
        String[] files = {"g1.txt", "g2.txt", "g3.txt"};
        int minShortestPath = INF;
        boolean negativeCycle = true;
        
        for (String file : files) {
            try {
                int[][] graph = readGraph(file);
                int n = graph.length;
                int[][] dist = floydWarshall(graph, n);
                
                if (!hasNegativeCycle(dist, n)) {
                    negativeCycle = false;
                    int shortestPath = findShortestShortestPath(dist, n);
                    if (shortestPath < minShortestPath) {
                        minShortestPath = shortestPath;
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        if (negativeCycle) {
            System.out.println("NULL");
        } else {
            System.out.println(minShortestPath);
        }
    }
    
    static int[][] readGraph(String file) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(file));
        String[] firstLine = br.readLine().split("\\s+");
        int vertices = Integer.parseInt(firstLine[0]);
        @SuppressWarnings("unused")
        int edges = Integer.parseInt(firstLine[1]);
        
        int[][] graph = new int[vertices][vertices];
        for (int[] row : graph) {
            Arrays.fill(row, INF);
        }
        
        String line;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split("\\s+");
            int u = Integer.parseInt(parts[0]) - 1;
            int v = Integer.parseInt(parts[1]) - 1;
            int length = Integer.parseInt(parts[2]);
            graph[u][v] = length;
        }
        
        br.close();
        return graph;
    }
    
    static int[][] floydWarshall(int[][] graph, int n) {
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = graph[i][j];
            }
            dist[i][i] = 0;
        }
        
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        return dist;
    }
    
    static boolean hasNegativeCycle(int[][] dist, int n) {
        for (int i = 0; i < n; i++) {
            if (dist[i][i] < 0) {
                return true;
            }
        }
        return false;
    }
    
    static int findShortestShortestPath(int[][] dist, int n) {
        int shortestPath = INF;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && dist[i][j] < shortestPath) {
                    shortestPath = dist[i][j];
                }
            }
        }
        return shortestPath;
    }
}
