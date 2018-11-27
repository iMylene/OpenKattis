// Name: Mylene Martodihardjo

import java.io.PrintStream;
import java.util.Scanner;

public class Carrots {
	PrintStream out;
	Scanner in;
	
	Carrots(){
		out = new PrintStream(System.out);
		in = new Scanner(System.in);
	}
	
	void start(){
		in.nextInt();
		out.printf("%d",in.nextInt());
	}
	
	public static void main(String[] argv) {
		new Carrots().start();
	}
}