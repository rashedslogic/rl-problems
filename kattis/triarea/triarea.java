package kattis.triarea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class triarea { 
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = reader.readLine();
        
        if (line != null) {
            StringTokenizer tokenizer = new StringTokenizer(line);
            if (tokenizer.countTokens() >= 2) {
                double h = Double.parseDouble(tokenizer.nextToken());
                double b = Double.parseDouble(tokenizer.nextToken());
                
                h = Math.max(1.0, Math.min(h, 1000.0));
                b = Math.max(1.0, Math.min(b, 1000.0));
                
                double area = 0.5 * h * b;
                
                System.out.printf("%.9f\n", area);
            }
        }
    }
}