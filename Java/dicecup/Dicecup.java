//Name:			Mylene Martodihardjo
//Date:			2-11-2016
//Assignment:	Dice Cup

package Dicecup;

import java.io.*;
import java.util.*;

public class Dicecup {
	public static void main(String[] args) throws IOException {
    IO io = new IO(System.in);
    
    int x = io.nextInt();
    int y = io.nextInt();
        
    if(x == y){
    	System.out.println(x+1);
    }else if(x < y){
    	for(int i = x+1; i<y+2; i++){
    		System.out.println(i);
    	}
    }else{
    	for(int i = y+1; i<x+2; i++){
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