package kattis.foundation.planina;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class planina {

    private static final boolean debug = false;

    public static void main(String[] args) {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        try {
            // Take the line input
            String inputIterationNumber = bufferedReader.readLine();
            if (inputIterationNumber == null || inputIterationNumber.trim().isEmpty()) {
                dPrint("Input error");
                return;
            }

            // Start the timer
            long startRuntime = System.nanoTime();

            // Find valid input
            if (!isDigit(inputIterationNumber)) {
                dPrint("Input is not valid");
                return;
            }

            // Find iteration number
            int iterationNumber = Integer.parseInt(inputIterationNumber);
            if (!isValidIterationNumber(iterationNumber)) {
                dPrint("Wrong iteration number");
                return;
            }

            // Find the number of points on a single side
            dPrint("Total Iteration Number: " + iterationNumber);

            // Rules: (2^N + 1)^2
            // Math.pow returns double, so we cast to int for points on a side
            int pointsOnSide = ((int) Math.pow(2, iterationNumber)) + 1;
            dPrint("Points on a single side: " + pointsOnSide);

            // Find the total number of points
            int numberOfPoints = pointsOnSide * pointsOnSide;
            dPrint("Number of Points:");
            System.out.println(numberOfPoints);

            // Stop the timer here
            long endRuntime = System.nanoTime();
            double totalRuntime = (endRuntime - startRuntime) / 1_000_000_000.0;

            dPrint(String.format("[Algorithmic Runtime] %.6f seconds", totalRuntime));

        } catch (IOException e) {
            dPrint("IOException occurred: " + e.getMessage());
        }
    }

    private static void dPrint(Object... args) {
        if (debug) {
            StringBuilder sb = new StringBuilder();
            for (Object arg : args) {
                sb.append(arg).append(" ");
            }
            System.out.println(sb.toString().trim());
        }
    }

    private static boolean isDigit(String str) {
        for (char c : str.toCharArray()) {
            if (!Character.isDigit(c)) {
                return false;
            }
        }
        return true;
    }

    private static boolean isValidIterationNumber(int value) {
        int min = 1;
        int max = 15;
        return value >= min && value <= max;
    }
}