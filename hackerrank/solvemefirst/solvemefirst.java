package hackerrank.solvemefirst;

import java.util.*;

public class solvemefirst {

    static int solveMeFirst(int a, int b) {
      	// Hint: Type return a+b; below 
        a = a<1 ? 1 : a;
        b = b>1000 ? 1000 : b;
        return a + b;
   }

 public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a;
        a = in.nextInt();
        int b;
        b = in.nextInt();
        int sum;
        sum = solveMeFirst(a, b);
        System.out.println(sum);
   }
}