package kattis.counting;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class counting {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String line = bufferedReader.readLine();

        if(line != null){
            StringTokenizer stringTokenizer = new StringTokenizer(line);
            if(stringTokenizer.hasMoreTokens()){
                int input = Integer.parseInt(stringTokenizer.nextToken());

                for (int i = 1; i <= 12; i++) {
                    System.out.println(input * i);
                }
            }
        }
    }
}