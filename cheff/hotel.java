import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    int N = toInt(r.readLine());
	    int[] enter = new int[N];
	    int[] exit = new int[N];
	    int[] count = new int[1001];
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    for(int j = 0; j < N; j++) {
		enter[j] = toInt(st.nextToken());
	    }
	    st = new StringTokenizer(r.readLine());
	    for(int j = 0; j < N; j++) {
		exit[j] = toInt(st.nextToken());
	    }
	    for(int j = 0; j < N; j++) {
		int start = enter[j];
		int end = exit[j];
		for(int k = start; k < end; k++)
		    count[k]++;
	    }
	    int ans = 0;
	    for(int j = 0; j < 1001; j++) {
		if(ans < count[j])
		    ans = count[j];
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
