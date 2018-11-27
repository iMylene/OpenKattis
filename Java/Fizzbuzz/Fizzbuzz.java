//Name:			Mylene Martodihardjo
//Date:			2-11-2016
//Assignment:	Fizzbuzz

package Fizzbuzz;

import java.io.*;
import java.util.*;

public class Fizzbuzz {
	public static void main(String[] args) throws IOException {
      IO io = new IO(System.in);
      
      int x = io.nextInt();
      int y = io.nextInt();
      int n = io.nextInt();
      
      for(int i = 1; i<n+1; i++){
    	  if(i%x == 0 && i%y == 0){
    		  System.out.println("FizzBuzz");
    	  }else if(i%x == 0){
    		  System.out.println("Fizz");
    	  }else if(i%y == 0){
    		  System.out.println("Buzz");
    	  }else{
    		  System.out.println(i);
    	  }
      }
      
      io.close();
	}
		
	static class IO extends PrintWriter {
		static BufferedReader r;
      static StringTokenizer t;
      
      public IO(InputStream i) {
          super(new BufferedOutputStream(System.out));
          r = new BufferedReader(new InputStreamReader(i));
          t = new StringTokenizer("");
      }
      
      public String next() throws IOException {
          while (!t.hasMoreTokens()) {
              t = new StringTokenizer(r.readLine());
          }
          return t.nextToken();
      }
      
      public int nextInt() throws IOException{
          return Integer.parseInt(next());
      }
      
      public long nextLong() throws IOException {
          return Long.parseLong(next());
      }
      
      public double nextDouble() throws IOException {
          return Double.parseDouble(next());
      }
	}
}