import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));
	PrintWriter out = new PrintWriter(System.out,true);
	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    int N = toInt(r.readLine());
	    int[] arr = new int[N];
	    StringTokenizer st = new StringTokenizer(r.readLine());

	    for(int j = 0; j < N; j++)
		arr[j] = toInt(st.nextToken());

	    Arrays.sort(arr);
	    int diff = 1000000000;
	    for(int j = 0; j < N-1; j++) {
		int tmp = arr[j+1] - arr[j];
		if(diff > tmp) {
		    diff = tmp;
		}
	    }
	    out.println(diff);
	}

	out.close();
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
