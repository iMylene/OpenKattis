// Name: Mylene Martodihardjo

import java.util.*;
import java.io.*;

public class Cold {
	PrintStream out;
	Scanner in;
	
	Cold(){
		out = new PrintStream(System.out);
		in = new Scanner(System.in);
	}
	
	void start(){
		in.nextLine();
		String collection = in.nextLine();
		int counter = (collection.length()) - (collection.replace("-", "").length());
		out.printf("%d", counter);
	}

	public static final void main(String[] argv){
		new Cold().start();
	}
}