// Name: Mylene Martodihardjo

import java.io.*;
import java.util.*;

public class Modulo {
	static final int B = 42;
	
	PrintStream out;
	Scanner in;
	
	Modulo(){
		out = new PrintStream(System.out);
		in = new Scanner(System.in);
	}
	
	void start(){
		Set <Integer> moduloSet = new TreeSet<Integer>();
		for (int i=0; i<10; i++){
			int a = in.nextInt();
			int modulo = a%B;
			moduloSet.add(modulo);
		}
		int distinctNumbers = moduloSet.size();
		out.printf("%d",distinctNumbers);
	}
	
	public static void main(String[] argv){
		new Modulo().start();
	}
}