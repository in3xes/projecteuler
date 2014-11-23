import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    int N = toInt(r.readLine());
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    boolean ans = true;
	    int[] A = new int[N];
	    for(int j = 0; j < N; j++)
		A[j] = toInt(st.nextToken());

	    for(int j = 0; j < N; j++)
		for(int k = j+2; k < N; k++)
		    if(A[j] > A[k]) {
			ans = false;
			break;
		    }

	    if(ans)
		prnt("YES");
	    else
		prnt("NO");
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
