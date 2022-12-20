import java.util.Scanner;

class HanSoo {
	public int getNum(int N) {
		int num = 0;
		
		for(int i =1; i<=N; i++) {
			//i의 각자리수가 등차수열을 이루면
			if(deungCha(i)) {
				num++;
			}
		}
		
		return num;
	}
	
	public boolean deungCha(int n) {

		if(n>=100 && n<1000) {
			int third = n/100;
			int second = (n - third*100)/10;
			int first = n - second*10- third*100;
			
			
			return (third-second == second-first);
		}
		
		else if(n==1000){
			return false;
		}
		else {
			return true;
		}
	}
}

class Main{
    public static void main(String[] args) {
       	HanSoo hansoo = new HanSoo();
		Scanner sc = new Scanner(System.in);
		
		
		System.out.println(hansoo.getNum(sc.nextInt()));

        
    }
}


