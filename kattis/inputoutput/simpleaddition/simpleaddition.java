package kattis.inputoutput.simpleaddition;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class simpleaddition {

    private final boolean debug;
    private final BufferedReader bufferedReader;
    private StringTokenizer stringTokenizer;

    public simpleaddition(boolean debug) {
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
            dprint("Input first number.");
            String inputFirstNumber = nextToken();
            dprint("Input second number.");
            String inputSecondNumber = nextToken();
            if (inputFirstNumber == null || inputSecondNumber == null || inputFirstNumber.trim().isEmpty()
                    || inputSecondNumber.trim().isEmpty())
                return;

            BigInteger firstNumber = new BigInteger(inputFirstNumber);
            BigInteger secondNumber = new BigInteger(inputSecondNumber);
            dprint("First number is: " + firstNumber + " and Second number is: " + secondNumber);

            // Add two numbers
            dprint("-------------------------------------");
            System.out.println(firstNumber.add(secondNumber));
            dprint("-------------------------------------");
        } catch (Exception exception) {
            if (debug)
                exception.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new simpleaddition(false).generateOutput();
    }
}