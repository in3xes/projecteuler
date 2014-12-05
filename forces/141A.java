import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	String s1 = r.readLine();
	String s2 = r.readLine();
	String s = s1 + s2;

	String s3 = r.readLine();
	
	char[] ca1 = s.toCharArray();
	char[] ca2 = s3.toCharArray();

	Arrays.sort(ca1);
	Arrays.sort(ca2);

	if(ca1.length != ca2.length)
	    prnt("NO");
	else {
	     String ans = "YES";
	     for(int i = 0; i < ca1.length; i++)
		 if(ca1[i] != ca2[i]) {
		     ans = "NO";
		     break;
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
