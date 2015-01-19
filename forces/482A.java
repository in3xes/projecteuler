import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	StringTokenizer st = new StringTokenizer(r.readLine());

	int n = toInt(st.nextToken());
	int k = toInt(st.nextToken());

	int ans = 1;
	StringBuilder sb = new StringBuilder("1");
	int loop = 0;
	for(int i = k; i >= 1; i--) {
	    if(loop%2 == 0)
		ans = ans + i;
	    else
		ans = ans - i;
	    sb.append(" " + ans);
	    loop++;
	}

	for(int i = k+2; i <= n; i++)
	    sb.append(" " + i);

	System.out.println(sb);
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
