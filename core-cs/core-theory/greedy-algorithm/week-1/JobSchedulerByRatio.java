import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Job {
    int weight;
    int length;

    public Job(int weight, int length) {
        this.weight = weight;
        this.length = length;
    }

    public double getRatio() {
        return (double) weight / length;
    }
}

public class JobSchedulerByRatio {

    public static List<Job> readJobs(String filePath) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line = reader.readLine();
        @SuppressWarnings("unused")
        int numJobs = Integer.parseInt(line.trim());
        List<Job> jobs = new ArrayList<>();

        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" ");
            int weight = Integer.parseInt(parts[0]);
            int length = Integer.parseInt(parts[1]);
            jobs.add(new Job(weight, length));
        }

        reader.close();
        return jobs;
    }

    public static void sortJobsByRatio(List<Job> jobs) {
        Collections.sort(jobs, new Comparator<Job>() {
            @Override
            public int compare(Job job1, Job job2) {
                double ratio1 = job1.getRatio();
                double ratio2 = job2.getRatio();
                return Double.compare(ratio2, ratio1); // Sort by ratio (weight/length) descending
            }
        });
    }

    public static long computeWeightedSum(List<Job> jobs) {
        long completionTime = 0;
        long weightedSum = 0;

        for (Job job : jobs) {
            completionTime += job.length;
            weightedSum += job.weight * completionTime;
        }

        return weightedSum;
    }

    public static void main(String[] args) {
        String filePath = "jobs.txt"; // Change this to the correct path of your file

        try {
            List<Job> jobs = readJobs(filePath);
            sortJobsByRatio(jobs);
            long result = computeWeightedSum(jobs);
            System.out.println(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
