import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	StringTokenizer st = new StringTokenizer(r.readLine());
	int n = toInt(st.nextToken());
	int q = toInt(st.nextToken());
	int[] arr = new int[n];
	st = new StringTokenizer(r.readLine());
	for(int i = 0; i < n; i++) {
	    arr[i] = toInt(st.nextToken());
	}
	for(int i = 0; i < q; i++) {
	    st = new StringTokenizer(r.readLine());
	    int a = toInt(st.nextToken()) - 1;
	    int b = toInt(st.nextToken()) - 1;

	    int ans = 0;
	    for(int j = a; j < b; j++) {
		int tmp = arr[j];
		for(int k = j+1; k <= b; k++) {
		    if(tmp > arr[k])
			ans++;
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
