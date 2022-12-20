import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N =sc.nextInt();
		int score[] = new int[N];
		int M = score[0];
		float newScore[] = new float[N];
		float total=0;
		float avg;
		//점수입력
		for(int i =0; i<N; i++) {
			score[i] = sc.nextInt();		
		}	
		//최대값 M에 입력
		for(int i =0; i<N; i++) {
			if(score[i]>M) {
				M = score[i];
		}}
		//점수 재정의 (조작한 점수)
		for(int i =0; i<N; i++) {
			newScore[i] =(float)score[i]/M*100;
		}
		//total 넣기
		for(int i =0; i<N; i++) {
			total = total + newScore[i];
		}
		avg = total/N;
		System.out.println(avg);
		
		
	}}