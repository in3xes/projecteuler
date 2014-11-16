public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	String[] input = r.readLine().split(" ");
	int A = toInt(input[0]);
	int B = toInt(input[1]);
	int diff = A - B;
	if(diff % 10 == 9)
	    prnt(--diff);
	else
	    prnt(++diff);
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
