package kattis.faktor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class faktor {

    private static final boolean debug = false;

    public static void main(String[] args) {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        try {
            // Take the line input
            String inputJournalInfo = bufferedReader.readLine();
            if (inputJournalInfo == null || inputJournalInfo.trim().isEmpty()) {
                dPrint("Input error");
                return;
            }

            // Start the timer
            long startRuntime = System.nanoTime();

            // Find journal info
            String[] journalInfo = inputJournalInfo.trim().split(" ");
            if (journalInfo.length != 2) {
                dPrint("Wrong journal info");
                return;
            }

            int numberOfArticle = Integer.parseInt(journalInfo[0].trim());
            int impactFactor = Integer.parseInt(journalInfo[1].trim());
            dPrint("Number of Article: " + numberOfArticle + " and impact factor " + impactFactor);

            if (!isValidJournalInfo(numberOfArticle) || !isValidJournalInfo(impactFactor)) {
                dPrint("Invalid journal info");
                return;
            }

            // Mathematical calculation matching your formula
            int bribedScientist = numberOfArticle * (impactFactor - 1) + 1;
            System.out.println(bribedScientist);

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

    private static boolean isValidJournalInfo(int metadata) {
        int min = 1;
        int max = 100;
        return metadata >= min && metadata <= max;
    }
}