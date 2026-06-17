package kattis.busassignment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class busassignment {

    private final boolean debug;
    private final BufferedReader bufferedReader;
    private StringTokenizer stringTokenizer;

    public busassignment(boolean debug) {
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

    public void findMaximumCapacity() {
        try {
            // Find the number of stoppage
            dprint("Input number of stoppage.");
            String inputNumberOfStoppage = nextToken();
            if (inputNumberOfStoppage == null)
                return;

            int numberOfStoppage = Integer.parseInt(inputNumberOfStoppage);
            dprint("Number of stoppage:", numberOfStoppage);
            dprint("-------------------------------------");

            // Process all passengers at each stoppage
            int currentPassenger = 0;
            int maximumCapacity = 0;

            for (int i = 0; i < numberOfStoppage; i++) {
                dprint("Input the off/on passengers for stoppage " + (i + 1));
                String offStr = nextToken();
                String onStr = nextToken();
                if (offStr == null || onStr == null)
                    break;

                int getOffPassengers = Integer.parseInt(offStr);
                int getOnPassengers = Integer.parseInt(onStr);
                dprint("Get off passengers:", getOffPassengers, "and get on passengers:", getOnPassengers);

                // Calculate net passengers at this stoppage
                currentPassenger += (getOnPassengers - getOffPassengers);
                dprint("Current passengers:", currentPassenger);

                // Calculate maximum capacity of the bus
                maximumCapacity = Math.max(maximumCapacity, currentPassenger);
                dprint("Maximum capacity at stoppage " + (i + 1) + ":", maximumCapacity);
                dprint("-------------------------------------");
            }

            // The actual output that prints regardless of the debug mode status
            System.out.println(maximumCapacity);
            dprint("-------------------------------------");
        } catch (Exception exception) {
            if (debug)
                exception.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new busassignment(false).findMaximumCapacity();
    }
}