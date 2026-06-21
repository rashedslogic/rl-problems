package kattis.statistics;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class statistics {

    private final boolean debug;
    private final BufferedReader bufferedReader;
    private StringTokenizer stringTokenizer;

    public statistics(boolean debug) {
        this.debug = debug;
        this.bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    }

    private void dprint(Object... args) {
        if (debug) {
            StringBuilder sb = new StringBuilder();
            for (Object arg : args) {
                sb.append(arg).append(" ");
            }
            System.out.println(sb.toString().trim());
        }
    }

    private boolean isValidDataCounter(int inputDataCounter) {
        int min = 1;
        int max = 30;
        return (inputDataCounter >= min && inputDataCounter <= max);
    }

    private boolean isValidDataSample(int inputDataSample) {
        int min = -1000000;
        int max = 1000000;
        return (inputDataSample >= min && inputDataSample <= max);
    }

    private String nextToken() throws IOException {
        while (stringTokenizer == null || !stringTokenizer.hasMoreTokens()) {
            String line = bufferedReader.readLine();
            if (line == null)
                return null;
            stringTokenizer = new StringTokenizer(line);
        }
        return stringTokenizer.nextToken();
    }

    private int countTokens() {
        return (stringTokenizer == null) ? 0 : stringTokenizer.countTokens();
    }

    private String readLine() throws IOException {
        stringTokenizer = null; // Invalidate the current line cache
        return bufferedReader.readLine();
    }

    public void generateOutput() {
        try {
            // Take input from user
            dprint("-------------------------------------");
            int testCaseNumber = 0;

            while (!(testCaseNumber >= 10)) {
                testCaseNumber += 1;
                dprint("Input the test case " + testCaseNumber + ".");
                String inputTestCase = readLine();

                // Check the validity of test case
                if (inputTestCase == null || inputTestCase.isEmpty()) {
                    dprint("Invalid input.");
                    break;
                }

                // Check the input length
                String dataInput[] = inputTestCase.trim().split(" ");
                int dataInputLength = dataInput.length;
                dprint("Data input length is: " + dataInputLength);
                if (dataInputLength <= 1) {
                    dprint("Invalid input length.");
                    break;
                }

                // Check the validity of data counter
                int dataCounter = Integer.parseInt(dataInput[0].trim());
                dprint("Data counter is: " + dataCounter);
                if (!isValidDataCounter(dataCounter)) {
                    dprint("Invalid data counter.");
                    break;
                }

                // Check the length of data sample
                dprint("Length of data sample is: " + (dataInputLength - 1));
                if (dataCounter != (dataInputLength - 1)) {
                    dprint("Invalid lenght of data sample.");
                    break;
                }

                // Build the data sample
                int dataSample[] = new int[dataCounter];
                for (int i = 0; i < dataCounter; i++) {
                    int valDataSample = Integer.parseInt(dataInput[i + 1].trim());
                    dprint((i + 1) + "Data sample value is: " + valDataSample);

                    // Check the valid data sample
                    if (!isValidDataSample(valDataSample)) {
                        dprint((i + 1) + "data sample is invalid.");
                        break;
                    }

                    dataSample[i] = valDataSample;
                }

                // Check valid final data sample
                dprint("Final data sample is: " + Arrays.toString(dataSample));
                if (dataSample.length != dataCounter) {
                    dprint("Final data sample is invalid.");
                }

                // Find min, max and range
                int statMinimum = dataSample[0];
                int statMaximum = dataSample[0];

                // Single pass pass to find both boundaries
                for (int i = 1; i < dataSample.length; i++) {
                    if (dataSample[i] < statMinimum) {
                        statMinimum = dataSample[i];
                    }
                    if (dataSample[i] > statMaximum) {
                        statMaximum = dataSample[i];
                    }
                }

                int statRange = statMaximum - statMinimum;
                System.out.println("Case " + testCaseNumber + ": " + statMinimum + " " + statMaximum + " " + statRange);
            }
            dprint("-------------------------------------");
        } catch (Exception exception) {
            dprint(exception.getMessage());
        }
    }

    public static void main(String[] args) {
        new statistics(false).generateOutput();
    }
}