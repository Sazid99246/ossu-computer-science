import java.io.*;
import java.util.*;

public class CountInversions {

    // Function to count the number of inversions in an array
    private static long countInversions(int[] arr) {
        int[] temp = new int[arr.length];
        return mergeSortAndCount(arr, temp, 0, arr.length - 1);
    }

    // Helper function to use divide and conquer approach to count inversions
    private static long mergeSortAndCount(int[] arr, int[] temp, int left, int right) {
        long invCount = 0;
        if (left < right) {
            int mid = (left + right) / 2;

            invCount += mergeSortAndCount(arr, temp, left, mid);
            invCount += mergeSortAndCount(arr, temp, mid + 1, right);
            invCount += mergeAndCount(arr, temp, left, mid, right);
        }
        return invCount;
    }

    // Function to merge two halves and count inversions
    private static long mergeAndCount(int[] arr, int[] temp, int left, int mid, int right) {
        int i = left;    // Starting index for left subarray
        int j = mid + 1; // Starting index for right subarray
        int k = left;    // Starting index to be sorted
        long invCount = 0;

        // Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
                invCount += (mid - i + 1);
            }
        }

        // Copy the remaining elements of left subarray, if any
        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        // Copy the remaining elements of right subarray, if any
        while (j <= right) {
            temp[k++] = arr[j++];
        }

        // Copy the sorted subarray into original array
        for (i = left; i <= right; i++) {
            arr[i] = temp[i];
        }

        return invCount;
    }

    public static void main(String[] args) {
        try {
            // Read the integers from the file
            BufferedReader reader = new BufferedReader(new FileReader("IntegerArray.txt"));
            List<Integer> list = new ArrayList<>();
            String line;

            while ((line = reader.readLine()) != null) {
                list.add(Integer.parseInt(line.trim()));
            }

            reader.close();

            // Convert list to array
            int[] arr = list.stream().mapToInt(i -> i).toArray();

            // Get the number of inversions
            long result = countInversions(arr);
            System.out.println(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
