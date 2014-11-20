import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    int N = toInt(st.nextToken());
	    int X = toInt(st.nextToken());
	    st = new StringTokenizer(r.readLine());
	    int[] notes = new int[N];
	    int sum = 0;
	    for(int j = 0; j < N; j++) {
		notes[j] = toInt(st.nextToken());
		sum += notes[j];
	    }
	    int max = sum/X;
	    boolean adequate = true;
	    for(int j = 0; j < N; j++) {
		if((sum - notes[j])/X == max) {
		    prnt(-1);
		    adequate = false;
		    break;
		}
	    }
		if(adequate)
		    prnt(max);
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
