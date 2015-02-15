import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));


	int lines = toInt(r.readLine());
	for(int j = 0; j < lines; j++) {
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    int n = toInt(st.nextToken());
	    int k = toInt(st.nextToken());
	    int p = toInt(st.nextToken());
	    if ( (n - k) < p) {
		st = new StringTokenizer(r.readLine());
		for(int i = 0; i < k; i++) {
		    int tmp = toInt(st.nextToken());
		}
		prnt(-1);
	    }
	    else {
		st = new StringTokenizer(r.readLine());
		for(int i = 0; i < k; i++) {
		    int tmp = toInt(st.nextToken());
		    if(tmp <= p)
			p++;
		}
		prnt(p);
	    }
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
