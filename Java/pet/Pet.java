// Name: Mylene Martodihardjo

import java.io.*;

public class Pet {
	public static final int NUMBER_OF_CONTESTANTS = 5;
	public static final int NUMBER_OF_POINTS = 4;
	public static final int MAX_POINTS = NUMBER_OF_POINTS * 5;
	public static final int MIN_POINTS = NUMBER_OF_POINTS * 1;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int winnerPoints = MIN_POINTS;
		int winner = 1;
		
		for(int i = 0; i<NUMBER_OF_CONTESTANTS; i++){
			String[] pointsString = br.readLine().split(" ");
			int totalPoints = 0;
	
			for(int k = 0; k<pointsString.length; k++){
				totalPoints += Integer.parseInt(pointsString[k]);
			}
				
			if (totalPoints>winnerPoints){
				winnerPoints = totalPoints;
				winner = i+1;
			}
		}
		System.out.printf("%s %s\n",winner,winnerPoints);
    }
}