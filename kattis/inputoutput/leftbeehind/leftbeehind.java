package kattis.inputoutput.leftbeehind;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class leftbeehind {

    private final boolean debug;
    private final BufferedReader bufferedReader;
    private StringTokenizer stringTokenizer;

    public leftbeehind(boolean debug) {
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
            int testCaseNumber = 0;
            while (!(testCaseNumber >= 15)) {
                testCaseNumber += 1;
                dprint("Input the test case " + testCaseNumber + ".");

                String inputSweetJars = nextToken();
                String inputSourJars = nextToken();

                if (inputSweetJars == null || inputSourJars == null || inputSweetJars.trim().isEmpty()
                        || inputSourJars.trim().isEmpty()) {
                    dprint("Invalid input.");
                    break;
                }

                int sweetJars = Integer.parseInt(inputSweetJars.trim());
                int sourJars = Integer.parseInt(inputSourJars.trim());
                dprint("Sweet Jars: " + sweetJars + " and Sour Jars: " + sourJars);

                if (sweetJars == 0 && sourJars == 0) {
                    break;
                } else if (sweetJars + sourJars == 13) {
                    System.out.println("Never speak again.");
                } else if (sweetJars < sourJars) {
                    System.out.println("Left beehind.");
                } else if (sweetJars == sourJars) {
                    System.out.println("Undecided.");
                } else if (sweetJars > sourJars) {
                    System.out.println("To the convention.");
                }

            }
            dprint("-------------------------------------");
        } catch (Exception exception) {
            if (debug)
                exception.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new leftbeehind(false).generateOutput();
    }
}