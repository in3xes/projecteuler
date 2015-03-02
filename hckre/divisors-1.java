import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	StringTokenizer st = new StringTokenizer(r.readLine());
	long n = toLong(st.nextToken());
	long a = toLong(st.nextToken());
	long b = toLong(st.nextToken());

	long g = GCD(a, b);
	long tmp = (a*b)/g;
	prnt(n/a + n/b - n/(tmp));
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
    static long GCD(long a, long b) {
	if(a % b == 0)
	    return b;

	return GCD(b, a % b);
    }
}
