import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	StringTokenizer st = new StringTokenizer(r.readLine());
	int n = toInt(st.nextToken());
	int k = toInt(st.nextToken());
	int[] arr = new int[n];
	st = new StringTokenizer(r.readLine());
	for(int i = 0; i < n; i++)
	    arr[i] = toInt(st.nextToken());

	Arrays.sort(arr);

	int ans = 0;
	int i = 2;
	while(i < n) {
	    if((5 - arr[i]) >= k)
		ans++;
	    else 
		break;
	    
	    i = i + 3;
	};

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
