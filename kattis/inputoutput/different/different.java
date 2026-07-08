package kattis.inputoutput.different;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class different {

    private final boolean debug;

    public different(boolean debug) {
        this.debug = debug;
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

    private boolean isValidNumber(long inputNumber) {
        long min = 0L;
        long max = 1000000000000000L; // 10^15
        return (inputNumber >= min && inputNumber <= max);
    }

    public void generateOutput() {
        try {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
            String inputLine;

            // Take input from user
            dprint("-------------------------------------");
            dprint("Input the file.");

            // Loop until End of File (EOF)
            while ((inputLine = bufferedReader.readLine()) != null) {
                // Trim and tokenize the line string
                StringTokenizer stringTokenizer = new StringTokenizer(inputLine.trim());

                // Confirm the number of token
                if (stringTokenizer.countTokens() != 2) {
                    dprint("Input count is not 2.");
                    break;
                }

                // Find two numbers
                long firstNumber = Long.parseLong(stringTokenizer.nextToken().trim());
                long secondNumber = Long.parseLong(stringTokenizer.nextToken().trim());
                dprint("First Number: " + firstNumber + " and Second Number: " + secondNumber);

                // Check the validity of the numbers
                if (!isValidNumber(firstNumber) || !isValidNumber(secondNumber)) {
                    dprint("Numbers are not valid.");
                    break;
                }

                // Calculate the absolute value
                dprint("This is absolute value:");
                System.out.println(Math.abs(firstNumber - secondNumber));
            }

            dprint("Reached end of file.");
            dprint("-------------------------------------");
        } catch (Exception exception) {
            dprint(exception.getMessage());
        }
    }

    public static void main(String[] args) {
        new different(false).generateOutput();
    }
}