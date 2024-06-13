import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int weight;
    Node left;
    Node right;

    Node(int weight) {
        this.weight = weight;
    }

    Node(int weight, Node left, Node right) {
        this.weight = weight;
        this.left = left;
        this.right = right;
    }

    @Override
    public int compareTo(Node other) {
        return this.weight - other.weight;
    }
}

class HuffmanTree {
    private Node root;

    public HuffmanTree(int[] weights) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        for (int weight : weights) {
            pq.add(new Node(weight));
        }

        while (pq.size() > 1) {
            Node left = pq.poll();
            Node right = pq.poll();
            Node parent = new Node(left.weight + right.weight, left, right);
            pq.add(parent);
        }

        root = pq.poll();
    }

    public int getMaxCodeLength() {
        return getMaxCodeLength(root, 0);
    }

    private int getMaxCodeLength(Node node, int depth) {
        if (node == null) return 0;
        if (node.left == null && node.right == null) return depth;
        return Math.max(getMaxCodeLength(node.left, depth + 1), getMaxCodeLength(node.right, depth + 1));
    }

    public int getMinCodeLength() {
        return getMinCodeLength(root, 0);
    }

    private int getMinCodeLength(Node node, int depth) {
        if (node == null) return Integer.MAX_VALUE;
        if (node.left == null && node.right == null) return depth;
        return Math.min(getMinCodeLength(node.left, depth + 1), getMinCodeLength(node.right, depth + 1));
    }
}

public class Main {
    public static void main(String[] args) {
        String filename = "huffman.txt";
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            int numberOfSymbols = Integer.parseInt(br.readLine().trim());
            int[] weights = new int[numberOfSymbols];
            for (int i = 0; i < numberOfSymbols; i++) {
                weights[i] = Integer.parseInt(br.readLine().trim());
            }
            br.close();

            HuffmanTree huffmanTree = new HuffmanTree(weights);
            System.out.println("Maximum codeword length: " + huffmanTree.getMaxCodeLength());
            System.out.println("Minimum codeword length: " + huffmanTree.getMinCodeLength());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}