// Name: Mylene Martodihardjo

import java.io.PrintStream;
import java.util.Scanner;

public class MixedFractions {
	PrintStream out;
	Scanner in;
	
	MixedFractions(){
		out = new PrintStream(System.out);
		in = new Scanner(System.in);
	}
	
	void start(){
		while(in.hasNextLine()){
			int numerator = in.nextInt();
			int denominator = in.nextInt();
			
			if (denominator == 0 && numerator == 0){
				break;
			} else if (numerator >= denominator){
				// Improper fraction
				
				int wholeNumber  = numerator/denominator;
				int newNumerator = numerator % denominator;
				out.printf("\n%d %d / %d",wholeNumber,newNumerator,denominator);
			} else if (numerator < denominator){
				// Proper fraction
				
				out.printf("\n%d %d / %d",0,numerator,denominator);
			}
		}
	}
	
	public static void main(String[] argv){
		new MixedFractions().start();
	}
}