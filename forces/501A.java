import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	StringTokenizer st = new StringTokenizer(r.readLine());
	int a = toInt(st.nextToken());
	int b = toInt(st.nextToken());
	int c = toInt(st.nextToken());
	int d = toInt(st.nextToken());

	int pts_m = Math.max((3*a)/10, a - (a*c)/250);
	int pts_v = Math.max((3*b)/10, b - (b*d)/250);

	if(pts_m == pts_v)
	    prnt("Tie");
	else if(pts_m > pts_v)
	    prnt("Misha");
	else
	    prnt("Vasya");

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
