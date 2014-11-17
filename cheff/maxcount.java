public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    int size = toInt(r.readLine());
	    String[] values = r.readLine().split(" ");
	    int[] count = new int[10001];
	    for(int j = 0; j < size; j++)
		count[toInt(values[j])]++;

	    int v=0, c =0;
	    for(int j = 0; j < 10001; j++) {
		if(count[j] > c) {
		    v = j;
		    c = count[j];
		}
	    }
	    prnt(v + " " + c);
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
