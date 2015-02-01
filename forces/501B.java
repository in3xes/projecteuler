import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	Map<String, String> name = new HashMap<String, String>();
	for(int i = 0; i < lines; i++) {
	StringTokenizer st = new StringTokenizer(r.readLine());
	    String o = st.nextToken();
	    String n = st.nextToken();
	    if(name.containsKey(o)) {
		String tmp_value = name.get(o);
		name.remove(o);
		name.put(n, tmp_value);
	    }
	    else {
		name.put(n, o);
	    }
	}

	prnt(name.size());
	for(String s: name.keySet())
	    prnt(name.get(s) + " " + s);
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
