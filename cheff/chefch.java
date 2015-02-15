import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    String s = r.readLine();
	    int len = s.length();
	    char[] ca = s.toCharArray();
	    char c = ca[0];
	    int ans = 0;
	    for(int j = 1; j < len; j++) {
		if( j % 2 == 0) {
		    if(ca[j] != c)
			ans++;
		}
		else {
		    if(ca[j] == c)
			ans++;
		}
	    }
	    if(ans > len/2)
		prnt(len - ans);
	    else
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
