import java.io.*;
import java.util.*;

public class Dijkstra {
    private static final int TOTAL_VERTICES = 200;
    private static final int INFINITY = 1000000;
    
    public static void main(String[] args) throws IOException {
        // Read the input file
        List<List<Node>> graph = readGraph("dijkstraData.txt");
        
        // Compute shortest paths using Dijkstra's algorithm
        int[] shortestPaths = dijkstra(graph, 1);
        
        // Vertices for which we need to find the shortest paths
        int[] targets = {7, 37, 59, 82, 99, 115, 133, 165, 188, 197};
        
        // Collect and print the shortest-path distances in the required format
        StringBuilder result = new StringBuilder();
        for (int target : targets) {
            result.append(shortestPaths[target]).append(",");
        }
        // Remove the last comma
        result.setLength(result.length() - 1);
        
        System.out.println(result.toString());
    }
    
    private static List<List<Node>> readGraph(String filename) throws IOException {
        List<List<Node>> graph = new ArrayList<>(TOTAL_VERTICES + 1);
        for (int i = 0; i <= TOTAL_VERTICES; i++) {
            graph.add(new ArrayList<>());
        }
        
        BufferedReader br = new BufferedReader(new FileReader(filename));
        String line;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split("\\s+");
            int vertex = Integer.parseInt(parts[0]);
            for (int i = 1; i < parts.length; i++) {
                String[] edge = parts[i].split(",");
                int neighbor = Integer.parseInt(edge[0]);
                int weight = Integer.parseInt(edge[1]);
                graph.get(vertex).add(new Node(neighbor, weight));
            }
        }
        br.close();
        return graph;
    }
    
    private static int[] dijkstra(List<List<Node>> graph, int source) {
        int[] dist = new int[TOTAL_VERTICES + 1];
        boolean[] visited = new boolean[TOTAL_VERTICES + 1];
        
        Arrays.fill(dist, INFINITY);
        dist[source] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(source, 0));
        
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int currentVertex = current.vertex;
            
            if (visited[currentVertex]) continue;
            visited[currentVertex] = true;
            
            for (Node neighbor : graph.get(currentVertex)) {
                if (!visited[neighbor.vertex]) {
                    int newDist = dist[currentVertex] + neighbor.weight;
                    if (newDist < dist[neighbor.vertex]) {
                        dist[neighbor.vertex] = newDist;
                        pq.add(new Node(neighbor.vertex, newDist));
                    }
                }
            }
        }
        
        return dist;
    }
    
    private static class Node implements Comparable<Node> {
        int vertex;
        int weight;
        
        Node(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }
        
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.weight, other.weight);
        }
    }
}
