import java.io.IOException;

public class QuickSortMedianPivot {

    private int comparisons = 0;

    public int sort(int[] array) {
        comparisons = 0;
        quickSort(array, 0, array.length - 1);
        return comparisons;
    }

    private void quickSort(int[] array, int left, int right) {
        if (left < right) {
            comparisons += right - left;
            int pivotIndex = medianOfThree(array, left, right);
            swap(array, left, pivotIndex);
            int partitionIndex = partition(array, left, right);
            quickSort(array, left, partitionIndex - 1);
            quickSort(array, partitionIndex + 1, right);
        }
    }

    private int medianOfThree(int[] array, int left, int right) {
        int mid = left + (right - left) / 2;
        int a = array[left];
        int b = array[mid];
        int c = array[right];
        if ((a > b) != (a > c)) {
            return left;
        } else if ((b > a) != (b > c)) {
            return mid;
        } else {
            return right;
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
        QuickSortMedianPivot sorter = new QuickSortMedianPivot();
        int comparisons = sorter.sort(array);
        System.out.println(comparisons);
    }
}
