import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int n = toInt(r.readLine());
	int rem = 0;
	String ans = "YES";
	while(n != 0) {
	    rem = n%10;
	    n = n / 10;
	    if(rem == 1) {
		continue;
	    }
	    rem = rem + (n%10)*10;
	    n = n/10;
	    if(rem == 14) {
		continue;
	    }
	    rem = rem + (n%10)*100;
	    n = n/10;
	    if(rem == 144)
		continue;

	    ans = "NO";
	    break;
	    
	};

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
