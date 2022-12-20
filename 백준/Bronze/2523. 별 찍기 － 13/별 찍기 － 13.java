import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M =2*N-1;
		for(int j=1;j<=M;j++) {
			for(int i= 1; i<=N-Math.abs(N-j);i++) {
				System.out.print("*");
			}
			System.out.println("");
		}

	}

}
