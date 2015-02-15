import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	int n = toInt(r.readLine());
	int[] arr = new int[n];
	int idx[] = new int[50];
	StringTokenizer st = new StringTokenizer(r.readLine());
	for(int i = 0; i < n; i++) {
	    arr[i] = toInt(st.nextToken());
	}

	for(int i = 0; i < n-1; i++) {
	    for(int j = i +1; j < n; j++) {
		if(GCD(arr[i], arr[j]) == 1) {
		    idx[arr[i]]++;
		    idx[arr[j]]++;
		}
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
    static int GCD(int a, int b) {
	if(a % b == 0)
	    return b;

	return GCD(b, a % b);
    }
}
