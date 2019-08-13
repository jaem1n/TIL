# Pandas by sunmi (0807)
library, 새로운 language, 범용 ,language  
## 라이브러리 설치
* import pandas as pd
* import numpy as np
* pandas, numpy -> colab에는 이미 설치되어 있음

## Pandas
* 데이터프레임(테이블) 만들기 ; pd.DataFrame
* .columns ; column이름만 보여줌
* pd.Series ; 
* df.head() ; 맨 위의 데이터만 보여줌 (default는 5, 다른 수도 설정 가능)
* df.tail() ; 맨 아래 데이터만 볼 수 있음
* df.values ; 
* df.discribe
* df.T ; 데이터 전치
* .sort_index(axis, ascending) ; 인덱스로 정렬 <br> -> axis = 0 인덱스 내림차순, axis = 1 인덱스 오름차순
* .sort_values(by = a) ; a칼럼으로 정렬 
* df['c'] ; df테이블에서 칼럼c만 출력 / 여러 개의 칼럼을 보고 싶을 때는 칼럼명을 리스트로 넣어줘야함
* pd.date_range('20190801', periods=7) ; 20190801부터 7일 간격으로 생성
* .index ; 인덱스를 바꿀 수 있음