import java.util.Scanner;

class BlackJack {
	
	public int findJack(int[] numList, int N, int M) {
		int result = 0;
		
		for(int i =0; i<N-2; i++) {
			for(int j=i+1; j<N-1; j++) {
				for(int k=j+1; k<N; k++) {
					int sum = numList[i] + numList[j] + numList[k];
					if(sum<=M&&sum>result) {
						result = sum;
					}
				}
			}
		}
		
		return result;
		
	}
}
class Main{
	public static void main(String[] args) {
		
		BlackJack bj =new BlackJack();
		
		Scanner sc= new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int[] numList = new int[N];
		
		for(int i =0; i<N; i++) {
			numList[i] = sc.nextInt();
		}
		
		int result = bj.findJack(numList, N, M);
		System.out.println(result);
	}
	
	
}
	
