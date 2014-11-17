public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    String[] values = r.readLine().split(" ");
	    int N = toInt(values[0]);
	    if(N == 1)
		prnt(toInt(values[1]));
	    int gcd = GCD(toInt(values[1]), toInt(values[2]));
	    for(int j = 3; j < N + 1; j++) {
		gcd = GCD(toInt(values[j]), gcd);
	    }

	    for(int j = 1; j < N + 1; j++)
		System.out.printf("%d ", toInt(values[j])/gcd);
	prnt("");
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
   static int GCD(int a, int b) {
	if(a % b == 0)
	    return b;

	return GCD(b, a % b);
    }

}
