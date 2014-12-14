import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    int n = toInt(st.nextToken());
	    int l = toInt(st.nextToken());
	    int[] arr = new int[n];
	    st = new StringTokenizer(r.readLine());
	    for(int j = 0; j < n; j++)
		arr[j] = toInt(st.nextToken());
	    
	    int ans = 0^l;
	    for(int j = 0; j < n; j++) {
		int tmp=0;
		for(int k = j; k < n; k++) {
		    tmp = arr[k]^tmp;
		    if((tmp^l) > ans)
			ans = tmp^l;
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
