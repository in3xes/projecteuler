public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = toInt(r.readLine());
	for(int i = 0; i < lines; i++) {
	    String s = r.readLine();
	    int size = s.length();
	    char[] ca = s.toCharArray();
	    int[] FQ = new int[256];
	    for(char c: ca){
		FQ[(int)c]++;
	    }

	    int max = 0, index = 0;
	    for(int j = 0; j < 256; j++) {
		if(max < FQ[j]) {
		    max = FQ[j];
		    index = j;
		}
	    }
	    char c = (char)index;
	    for(int j = 0; j < size; j++) {
		if(ca[j] == c)
		    ca[j] = '?';
	    }

	    prnt(new String(ca));
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
