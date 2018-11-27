// Name: Mylene Martodihardjo

import java.io.*;

public class Ptice {
	public static final String ADRIAN = "ABC";
	
	public static final String BRUNO = "BABC";
	
	public static final String GORAN = "CCAABB";
	
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int numberOfQuestions = Integer.parseInt(input.readLine());
		String answer = input.readLine();
		
		int counterAdrian = 0;
		int counterBruno = 0;
		int counterGoran = 0;
		
		int a = 0;
		int b = 0;
		int g = 0;
		
		for(int i = 0; i<numberOfQuestions; i++){
			if(i%ADRIAN.length() == 0){
				a = 0;
			}
			if(answer.charAt(i) == ADRIAN.charAt(a)){
				counterAdrian += 1;
			}
			a += 1;
			
			if(i%BRUNO.length() == 0){
				b = 0;
			}
			if(answer.charAt(i) == BRUNO.charAt(b)){
				counterBruno += 1;
			}
			b += 1;
			
			if(i%GORAN.length() == 0){
				g = 0;
			}
			if(answer.charAt(i) == GORAN.charAt(g)){
				counterGoran += 1;
			}
			g += 1;
		}

		
		if(counterAdrian>=counterBruno && counterAdrian>=counterGoran){
			System.out.printf("%d\nAdrian\n",counterAdrian);
			
			if(counterAdrian == counterBruno){
				System.out.printf("Bruno\n");
			}
			if(counterAdrian == counterGoran){
				System.out.printf("Goran");
			}
			
		}else if(counterBruno>=counterGoran){
			System.out.printf("%d\nBruno\n",counterBruno);
			
			if(counterBruno == counterGoran){
				System.out.printf("Goran");
			}
			
		}else{
			System.out.printf("%d\nGoran",counterGoran);
		}
	}
}