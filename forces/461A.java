import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int N = toInt(r.readLine());
	long[] arr = new long[N];
	StringTokenizer st = new StringTokenizer(r.readLine());

	for(int i = 0; i < N; i++) {
	    arr[i] = toLong(st.nextToken());
	}
	long answer = 0;
	Arrays.sort(arr);
	for(int i = 1; i < N; i++) {
	    answer = answer+arr[i-1]*(i+1);
	}
	answer = answer + arr[N-1]*N;
	prnt(answer);
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
