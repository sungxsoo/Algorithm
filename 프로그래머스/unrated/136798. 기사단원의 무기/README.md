# [unrated] 기사단원의 무기 - 136798 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/136798) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.62 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>숫자나라 기사단의 각 기사에게는 1번부터 <code>number</code>까지 번호가 지정되어 있습니다. 기사들은 무기점에서 무기를 구매하려고 합니다.</p>

<p>각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 합니다. 단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 합니다.</p>

<p>예를 들어, 15번으로 지정된 기사단원은 15의 약수가 1, 3, 5, 15로 4개 이므로, 공격력이 4인 무기를 구매합니다. 만약, 이웃나라와의 협약으로 정해진 공격력의 제한수치가 3이고 제한수치를 초과한 기사가 사용할 무기의 공격력이 2라면, 15번으로 지정된 기사단원은 무기점에서 공격력이 2인 무기를 구매합니다. 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요합니다. 그래서 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게를 미리 계산하려 합니다.</p>

<p>기사단원의 수를 나타내는 정수 <code>number</code>와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 <code>limit</code>와 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 <code>power</code>가 주어졌을 때, 무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>number</code> ≤ 100,000</li>
<li>2 ≤ <code>limit</code> ≤ 100</li>
<li>1 ≤ <code>power</code> ≤ <code>limit</code></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>number</th>
<th>limit</th>
<th>power</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>5</td>
<td>3</td>
<td>2</td>
<td>10</td>
</tr>
<tr>
<td>10</td>
<td>3</td>
<td>2</td>
<td>21</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>1부터 5까지의 약수의 개수는 순서대로 [1, 2, 2, 3, 2]개입니다. 모두 공격력 제한 수치인 3을 넘지 않기 때문에 필요한 철의 무게는 해당 수들의 합인 10이 됩니다. 따라서 10을 return 합니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>1부터 10까지의 약수의 개수는 순서대로 [1, 2, 2, 3, 2, 4, 2, 4, 3, 4]개입니다. 공격력의 제한수치가 3이기 때문에, 6, 8, 10번 기사는 공격력이 2인 무기를 구매합니다. 따라서 해당 수들의 합인 21을 return 합니다.</p>

<hr>

### 어떤 수의 약수 개수 구하기

**1. 기초적인 반복문 사용**

	def solution(n):
	    cnt = 0
	    for i in range(1, n+1):
		if n % i == 0:
		       cnt += 1 

	    return cnt


**2. n/2 원리 사용**

	def solution(n):
	    factor_array = []
	    for i in range(1, n/2+1):
		if n % i == 0:
		       cnt += 1 

	   return cnt
	   
> 어떤 수 n의 절반 (n/2) 이상 에서는 n의 약수가 존재하지 않기 때문에 알고리즘 개선 가능


**3. 제곱근 사용**
				
	def solution(n):
	    factor_array = []
	    for i in range(1, int(n**(1/2))+1):
		if n % i == 0:
		      //제곱근일 때
		      if i == n//i:
			cnt += 1
		      //제곱근이 아닐 때
		      else:
			cnt += 2
	    return cnt
 
> for문을 어떤 수 n의 제곱근까지만 반복한다. 해당 수의 제곱근 이상 반복하는 것은 의미가 없다.


<hr>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
