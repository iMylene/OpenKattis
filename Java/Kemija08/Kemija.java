// Name: Mylene Martodihardjo

import java.io.*;

public class Kemija {
	
	static int jumpMethode(char i){
		switch(i){
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u':
				return 2;
			default:
				return 0;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		String words = input.readLine();
		
		for(int i = 0; i<words.length(); i++){
			char j = words.charAt(i);
			int jump = jumpMethode(j);
			System.out.printf("%c",j);
			i=i+jump;
		}
	}
}