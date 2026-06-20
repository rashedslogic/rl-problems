package template;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class template {

    private final boolean debug;
    private final BufferedReader bufferedReader;
    private StringTokenizer stringTokenizer;

    public template(boolean debug) {
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
            // // Take input from user
            // dprint("-------------------------------------");
            // dprint("Input the number.");
            // String inputNumber = nextToken();
            // if (inputNumber == null)
            //     return;

            // int number = Integer.parseInt(inputNumber);
            // dprint("The number is:", number);

            dprint("-------------------------------------");
            System.out.println("Hello Output!");
            dprint("-------------------------------------");
        } catch (Exception exception) {
            dprint(exception.getMessage());
        }
    }

    public static void main(String[] args) {
        new template(false).generateOutput();
    }
}