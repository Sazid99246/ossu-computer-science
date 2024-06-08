import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

class Edge {
    int node1;
    int node2;
    int cost;

    public Edge(int node1, int node2, int cost) {
        this.node1 = node1;
        this.node2 = node2;
        this.cost = cost;
    }
}

public class PrimsMST {
    
    public static List<Edge> readGraph(String filePath) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line = reader.readLine();
        String[] firstLine = line.split(" ");
        @SuppressWarnings("unused")
        int numNodes = Integer.parseInt(firstLine[0]);
        @SuppressWarnings("unused")
        int numEdges = Integer.parseInt(firstLine[1]);
        List<Edge> edges = new ArrayList<>();

        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" ");
            int node1 = Integer.parseInt(parts[0]);
            int node2 = Integer.parseInt(parts[1]);
            int cost = Integer.parseInt(parts[2]);
            edges.add(new Edge(node1, node2, cost));
        }

        reader.close();
        return edges;
    }

    public static int primsMST(int numNodes, List<Edge> edges) {
        // Initialize the adjacency list
        Map<Integer, List<Edge>> adjList = new HashMap<>();
        for (int i = 1; i <= numNodes; i++) {
            adjList.put(i, new ArrayList<>());
        }
        for (Edge edge : edges) {
            adjList.get(edge.node1).add(edge);
            adjList.get(edge.node2).add(edge);
        }

        // Prim's algorithm
        boolean[] inMST = new boolean[numNodes + 1];
        PriorityQueue<Edge> minHeap = new PriorityQueue<>(Comparator.comparingInt(e -> e.cost));
        int mstCost = 0;
        int nodesInMST = 0;

        // Start with node 1
        inMST[1] = true;
        nodesInMST++;
        for (Edge edge : adjList.get(1)) {
            minHeap.offer(edge);
        }

        while (nodesInMST < numNodes) {
            Edge minEdge = minHeap.poll();
            if (inMST[minEdge.node1] && inMST[minEdge.node2]) {
                continue;
            }

            mstCost += minEdge.cost;
            int newNode = inMST[minEdge.node1] ? minEdge.node2 : minEdge.node1;
            inMST[newNode] = true;
            nodesInMST++;

            for (Edge edge : adjList.get(newNode)) {
                if (!inMST[edge.node1] || !inMST[edge.node2]) {
                    minHeap.offer(edge);
                }
            }
        }

        return mstCost;
    }

    public static void main(String[] args) {
        String filePath = "edges.txt"; // Change this to the correct path of your file

        try {
            List<Edge> edges = readGraph(filePath);
            @SuppressWarnings("resource")
            String firstLine = new BufferedReader(new FileReader(filePath)).readLine();
            int numNodes = Integer.parseInt(firstLine.split(" ")[0]);
            int result = primsMST(numNodes, edges);
            System.out.println(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
