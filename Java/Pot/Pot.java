// Name: Mylene Martodihardjo

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Pot {
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(input.readLine());
		
		int sum = 0;
		for(int i = 0; i<n; i++){
			String[] term = input.readLine().split("");
			int power = Integer.parseInt(term[term.length - 1]);
			
			String[] numberArray = Arrays.copyOf(term, term.length - 1);
			StringBuilder numberStringBuilder = new StringBuilder();
			
			for(int j = 0; j<numberArray.length; j++){
				numberStringBuilder.append(numberArray[j]);
			}
			
			String numberString = numberStringBuilder.toString();
			int number = Integer.parseInt(numberString);
			
			sum += Math.pow(number, power);
		}
		System.out.printf("%d", sum);
	}
}