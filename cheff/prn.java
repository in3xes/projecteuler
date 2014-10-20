import java.util.*;

public class Main {

    public static void main(String[] args) throws java.lang.Exception {
	java.io.BufferedReader r = new java.io.BufferedReader(new java.io.InputStreamReader (System.in));
	int lines = Integer.parseInt(r.readLine());
	String[] e = new String[100];
	for(int i = 0; i < lines; i++) {
	    e[i] = r.readLine();
	}
	for(int i = 0; i < lines; i++) {
	    Stack<Character> s = new Stack<Character>();
	    StringBuilder out = new StringBuilder();
	    for(char c: e[i].toCharArray()) {
		int alpha = (int) c;
		if(c == '(')
		    continue;
		if(c == ')') {
		    out.append(s.pop());
		    continue;
		}
		if(alpha > 96 && alpha < 123) {
		    out.append(c);
		    continue;
		}
		s.push(c);
	    }
	System.out.println(out.toString());
	}
    }
}
