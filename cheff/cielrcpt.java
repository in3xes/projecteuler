public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    int count = 0;
	    int N = toInt(r.readLine());
	    count = N / 2048;
	    N = N % 2048;
	    while(N > 0) {
		count++;
		N = N & (N - 1);
	    }

	    prnt(count);
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
    public static int toInt(String s) {
	return Integer.parseInt(s);
    }
}
