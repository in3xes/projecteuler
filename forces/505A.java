import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	String str = r.readLine();
	String orig = str;
	String rev = new StringBuffer(str).reverse().toString();

	int len = str.length();
	int index = -1;
	for(int i = 0; i < len; i++) {
	    if(str.charAt(i) != rev.charAt(i)) {
		index = i;
		break;
	    }
	}
	
	if(index != -1) {
	    rev = rev.substring(0, index) + str.charAt(index) + rev.substring(index, len);
	    str = new StringBuffer(rev).reverse().toString();
	    if(str.equals(rev))
		prnt(str);
	    else {
		str = orig;
		rev = new StringBuffer(str).reverse().toString();
		str = str.substring(0, index) + rev.charAt(index) + str.substring(index, len);
		rev = new StringBuffer(str).reverse().toString();
		if(str.equals(rev))
		    prnt(str);
		else
		    prnt("NA");
	    }
	}
	else {
	    if(len%2  == 0)
		str = str.substring(0, len/2) + "a" + str.substring(len/2, len);
	    else
		str = str.substring(0, len/2 + 1) + str.charAt(len/2) + str.substring(len/2 + 1, len);
	    prnt(str);
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
