import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    int n = toInt(st.nextToken());
	    int k = toInt(st.nextToken());
	    long[] arr = new long[n];
	    long sum = 0;
	    String ans = "yes";
	    st = new StringTokenizer(r.readLine());
	    for(int j = 0; j < n; j++) {
		arr[j] = toInt(st.nextToken());
		sum += arr[j];
	    }
	    if(sum%k != 0)
		ans = "no";
	    else {
	    	long tmp = sum / k;
	    	for(int j = 0; j < n/2 + 1; j++) {
	    	    if(Arrays.binarySearch(arr, tmp - arr[j]) <= 0) {
	    		ans = "no";
	    		break;
	    	    }
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
}
