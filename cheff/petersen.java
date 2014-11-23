import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	int[][] graph = new int[][] {{0, 1, 0, 0, 1, 1, 0, 0, 0, 0},
			     {1, 0, 1, 0, 0, 0, 1, 0, 0, 0},
			     {0, 1, 0, 1, 0, 0, 0, 1, 0, 0},
			     {0, 0, 1, 0, 1, 0, 0, 0, 1, 0},
			     {1, 0, 0, 1, 0, 0, 0, 0, 0, 1},
			     {1, 0, 0, 0, 0, 0, 0, 1, 1, 0},
			     {0, 1, 0, 0, 0, 0, 0, 0, 1, 1},
			     {0, 0, 1, 0, 0, 1, 0, 0, 0, 1},
			     {0, 0, 0, 1, 0, 1, 1, 0, 0, 0},
			     {0, 0, 0, 0, 1, 0, 1, 1, 0, 0}};
	for(int i = 0; i < lines; i++) {
	    String S = r.readLine();
	    int length = S.length();
	    char[] C = S.toCharArray();
	    String ans = "";
	    int index = ((int)C[0]) % 65;
	    for(int j = 0; j < length - 1; j++) {
		int second = (int)C[j + 1] % 65;
		if(graph[index][second] == 1)
		    ans += index;
		else if(graph[index][second + 5] == 1) {
		    ans += index;
		    second = second + 5;
		}
		else if(graph[(index + 5)%10][second] == 1)
		    ans += (index + 5) % 10;
		else if(graph[(index + 5)%10][second + 5] == 1) {
		    ans += (index + 5) % 10;
		    second = second + 5;
		}
		else {
		    ans = "-1";
		    break;
		}
		index = second;
	    }
	    if(ans.equals("-1"))
		prnt(ans);
	    else
		ans += (index = ((int)C[length - 1]) % 65);

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
