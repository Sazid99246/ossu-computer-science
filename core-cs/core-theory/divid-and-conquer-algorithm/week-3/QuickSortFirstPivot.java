import java.io.IOException;

public class QuickSortFirstPivot {

    private int comparisons = 0;

    public int sort(int[] array) {
        comparisons = 0;
        quickSort(array, 0, array.length - 1);
        return comparisons;
    }

    private void quickSort(int[] array, int left, int right) {
        if (left < right) {
            comparisons += right - left;
            int pivotIndex = partition(array, left, right);
            quickSort(array, left, pivotIndex - 1);
            quickSort(array, pivotIndex + 1, right);
        }
    }

    private int partition(int[] array, int left, int right) {
        int pivot = array[left];
        int i = left + 1;
        for (int j = left + 1; j <= right; j++) {
            if (array[j] < pivot) {
                swap(array, i, j);
                i++;
            }
        }
        swap(array, left, i - 1);
        return i - 1;
    }

    private void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void main(String[] args) throws IOException {
        int[] array = FileUtil.readFile("QuickSort.txt");
        QuickSortFirstPivot sorter = new QuickSortFirstPivot();
        int comparisons = sorter.sort(array);
        System.out.println(comparisons);
    }
}
