// Name: Mylene Martodihardjo

import java.util.*;
import java.io.*;

public class Everywhere {
	PrintStream out;
	Scanner in;
	
	Everywhere(){
		out = new PrintStream(System.out);
		in = new Scanner(System.in);
	}
	
	void start(){
		String firstLine = in.nextLine();
		Scanner firstLineScanner = new Scanner(firstLine);
		int numberOfTestCases = firstLineScanner.nextInt();
		
		for(int i=0; i<numberOfTestCases; i++){
			String numberOfTripsLine = in.nextLine();
			Scanner numberOfTripsLineScanner = new Scanner(numberOfTripsLine);
			int numberOfTrips = numberOfTripsLineScanner.nextInt();
			
			Set<String> tripSet = new HashSet<String>();
			
			for(int j=0; j<numberOfTrips; j++){
				String test = in.nextLine();
				tripSet.add(test);
			}
			
			int distinctTrips = tripSet.size();
			out.printf("%d\n", distinctTrips);
		}
	}
	
	public static final void main(String[] argv){
		new Everywhere().start();
	}
}