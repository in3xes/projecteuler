import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	StringTokenizer st = new StringTokenizer(r.readLine(), "+");
	int n = st.countTokens();
	Integer[] arr = new Integer[n];
	for(int i = 0; i < n; i++) {
	    arr[i] = toInt(st.nextToken());
	}
	Arrays.sort(arr);

	StringBuffer sb = new StringBuffer();
	for(int i = 0; i < n; i++) {
	    sb.append(arr[i]);
	    if(i != n -1)
		sb.append("+");
	}

	prnt(sb.toString());
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
