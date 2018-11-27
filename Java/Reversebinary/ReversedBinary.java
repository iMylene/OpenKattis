// Name: Mylene Martodihardjo

import java.io.*;

public class ReversedBinary {
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		
		int number = Integer.parseInt(input.readLine());
		String binary = Integer.toBinaryString(number);		
		String inverseBinary = new StringBuffer(binary).reverse().toString();
		int inverseBinaryNumber = Integer.parseInt(inverseBinary,2);
		
		System.out.printf("%d", inverseBinaryNumber);
	}
}