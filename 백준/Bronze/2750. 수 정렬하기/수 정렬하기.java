import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int[] numList = new int[N];
		
		for(int i =0; i<N; i++) {
			numList[i] = sc.nextInt();
		}
		
		find(numList, N);
	}
	
	public static void find(int[] numList, int N) {
		for(int i=0; i<N-1; i++) {
			for(int j = i+1; j<N; j++) {
				if(numList[i] > numList[j]) {
					int temp;
					temp = numList[i];
					numList[i] = numList[j];
					numList[j] = temp;
				}
			}
		}
		
		for(int i =0; i<N; i++) {
			System.out.println(numList[i]);
		}
	}
	
	public static void swap(int a, int b) {
		
	}
}

