import java.io.*;
import java.util.*;

public class MinCut {
    
    public static Map<Integer, List<Integer>> readGraph(String filename) throws IOException {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        BufferedReader br = new BufferedReader(new FileReader(filename));
        String line;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split("\\s+");
            int vertex = Integer.parseInt(parts[0]);
            List<Integer> edges = new ArrayList<>();
            for (int i = 1; i < parts.length; i++) {
                edges.add(Integer.parseInt(parts[i]));
            }
            graph.put(vertex, edges);
        }
        br.close();
        return graph;
    }

    private static void contractEdge(Map<Integer, List<Integer>> graph, int vertex1, int vertex2) {
        // Merge vertex2 into vertex1 and remove vertex2
        List<Integer> edges1 = graph.get(vertex1);
        List<Integer> edges2 = graph.get(vertex2);

        // Add vertex2's edges to vertex1
        edges1.addAll(edges2);

        // Replace occurrences of vertex2 with vertex1 in the graph
        for (int vertex : edges2) {
            List<Integer> edges = graph.get(vertex);
            Collections.replaceAll(edges, vertex2, vertex1);
        }

        // Remove self-loops
        edges1.removeIf(edge -> edge == vertex1);

        // Remove vertex2 from the graph
        graph.remove(vertex2);
    }

    public static int randomizedContraction(Map<Integer, List<Integer>> graph) {
        Random rand = new Random();
        Map<Integer, List<Integer>> graphCopy = deepCopyGraph(graph);
        
        while (graphCopy.size() > 2) {
            // Choose a random edge (u, v)
            int vertex1 = getRandomVertex(graphCopy, rand);
            List<Integer> edges = graphCopy.get(vertex1);
            int vertex2 = edges.get(rand.nextInt(edges.size()));
            
            // Contract the edge (vertex1, vertex2)
            contractEdge(graphCopy, vertex1, vertex2);
        }
        
        // Return the number of edges between the two remaining vertices
        return graphCopy.values().iterator().next().size();
    }

    private static int getRandomVertex(Map<Integer, List<Integer>> graph, Random rand) {
        List<Integer> keys = new ArrayList<>(graph.keySet());
        return keys.get(rand.nextInt(keys.size()));
    }

    private static Map<Integer, List<Integer>> deepCopyGraph(Map<Integer, List<Integer>> graph) {
        Map<Integer, List<Integer>> copy = new HashMap<>();
        for (Map.Entry<Integer, List<Integer>> entry : graph.entrySet()) {
            copy.put(entry.getKey(), new ArrayList<>(entry.getValue()));
        }
        return copy;
    }

    public static void main(String[] args) throws IOException {
        Map<Integer, List<Integer>> graph = readGraph("./KargerMinCut.txt");
        int minCut = Integer.MAX_VALUE;
        
        for (int i = 0; i < 1000; i++) { // Run the algorithm multiple times
            int cut = randomizedContraction(graph);
            if (cut < minCut) {
                minCut = cut;
            }
        }
        
        System.out.println(minCut);
    }
}
