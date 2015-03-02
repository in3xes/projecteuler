import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	StringTokenizer st = new StringTokenizer(r.readLine());
	long a = toLong(st.nextToken());
	long b = toLong(st.nextToken());
	long m = 1000000007;

	long product = 1;
	while(b > 0) {
	    // if b is odd
	    if(b % 2 == 1) {
		product = product * a;
		if (product > m)
		    product %= m;
	    }
	    a = a*a;
	    if (a > m)
		a %= m;

	    b /= 2;
	}
	prnt(product);
    }

    public static void prnt(String s) {
	System.out.println(s);
    }
    public static void prnt(int s) {
	System.out.println(s);
    }
    public static void prnt(double s) {
	System.out.println(s);
    }
    public static void prnt(long s) {
	System.out.println(s);
    }
    public static void prnt(char s) {
	System.out.println(s);
    }
    public static int toInt(String s) {
	return Integer.parseInt(s);
    }
    public static long toLong(String s) {
	return Long.parseLong(s);
    }
}
