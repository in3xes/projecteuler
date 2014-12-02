import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int n = toInt(r.readLine());
	StringTokenizer st = new StringTokenizer(r.readLine());
	Integer arr[] = new Integer[n];
	int sum = 0;
	for(int i = 0; i < n; i++) {
	    arr[i] = toInt(st.nextToken());
	    sum += arr[i];
	}

	Arrays.sort(arr, Collections.reverseOrder());

	int tmp = 0;
	int ans = 0;
	for(int i = 0; i < n; i++) {
	    tmp += arr[i];
	    ans++;
	    if(tmp > sum/2) {
		prnt(ans);
		break;
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
