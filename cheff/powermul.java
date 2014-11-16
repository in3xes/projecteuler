public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));

	int lines = Integer.parseInt(r.readLine());
	int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 1};
	int[] all_primes = new int[9592];
	int[] product = new int[9592];
	int index = 65;
	for(int i = 0; i < 64; i++)
	    all_primes[i] = primes[i];
	for(int i = 2; i < 100000; i++) {
	    int num = i;
	    for(int j: primes) {
		if(j == 1) {
		    all_primes[index] = num;
		    index++;
		}
		if(num % j == 0)
		    break;
	    }
	}
	int n = 4;
	int num = 0;
	for(int i= 2; i<=n; i++) {
	    num = i;
	    for(int j = 0; all_primes[j]<=num; j++) {
		while(num%all_primes[j] == 0) {
		    product[j] = product[j] + i;
		    num = num/all_primes[j];
		}
	    }
	}
	// for(int j = 0; all_primes[j] <= n; j++) {
	//     System.out.printf("%d, ", all_primes[j]);
	//     prnt(product[j]);
	// }
	// for(int i = 0; i< 100; i++)
	//     prnt(all_primes[i]);
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
}
