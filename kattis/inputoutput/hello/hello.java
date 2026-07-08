package kattis.inputoutput.hello;

public class hello {

    private final boolean debug;

    public hello(boolean debug) {
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

    public void generateOutput() {
        // Print Hello World!
        dprint("-------------------------------------");
        System.out.println("Hello World!");
        dprint("-------------------------------------");
    }

    public static void main(String[] args) {
        new hello(false).generateOutput();
    }
}