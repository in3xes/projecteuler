import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	StringTokenizer st = new StringTokenizer(r.readLine());
	int N = toInt(st.nextToken());
	int X = toInt(st.nextToken());
	int Y = toInt(st.nextToken());
	st = new StringTokenizer(r.readLine());
	int[] arr = new int[N];
	for(int i = 0; i < N; i++) {
	    arr[i] = toInt(st.nextToken());
	}
	long ans = 0;
	st = new StringTokenizer(r.readLine());
	for(int i = 0; i < N; i++) {
	    int n = arr[i];
	    ans = ans + Math.max(n, toInt(st.nextToken()));
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
