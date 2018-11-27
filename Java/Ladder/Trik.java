// Name: Mylene Martodihardjo

import java.io.*;

public class Trik {
	public static final int START = 1;
	
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		String[] move = input.readLine().split("");
		int numberOfMoves = move.length;
		
		int positionBall = START;
		for(int i = 0; i<numberOfMoves; i++){
			if(move[i].equals("A") && positionBall == 1){
				positionBall = 2;
			}
			
			if(move[i].equals("A") && positionBall == 2){
				positionBall = 1;
			}
			
			if(move[i].equals("B") && positionBall == 2){
				positionBall = 3;
			}
			
			if(move[i].equals("B") && positionBall == 3){
				positionBall = 1;
			}
			
			if(move[i].equals("C") && positionBall == 1){
				positionBall = 3;
			}
			
			if(move[i].equals("C") && positionBall == 3){
				positionBall = 1;
			}
		}
		System.out.printf("%d\n", positionBall);
	}
}