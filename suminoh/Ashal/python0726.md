# PYTHON (ASHAL)
## PROGRAM
pro + gram = 이전 + 계획 (+단위)

### 컴퓨터 프로그램
* 컴퓨터가 순서대로 해야할 일을 적는 것 (+단위)
* 컴퓨터는 어떤 단위를 쓸 것인가?

## PYTHON
python을 사용하는 이유? 많이 써서...

* 표현식 : 입력한 것 ; 계산, 결과를 내는 것 ; 화면의 상태가 변화
* 명령문 : 실행하는 것 ; 값을 할당하는 것 = 이름붙이기 = assignment</br>ex) score = 10 
* 변수 ; ex) score은 변수, 10은 expression
* 연산자 : +, -, =, *, /, //, % ; 우선순위가 있음
* 함수 ; ex) print() 
* 데이터타입 : int(integer) = 정수, float = 실수, 
* Error ; 에러에 대한 설명을 많이 보는 것도 유익함
* 문자열 내에 "를 포함하고 싶을 때는 '' 안에 표현
* \ (escape 문자) : 특수한 문자를 처리해줌 </br> ex) "\"Hello, world\""
    "Hello, world"가 프린트 됨

### print('Hello, world')
* print는 명령, ''안의 글자는 인용한 글자
* print는 명령을 하는 함수로 ()로 표시해줌
* 문법 = 규칙 
* 파이썬의 문법을 알면 명령을 내릴 수 있고 </br> 명령을 모아 프로그램을 만들 수 있음


### 실습 예제 1
* 문자 + 숫자 => 에러
* 문자 * 숫자 => 문자 반복 ; 계산 X
* / 실수나눗셈 ; 결과가 항상 float형으로 출력
* // 정수나눗셈 ; 결과가 항상 int형으로 출력
* 1=1 ? False ; 변수명에는 숫자 불가능
* 1 < (2 and 1) < 2 </br> : 2 and 1의 결과 = 1 (논리연산 + Boolean 참고)

### Boolean + 논리연산자
* 숫자 0은 False, 나머지는 True </br> 공백은 False, 나머지는 True
* True and True 뒤 </br>True or True 앞 </br>

* True and False 뒤 </br>True or False 앞 </br>

* False and True 앞 </br>False or True 뒤 </br>

* False and False 앞 </br>False or False 뒤 </br>

### 실습 예제 2
* 프로그램은 순서대로 실행되기 때문에 새로운 할당 값을 주면 먼저 있던 할당값은 없어지고 새로운 값이 할당됨
* list1 = [0,1,2,3] : 리스트 선언; 여러개의 값을 다룸
* 리스트의 원소번호는 0부터 시작
* sum(list1) : list의 원소값을 모두 더해 줌
* len(list1) : list의 원소의 갯수
* list1[a:b] : list1[a]부터 list[b-1]까지의 원소만 추출</br>ex)list1[2:5] ; list1[2]부터 list1[4]번째 원소만 추출
* list1[a:] : list1[a]부터 마지막 원소까지 / 반대도 가능
* 원소번호를 마지막 원소를 기준으로 줄 수 있음 ; 마지막 원소 = -1, 그 후로 1씩 감소
* list1[::c] : c의 부호는 방향, c의 크기는 간격
