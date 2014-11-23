import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    StringBuffer sb = new StringBuffer();
	    String A = r.readLine();
	    char[] C = A.toCharArray();
	    int  balance = 0, max_balance = 0;
	    for(char c: C) {
		if(c == '(')
		    balance++;
		else
		    balance--;

		if(max_balance < balance) {
		    max_balance = balance;
		    sb.append('(');
		}

	    }
	    for(int j = 0; j < max_balance; j++)
		sb.append(')');

	    prnt(sb.toString());
	}
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
