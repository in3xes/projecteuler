public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));

	int N = Integer.parseInt(r.readLine());
	int[] A = new int[1000];
	String[] Ai = r.readLine().split(" ");
	int[][] F = new int[1000][2];
	for(int i = 0; i < N; i++)
	    A[i] = Integer.parseInt(Ai[i]);

	for(int i = 0; i < N; i++) {
	    String[] B = r.readLine().split(" ");
	    F[i][0] = Integer.parseInt(B[0]) - 1;
	    F[i][1] = Integer.parseInt(B[1]) - 1;
	}
	int Q = Integer.parseInt(r.readLine());
	for(int i = 0; i < Q; i++) {
	    int a, b, c;
	    String[] actions = r.readLine().split(" ");
	    a = Integer.parseInt(actions[0]);
	    b = Integer.parseInt(actions[1]) - 1;
	    c = Integer.parseInt(actions[2]);

	    if(a == 1)
		A[b] = c;
	    else {
		int[] Final_F = new int[1000];
		for(int j = b; j < c; j++) {
		    int L = F[j][0];
		    int R = F[j][1];
		    for(int k = L; k<= R; k++)
			Final_F[k]++;
		}
		long result = 0;
		for(int j = 0; j < N; j++) {
		    result = result + Final_F[j] * A[j];
		}
		prnt(result);
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

}
