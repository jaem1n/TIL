* 코드랩으로 기본 문법을 배운 후 해커랭크에 있는 문제를 풀어보며 익힘 
* SQL에서는 주석 달 때 # 대신 -- 를 사용해야 함
* 세미콜론(;)
    * 여기까지 실행한다고 범위를 나누어주는 것
    * 코드 끝에 한번만 붙임
    * 필수적일 때가 있고 아닐 때가 있음

```SQL
SELECT *  -- 모든 컬럼을 다 보겠다
FROM employees;
```

```SQL
SELECT *
FROM employees LIMIT 5;  -- 위에 5줄만 보겠다
```

```SQL
SELECT * 
FROM employees 

WHERE salary >= 7000  -- salary 값이 7000 넘는 행만 출력
WHERE salary BETWEEN 5000 AND 6000  -- salary 값이 5000과 6000 사이인 행만 출력
WHERE salary IN (5000,6000)  -- salary 값이 5000이거나 6000인 행 출력
```

```SQL
SELECT hire_date AS h  -- 출력값의 컬럼명이 h로 나옴
        , emp_name  -- hire_date와 emp_name 컬럼만 출력
FROM employees

WHERE salary >= 7000
AND hire_date >= '2005-01-01' 
```

```SQL
SELECT emp_name
FROM employees

WHERE emp_name LIKE 'E%' -- E로 시작하는 값
WHERE emp_name LIKE '%E' -- E로 끝나는 값
WHERE emp_name LIKE '%E%' -- E가 중간에 있는 값
```

```SQL
SELECT DISTINCT city
-- 중복 제거
FROM station

WHERE MOD(id,2)=0
-- id를 2로 나눴을 때 나머지가 0인 값
```

```SQL
SELECT count(city)- count(distinct city)
FROM station

-- 갯수 세기: count()
-- 중복 제외한 갯수 세기: count(distinct )
```

```SQL
SELECT DISTINCT st.city
FROM station AS st

WHERE (st.city NOT LIKE 'a%'
       AND st.city NOT LIKE 'e%')
OR (st.city NOT LIKE '%a' 
    AND st.city NOT LIKE '%e')
-- a와 e로 시작하거나 끝나지 않는 문자열을 가진 값만 출력
```