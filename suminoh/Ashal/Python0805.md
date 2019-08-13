# Python by ashal
## 복습
* 누산 - 반복, 상태 변경
* Factorial 
factorial = 1
for i in range(1,n)
    factorial = factorial * i
1. 초기값 지정
2. 코드를 반복 입력 = 누산
3. 계산 결과 출력<br>
 => 자주 결과를 확인하는 것이 좋음 / 그렇지 않으면 어디서 오류가 발생했는지 찾기 힘듬

## 과제
* 초기값 지정<br>
total_score = 0<br>
<br>
* 누산1<br>
scores = [80, 100, 70, 90, 40]<br>
total_score = scores[0] + ...<br>
print(total_score)<br>
<br>
* 누산 2<br>
scores = [80, 100, 70, 90, 40]<br>
total_score += scores[0]<br>
total_score += scores[1]<br>
total_score += scores[2]<br>
total_score += scores[3]<br>
total_score += scores[4]<br>
print(total_score)<br>
<br>
* 누산 3<br>
<pre><code>for i in range(0,5):<br>
----total_score += scores[i]<br>
print(total+score)</pre></code>
<br>
* 누산 4
<pre><code>for i in range(0, len(scores)):
    total_score += scores[i]
print(total_score)
</code></pre>

## 추상화 (Abstraction)
* 함수를 이용하여 추상화<br>
### factorial 함수 만들기
<pre><code>def factorial(n):  
    accumulator = 1  
    for x in range(1, n+1):  
        accumulator *= x  
    return accumulator
</code></pre>  
### 함수
반복으로 외우기
