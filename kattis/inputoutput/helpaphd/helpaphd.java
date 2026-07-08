package kattis.inputoutput.helpaphd;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class helpaphd {

    private final boolean debug;
    private final BufferedReader bufferedReader;
    private StringTokenizer stringTokenizer;

    public helpaphd(boolean debug) {
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

    private String nextToken() throws IOException {
        while (stringTokenizer == null || !stringTokenizer.hasMoreTokens()) {
            String line = bufferedReader.readLine();
            if (line == null)
                return null;
            stringTokenizer = new StringTokenizer(line);
        }
        return stringTokenizer.nextToken();
    }

    public void generateOutput() {
        try {
            // Take input from user
            dprint("-------------------------------------");
            dprint("Input the number of test cases.");
            String inputNumberOfTestCases = nextToken();
            if (inputNumberOfTestCases == null)
                return;

            int numberOfTestCases = Integer.parseInt(inputNumberOfTestCases);
            dprint("The number of test cases is:", numberOfTestCases);
            dprint("-------------------------------------");

            // Process each test case
            for (int i = 0; i < numberOfTestCases; i++) {
                dprint("Input the test case " + (i + 1) + ".");
                String inputTestCase = nextToken().trim();
                if (inputTestCase == null || inputTestCase.isEmpty()) {
                    break;
                }

                // Print output of test case
                inputTestCase = inputTestCase.trim();
                if (inputTestCase.equals("P=NP")) {
                    System.out.println("skipped");
                } else {
                    String inputNumbers[] = inputTestCase.split("\\+");
                    int numberOne = Integer.parseInt(inputNumbers[0].trim());
                    int numberTwo = Integer.parseInt(inputNumbers[1].trim());
                    dprint("Number one: " + numberOne + " and number two: " + numberTwo);
                    System.out.println(numberOne + numberTwo);
                }
            }
            dprint("-------------------------------------");
        } catch (Exception exception) {
            if (debug)
                exception.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new helpaphd(false).generateOutput();
    }
}