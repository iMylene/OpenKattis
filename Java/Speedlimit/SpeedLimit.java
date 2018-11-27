// Name: Mylene Martodihardjo

import java.io.*;

public class SpeedLimit {
	public static final int STOP = -1;
	
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		
		while(true){
			int numberOfValues = Integer.parseInt(input.readLine());
			
			if (numberOfValues == STOP){
				break;
			}else{
				int oldTime = 0;
				int sum = 0;
				
				for(int i=0; i<numberOfValues;i++){
					String[] pair = input.readLine().split(" ");
					
					int speed = Integer.parseInt(pair[0]);
					int totalElapsedTime = Integer.parseInt(pair[1]);
					int time = totalElapsedTime - oldTime;
					oldTime = totalElapsedTime;
				
					sum += speed*time;
				}
				System.out.printf("%d miles \n", sum);
			}		
		}
	}
}