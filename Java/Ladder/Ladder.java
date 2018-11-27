// Name: Mylene Martodihardjo

import java.io.*;

public class Ladder {
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		String [] number = input.readLine().split(" ");
	
		int h = Integer.parseInt(number[0]);
		double v = Math.toRadians(Integer.parseInt(number[1]));
		int s = (int) Math.ceil(h/Math.sin(v));
		System.out.printf("%d",s);
	
	}
}