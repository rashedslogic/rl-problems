package kattis.inputoutput.cd;

import java.io.IOException;
import java.util.Arrays;

public class cd {

    private static final boolean debug = false;

    public static void main(String[] args) {

        byte[] mBuffer;
        // A single-element array to pass a mutable reference pointer to our parser
        int[] mPointerPosition = { 0 };

        try {
            mBuffer = System.in.readAllBytes();
        } catch (IOException ioException) {
            dprint("IOException: " + ioException.getMessage());
            return;
        }

        if (mBuffer.length == 0) {
            dprint("Empty Input.");
            return;
        }

        // Start the high-resolution timer here
        long startTime = System.nanoTime();

        while (true) {
            int mN = nextIntToken(mBuffer, mPointerPosition);
            int mM = nextIntToken(mBuffer, mPointerPosition);

            // Break if termination line(0 0)
            if (mN == 0 && mM == 0) {
                dprint("Termination line.");
                break;
            }

            // Break if End of File(EOF)
            if (mN == -1 || mM == -1) {
                dprint("End of file.");
                break;
            }

            // Store Jack's CD into a raw primitive array
            int[] jackCDs = new int[mN];
            for (int i = 0; i < mN; i++) {
                jackCDs[i] = nextIntToken(mBuffer, mPointerPosition);
            }
            dprint("Jacks CD: " + Arrays.toString(jackCDs));

            // Perform Two-pointer intersection sweep comparing Jill's CDs
            int intersectionCount = 0;
            int jackCDsIndex = 0;

            for (int i = 0; i < mM; i++) {
                int jillCD = nextIntToken(mBuffer, mPointerPosition);

                while (jackCDsIndex < mN && jackCDs[jackCDsIndex] < jillCD) {
                    jackCDsIndex++;
                }

                // Store the intersection information
                if (jackCDsIndex < mN && jackCDs[jackCDsIndex] == jillCD) {
                    intersectionCount++;
                    jackCDsIndex++;
                }
            }

            // Print the final output of common items
            dprint("Intersection count: ");
            System.out.println(intersectionCount);
        }

        // Stop the timer here
        long endTime = System.nanoTime();

        // Calculate the difference and convert to second
        // Since 1 second = 1,000,000,000 nanoseconds, divide by 1e9
        double totalRuntime = (endTime - startTime) / 1_000_000_000.0;
        dprint("[Algorithmic Runtime] %.6f seconds" + totalRuntime);
    }

    private static void dprint(Object... args) {
        if (debug) {
            StringBuilder sb = new StringBuilder();
            for (Object arg : args) {
                sb.append(arg).append(" ");
            }
            System.out.println(sb.toString().trim());
        }
    }

    private static int nextIntToken(byte[] buffer, int[] pointerPosition) {

        int pointer = pointerPosition[0];

        // Skip whitespace(23) and newline(10)
        while (pointer < buffer.length && buffer[pointer] <= 32) {
            pointer++;
        }

        // Return -1 to represent End of File(EOF)
        if (pointer >= buffer.length) {
            pointerPosition[0] = pointer;
            return -1;
        }

        // Convert characters to a mathematical integer using fast base-10 arithmetic
        int value = 0;
        while (pointer < buffer.length && buffer[pointer] > 32) {
            value = (value * 10) + (buffer[pointer] - '0');
            pointer++;
        }

        // Save back the updated pointer position
        pointerPosition[0] = pointer;

        return value;
    }
}