package kattis.dagatal;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class dagatal {

    private final boolean debug;
    private final BufferedReader bufferedReader;
    private StringTokenizer stringTokenizer;

    public dagatal(boolean debug) {
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

    private Integer getDaysInMonth(int month) {
        HashMap<Integer, Integer> daysMap = new HashMap<>();

        daysMap.put(1, 31); // January
        daysMap.put(2, 28); // February (as 2019 is not leap year)
        daysMap.put(3, 31); // March
        daysMap.put(4, 30); // April
        daysMap.put(5, 31); // May
        daysMap.put(6, 30); // June
        daysMap.put(7, 31); // July
        daysMap.put(8, 31); // August
        daysMap.put(9, 30); // September
        daysMap.put(10, 31); // October
        daysMap.put(11, 30); // November
        daysMap.put(12, 31); // December

        return daysMap.get(month);
    }

    private void generateOutput() {
        try {
            // Take input the number of month
            dprint("-------------------------------------");
            dprint("Input the number of month.");
            String inputNumberOfMonth = nextToken();
            if (inputNumberOfMonth == null)
                return;

            int numberOfMonth = Integer.parseInt(inputNumberOfMonth);
            dprint("The number of month is:", numberOfMonth);

            if (!(1 <= numberOfMonth && numberOfMonth <= 12)) {
                dprint(numberOfMonth, " is an invalid input!");
                return;
            }

            dprint("-------------------------------------");
            System.out.println(getDaysInMonth(numberOfMonth));
            dprint("-------------------------------------");
        } catch (Exception exception) {
            if (debug)
                exception.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new dagatal(false).generateOutput();
    }
}