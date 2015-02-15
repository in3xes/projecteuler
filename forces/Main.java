import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int n = toInt(r.readLine());
	int digit = 0;
	int ans = 0;
	int multipler = 1
	while(n > 0) {
	    digit = n % 10;
	    n = n / 10;
	    if(digit >= 5) {
		if(n == 0 && digit == 9)
		    digit = 9;
		else
		    digit = 9 - digit;
	    }
	    ans = ans * 10 + digit;
	}
	prnt(ans);
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
