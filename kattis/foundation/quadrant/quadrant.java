package kattis.foundation.quadrant;

import java.io.InputStream;
import java.io.PrintWriter;
import java.io.BufferedOutputStream;

public class quadrant {

    private static final boolean DEBUG = false;
    private static PrintWriter out;
    private static long startRuntime;

    private static void init() {
        out = new PrintWriter(new BufferedOutputStream(System.out));

        if (DEBUG) {
            startRuntime = System.nanoTime();
        }
    }

    private static void close() {
        if (DEBUG) {
            long endRuntime = System.nanoTime();
            double totalRuntime = (endRuntime - startRuntime) / 1_000_000_000.0;
            System.err.println(String.format("[Algorithmic Runtime] %.6f seconds", totalRuntime));
        }

        out.flush();
    }

    private static void solve() {
        // Take the coordinate input
        Integer inputX = FastScanner.nextInt();
        Integer inputY = FastScanner.nextInt();
        boolean extraInput = FastScanner.hasNext();
        if (inputX == null || inputY == null || extraInput) {
            dPrint("Wrong input");
            return;
        }

        // Is valid input
        dPrint("Parsed Coordinates -> X:", inputX, "Y:", inputY);
        if (!isValidCoordinate(inputX) || !isValidCoordinate(inputY)) {
            dPrint("Invalid input");
            return;
        }

        // Find quadrant
        if (inputX > 0 && inputY > 0) {
            out.println("1");
        } else if (inputX < 0 && inputY > 0) {
            out.println("2");
        } else if (inputX < 0 && inputY < 0) {
            out.println("3");
        } else if (inputX > 0 && inputY < 0) {
            out.println("4");
        } else {
            out.println("Unknown coordinate");
        }
    }

    public static void main(String[] args) {
        init();
        solve();
        close();
    }

    static class FastScanner {
        private static final int BUFFER_SIZE = 1 << 16; // 64KB hardware chunk block
        private static final InputStream in = System.in;
        private static final byte[] buffer = new byte[BUFFER_SIZE];
        private static int bufferPointer = 0;
        private static int bytesRead = 0;

        private static boolean fillBuffer() {
            try {
                bytesRead = in.read(buffer, 0, BUFFER_SIZE);
                bufferPointer = 0;
                return bytesRead > 0;
            } catch (Exception e) {
                return false;
            }
        }

        private static byte readByte() {
            if (bufferPointer >= bytesRead) {
                if (!fillBuffer())
                    return -1;
            }
            return buffer[bufferPointer++];
        }

        public static boolean hasNext() {
            while (true) {
                if (bufferPointer >= bytesRead) {
                    if (!fillBuffer())
                        return false;
                }
                if (buffer[bufferPointer] > 32)
                    return true;
                bufferPointer++;
            }
        }

        public static int nextInt() {
            byte c = readByte();
            while (c <= 32) {
                if (c == -1)
                    return 0;
                c = readByte();
            }
            boolean negative = false;
            if (c == '-') {
                negative = true;
                c = readByte();
            }
            int value = 0;
            while (c > 32) {
                if (c >= '0' && c <= '9') {
                    value = (value * 10) + (c - '0');
                }
                c = readByte();
            }
            return negative ? -value : value;
        }

        public static long nextLong() {
            byte c = readByte();
            while (c <= 32) {
                if (c == -1)
                    return 0L;
                c = readByte();
            }
            boolean negative = false;
            if (c == '-') {
                negative = true;
                c = readByte();
            }
            long value = 0;
            while (c > 32) {
                if (c >= '0' && c <= '9') {
                    value = (value * 10) + (c - '0');
                }
                c = readByte();
            }
            return negative ? -value : value;
        }

        public static double nextDouble() {
            if (!hasNext())
                return 0.0;
            byte c = readByte();
            while (c <= 32)
                c = readByte();
            boolean negative = false;
            if (c == '-') {
                negative = true;
                c = readByte();
            }
            double value = 0;
            while (c > 32 && c != '.') {
                if (c >= '0' && c <= '9') {
                    value = (value * 10) + (c - '0');
                }
                c = readByte();
            }
            if (c == '.') {
                c = readByte();
                double multiplier = 1.0;
                while (c > 32) {
                    if (c >= '0' && c <= '9') {
                        multiplier /= 10.0;
                        value += (c - '0') * multiplier;
                    }
                    c = readByte();
                }
            }
            return negative ? -value : value;
        }

        public static String next() {
            if (!hasNext())
                return null;
            StringBuilder sb = new StringBuilder();
            byte c = readByte();
            while (c <= 32) {
                if (c == -1)
                    return null;
                c = readByte();
            }
            while (c > 32) {
                sb.append((char) c);
                c = readByte();
            }
            return sb.toString();
        }
    }

    private static void dPrint(Object message) {
        if (DEBUG)
            System.err.println("[DEBUG] " + message);
    }

    private static void dPrint(Object... args) {
        if (DEBUG) {
            StringBuilder sb = new StringBuilder("[DEBUG] ");
            for (int i = 0; i < args.length; i++) {
                sb.append(args[i]).append(i < args.length - 1 ? " " : "");
            }
            System.err.println(sb.toString());
        }
    }

    private static boolean isValidCoordinate(int value) {
        int min = -1000;
        int max = 1000;
        return min <= value && value <= max && value != 0;
    }
}