public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));
	
	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    String[] sides = r.readLine().split(" ");
	    long L = toInt(sides[0]);
	    long B = toInt(sides[1]);
	    if(isPrime(L))
		L--;
	    if(isPrime(B))
		B--;

	    if(L == 2)
		L = 1;
	    if(B == 2)
		B = 1;

	    prnt(L*B);
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
    public static boolean isPrime(long n) {
	if(n < 2)
	    return false;
	if(n < 4)
	    return true;
	else if(n%2==0||n%3==0)
	    return false;
	int srt=(int)Math.sqrt(n)+1;
	for(int i=6;i<=srt;i+=6)
	    {
		if(n%(i-1)==0||n%(i+1)==0)
		    return false;
	    }
	return true;
    }
}
