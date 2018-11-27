// Name: Mylene Martodihardjo

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bijele {
	public final static int KING = 1;
	public final static int QUEEN = 1;
	public final static int ROOKS = 2;
	public final static int BISCHOPS = 2;
	public final static int KNIGHTS = 2;
	public final static int PAWNS = 8;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		String[] inputString = input.readLine().split(" ");
		
		int king = Integer.parseInt(inputString[0]);
		int queen = Integer.parseInt(inputString[1]);
		int rooks = Integer.parseInt(inputString[2]);
		int bischops = Integer.parseInt(inputString[3]);
		int knights = Integer.parseInt(inputString[4]);
		int pawns = Integer.parseInt(inputString[5]);
		
		System.out.printf("%d %d %d %d %d %d", KING-king, QUEEN-queen, ROOKS-rooks, BISCHOPS-bischops, KNIGHTS-knights, PAWNS-pawns);
	}
}