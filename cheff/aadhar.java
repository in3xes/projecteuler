import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    char[] c1 = st.nextToken().toCharArray();
	    char[] c2 = st.nextToken().toCharArray();
	    int[] buf = new int[256];
	    for(char c: c1) {
		buf[(int)c]++;
	    }
	    for(char c: c2) {
		buf[(int)c]--;
	    }
	    String ans = "YES";
	    for(int j = 0; j < 256; j++) {
		if(buf[j] != 0) {
		    ans = "NO";
		    break;
		}
	    }

	    prnt(ans);
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
