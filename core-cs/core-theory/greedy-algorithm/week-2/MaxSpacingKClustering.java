import java.io.*;
import java.util.*;

public class MaxSpacingKClustering {

    static class Edge implements Comparable<Edge> {
        int node1, node2, cost;

        Edge(int node1, int node2, int cost) {
            this.node1 = node1;
            this.node2 = node2;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    static class UnionFind {
        private int[] parent;
        private int[] rank;
        private int count;

        UnionFind(int n) {
            parent = new int[n + 1];
            rank = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
            count = n;
        }

        int find(int p) {
            if (p != parent[p]) {
                parent[p] = find(parent[p]); // Path compression
            }
            return parent[p];
        }

        boolean union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);

            if (rootP == rootQ) return false;

            if (rank[rootP] < rank[rootQ]) {
                parent[rootP] = rootQ;
            } else if (rank[rootP] > rank[rootQ]) {
                parent[rootQ] = rootP;
            } else {
                parent[rootQ] = rootP;
                rank[rootP]++;
            }
            count--;
            return true;
        }

        int count() {
            return count;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("clustering1.txt"));
        int numberOfNodes = Integer.parseInt(br.readLine().trim());

        List<Edge> edges = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split("\\s+");
            int node1 = Integer.parseInt(parts[0]);
            int node2 = Integer.parseInt(parts[1]);
            int cost = Integer.parseInt(parts[2]);
            edges.add(new Edge(node1, node2, cost));
        }
        br.close();

        // Kruskal's algorithm
        Collections.sort(edges);
        UnionFind uf = new UnionFind(numberOfNodes);

        int k = 4; // target number of clusters
        int maxSpacing = 0;

        for (Edge edge : edges) {
            if (uf.count() == k) {
                if (uf.find(edge.node1) != uf.find(edge.node2)) {
                    maxSpacing = edge.cost;
                    break;
                }
            }
            uf.union(edge.node1, edge.node2);
        }

        System.out.println("Maximum spacing of 4-clustering: " + maxSpacing);
    }
}
