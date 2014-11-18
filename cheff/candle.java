import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    int m = toInt(st.nextToken());
	    int index = 1, min = toInt(st.nextToken());
	    for(int j = 2; j < 10; j++) {
		int temp = toInt(st.nextToken());
		if(min > temp) {
		    min = temp;
		    index = j;
		}
	    }

	    long ans = 0;
	    if(min > m) {
		ans = 1;
		min = m;
		index = 0;
	    }
	    for(int j = 0; j < min+1; j++) {
		ans = ans * 10;
		ans = ans + index;
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
