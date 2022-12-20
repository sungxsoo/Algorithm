import java.util.Scanner;

class Factorial {
	public int factorial(int n) {
		if(n==0) {
			return 1;
		}
		else {
		
		if(n==1) {
			return 1;
		}
		return n*factorial(n-1);
	
		}
    }
}

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		Factorial fc = new Factorial();
		
		System.out.println(fc.factorial(sc.nextInt()));
	
	}
}


