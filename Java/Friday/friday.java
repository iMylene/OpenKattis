// Assignment: Friday the 13th
// Created on 29 november 2018
// @author: Mylene Martodihardjo

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class friday {
	public static int FRIDAY13TH 	= 1;
	public static int MIN_DAYS 		= 13;
	public static int DAYSINWEEK 	= 7;
	
	public static void main(String[] args) throws IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));		
		int numberOfCases = Integer.parseInt(input.readLine());
		
		for(int i = 0; i<numberOfCases;i++){
			int counterFriday13th = 0;
			String[] arrayData = input.readLine().split(" ");
			
			int monthsInYear = Integer.parseInt(arrayData[1]);
			
			String[] daysInMonthsString = input.readLine().split(" ");
			int[] daysInMonths = new int[monthsInYear];
			for(int monthNumber = 0; monthNumber<monthsInYear; monthNumber ++){
				daysInMonths[monthNumber] = Integer.parseInt(daysInMonthsString[monthNumber]);
			}
			
			int firstSunday = 1;
			int nextSunday = 1;
			for(int monthNumber = 0; monthNumber < monthsInYear; monthNumber++){
				if(monthNumber != 0){
					firstSunday = nextSunday;
				}
				
				if(firstSunday == FRIDAY13TH){
					counterFriday13th ++;
				}
				
				if(monthNumber < monthsInYear - 1 && daysInMonths[monthNumber]>=MIN_DAYS){
					if(daysInMonths[monthNumber]%(DAYSINWEEK) == 0){
						nextSunday = 1;
					}else if(daysInMonths[monthNumber]%(DAYSINWEEK) == 1){
						nextSunday = 7;
					}else if(daysInMonths[monthNumber]%(DAYSINWEEK) == 2){
						nextSunday = 6;
					}else if(daysInMonths[monthNumber]%(DAYSINWEEK) == 3){
						nextSunday = 5;
					}else if(daysInMonths[monthNumber]%(DAYSINWEEK) == 4){
						nextSunday = 4;
					}else if(daysInMonths[monthNumber]%(DAYSINWEEK) == 5){
						nextSunday = 3;
					}else if(daysInMonths[monthNumber]%(DAYSINWEEK) == 6){
						nextSunday = 2;
					}
				}else{
					nextSunday = 0;
				}
			}
			System.out.printf("%d\n",counterFriday13th);
		}
	}
}