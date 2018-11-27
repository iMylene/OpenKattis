// Name: Mylene Martodihardjo

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Eligibility {
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int numberOfCases = Integer.parseInt(input.readLine());
		
		for(int i = 0; i<numberOfCases; i++){
			String[] informationArray = input.readLine().split(" ");
			
			String name = informationArray[0];
			
			String[] dateOfStudy = informationArray[1].split("/");
			int yearOfStudy = Integer.parseInt(dateOfStudy[0]);
			
			String[] dataOfBirth = informationArray[2].split("/");
			int yearOfBirth = Integer.parseInt(dataOfBirth[0]);
			
			int numberOfCourses = Integer.parseInt(informationArray[3]);
			
			if(yearOfStudy>=2010){
				System.out.printf("%s eligible\n", name);
			}else if(yearOfBirth>=1991){
				System.out.printf("%s eligible\n", name);
			}else if(numberOfCourses<41){
				System.out.printf("%s coach petitions\n", name);
			}else{
				System.out.printf("%s ineligible\n", name);
			}
		}
	}
}
