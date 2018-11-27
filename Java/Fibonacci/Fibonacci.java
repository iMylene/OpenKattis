//Name:			Mylene Martodihardjo
//Date:			1-11-2016
//Assignment:	Fibonacci Words

package Fibonacci;

import java.io.*;
import java.util.*;

public class Fibonacci {
	public static void main(String[] args) throws IOException {
        IO io = new IO(System.in);
        
        /* We know:
         * - A Fibonacci word can be created by
         * 		- replacing 0 by 1
         * 		- replacing 1 by 10
         * 
         * - Edge case:
         * 		- p = 111 (won't happen)
         * 		- p = 00 (won't happen)
         * 
         * - Fibonacci words: Dynamic Programming, recursive would be to slow
         * 
         */
        
        
        String line;
        while((line=io.next())!=null){
            System.out.println(line);
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