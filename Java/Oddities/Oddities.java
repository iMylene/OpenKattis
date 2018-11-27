// Name: Mylene Martodihardjo

import java.io.*;

public class Oddities {
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(input.readLine());
		
		for(int i = 0; i<n; i++){
			int number = Integer.parseInt(input.readLine());

			if((Math.abs(number)%2) == 0){
				System.out.printf("%d is even\n", number);
			}else{
				System.out.printf("%d is odd\n", number);
			}
		}
	}
}