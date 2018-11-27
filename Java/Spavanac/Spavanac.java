// Name: Mylene Martodihardjo

import java.io.PrintStream;
import java.util.Scanner;

public class Spavanac {
	public static final int MINUTES_EARLIER = 45;
	public static final int MINUTES_IN_HOUR = 60;
	public static final int HOURS_IN_DAY = 24;
	
	PrintStream out;
	Scanner in;
	int newMinutes;
	int newHours;
	
	Spavanac(){
		out = new PrintStream(System.out);
		in = new Scanner(System.in);
	}
	
	void start(){
		int hours = in.nextInt();
		int minutes = in.nextInt();
		
		newMinutes = minutes - MINUTES_EARLIER;
		newHours = hours;
		
		if (newMinutes < 0){
			int negativeMinutes = newMinutes;
			
			newMinutes = MINUTES_IN_HOUR + negativeMinutes;
			newHours -= 1;
		}
		
		if (newHours < 0){
			int negativeHours = newHours;
			
			newHours = HOURS_IN_DAY + negativeHours;
		}
		
		out.printf("%d %d", newHours, newMinutes);
	}
	
	public static void main(String[] argv){
		new Spavanac().start();
	}
}