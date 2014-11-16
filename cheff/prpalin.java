public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int n = toInt(r.readLine());
	if(n > 98689)
	    prnt(1003001);
	else {
	    while(true) {
		if(isPrime(n)) {
		    if(isPalin(n)) {
			prnt(n);
			break;
		    }
		}
		n++;
	    }
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

    
    public static boolean isPrime(int n) {
	if(n<2)
	    return false;
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

    static boolean isPalin(int n) {
	int t=n;
	int rev=0;
	while(t!=0)
	    {
		int rem=t%10;
		rev=(rev*10)+rem;
		t=t/10;
	    }
	if(rev==n)
	    return true;
	return false;
    }
}
