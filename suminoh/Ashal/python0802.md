# Python by ashal
## 1. 파이썬 인스톨
chocolatey ; window package manager
* IDE(Integrated Development Environment)
* PyCharm ; 무료버전 ; chocolatey이용 choco install pycharm-community 

Accumulation ; 누산
Acuumulator ; 누산기
계속 계산해서 최종 상태만 가지고 가는 것; 연산을 하면 상태가 바뀜

상태(state), 상태 변경(State Transition)  
Age = 13  
Age = 14 ; 의미를 갱신 / 상태를 바꿈  
다시 이름 붙이는 것 = 상태를 바꾸는 행위  
age = age + 1  
new_age = age + 1 / age = new_age / age = age + 1  
age += 1 (-=, *=, /=, %= )

factorial = 1 * 2 * 3 ... * n  
factorial = 1 / factorial *= 1 / factorial *= 2 / ... / factorial *= n  
초기값 ; factorial = 1  
누산 ; x는 1부터 n까지 Factorial *= x  
-> for x in range(1, n+1)  
factorial *= x  
-> for loop
(for반복 / in 반복횟수 / range 범위)

시작 <= X < 끝

Tab ; 공백4개 맞춰줘야 함 ; 들여쓰기 ; indent..?
<pre><code>n = 10000  
  f = 1  
  
  for i in range(1, n+1)  
    f*=i  
    print(f)
</pre></code>