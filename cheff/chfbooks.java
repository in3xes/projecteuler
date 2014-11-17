import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    String[] s = r.readLine().split(" ");
	    int n = toInt(s[0]);
	    int m = toInt(s[1]);
	    int[] arr = new int[10000];
	    String[] values = r.readLine().split(" ");
	    for(int j = 0; j < n; j++) {
		arr[10000-n+j] = toInt(values[j]);
	    }

	    Arrays.sort(arr);
	    long ans = 0;
	    for(int j = 10000-n; j < 10000-n+m; j++) {
		// prnt(arr[j]);
		ans = ans - arr[j];
	    }
	    // prnt(ans);
	    for(int j = 10000-n+m; j < 10000; j++) {
		// prnt(arr[j]);
		ans = ans + arr[j];
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
}
