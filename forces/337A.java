import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));


	StringTokenizer st = new StringTokenizer(r.readLine());
	int n = toInt(st.nextToken());
	int m = toInt(st.nextToken());
	int[] arr = new int[m];
	st = new StringTokenizer(r.readLine());
	for(int i = 0; i < m; i++)
	    arr[i] = toInt(st.nextToken());

	Arrays.sort(arr);

	int diff = arr[n-1] - arr[0];
	for(int i = 1; i <= m-n; i++) {
	    if(arr[i+n-1] - arr[i] < diff)
		diff = arr[i+n-1] - arr[i];
	}
	prnt(diff);
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
