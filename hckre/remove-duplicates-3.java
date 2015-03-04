import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	String s = r.readLine();
	String ans = "";
	int len = s.length();
	int[] h = new int[26];

	for(char c: s.toCharArray()) {
	    int index = hash(c);
	    if(h[index] == 0) {
		ans = ans + c;
		h[index] = 1;
	    }
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
    static int hash(char c) {
	int ascii = (int)c;
	return c%97;
    }
}
