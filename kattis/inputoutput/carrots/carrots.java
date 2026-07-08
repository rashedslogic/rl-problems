package kattis.inputoutput.carrots;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class carrots {

    private final boolean debug;
    private final BufferedReader bufferedReader;
    private StringTokenizer stringTokenizer;

    public carrots(boolean debug) {
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
            dprint("Input the contestants and solved problem count");
            String inputContestents = nextToken();
            String inputSolvedProblems = nextToken();
            if (inputContestents == null || inputSolvedProblems == null || inputContestents.trim().isEmpty()
                    || inputSolvedProblems.trim().isEmpty())
                return;

            int contestants = Integer.parseInt(inputContestents);
            int solvedProblems = Integer.parseInt(inputSolvedProblems);
            dprint("Contestants:", contestants, " Solved Problems: ", solvedProblems);

            dprint("-------------------------------------");
            dprint("The number of carrot is:");
            System.out.println(solvedProblems);
            dprint("-------------------------------------");
        } catch (Exception exception) {
            if (debug)
                exception.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new carrots(false).generateOutput();
    }
}