// Name: Mylene Martodihardjo

import java.io.PrintStream;
import java.util.Scanner;

public class Conundrum {
	static final int LENGTH_PER = 3;
	
	PrintStream out;
	Scanner in;
	
	Conundrum(){
		out = new PrintStream(System.out);
		in  = new Scanner(System.in);
	}
	
	void start(){
		String cipherText 	 = in.next();
		int lengthCipherText = cipherText.length();
		int numberOfPer	  	 = lengthCipherText/LENGTH_PER;
		
		String onlyPers = "";
		for(int i = 0; i < numberOfPer; i++){
			onlyPers += "PER";
		}
		
		int counter = 0;
		for(int j = 0; j < lengthCipherText; j++){
			if(cipherText.charAt(j) != onlyPers.charAt(j)){
				counter++;
			}
		}
		out.printf("%d",counter);
	}
	
	public static void main(String[] argv){
		new Conundrum().start();
	}
}