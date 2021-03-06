import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    int size = toInt(r.readLine());
	    int[] arr = new int[100001];
	    StringTokenizer st = new StringTokenizer(r.readLine());
	    int sum = 0;
	    int max = 0;
	    int index = -1;
	    for(int j = 0; j < size; j++) {
		int tmp = toInt(st.nextToken());
		arr[tmp]++;
		sum = sum + tmp;

		if(arr[tmp] > max) {
		    max = arr[tmp];
		    index = tmp;
		}
	    }
	    int s = 0;
	    for(int j = 0; j < 100001; j++) {
		if(sum > (size * j)) {
		    if(s < arr[j])
			s = arr[j];
		}
	    }

	    prnt(size - s);
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
