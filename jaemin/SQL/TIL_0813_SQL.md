# HackerRank 문제풀이

## Type of Triangle
```SQL
-- 1번째 방법
SELECT
    CASE
        WHEN (A+B)<=C OR (A+C)<=B OR (B+C)<=A THEN 'Not A Triangle'
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN A=B OR A=C OR B=C THEN 'Isosceles'
        ELSE 'Scalene'
    END
FROM triangles

-- CASE에서 A,B,C에 들어갈 수 있는 값에 제한이 큰 순서로 씀
-- Not A Triangle과 Equilatera의 조건은 서로 필요충분조건(?)이기 때문에 순서 바뀌어도 됨
-- Isosceles은 Equilateral의 의미도 포함하고 있으므로(정사각형의 경우) Equilateral보다 뒤에 써야함

-- 2번째 방법
SELECT
CASE
  WHEN A+B>C AND B+C>A AND A+C>B THEN
      CASE
          WHEN A=B AND B=C THEN 'Equilateral'
          WHEN A=B or A=C OR B=C THEN 'Isosceles'
          ELSE 'Scalene'
      END
  ELSE 'Not A Triangle'
END
FROM TRIANGLES
```

## Top Earners
```SQL
-- 1번째 방법
SELECT months * salary, COUNT(employee_id)
    FROM employee
    WHERE months * salary = (SELECT MAX(months * salary) FROM employee)
    GROUP BY months * salary

--2번째 방법
SELECT MAX(months * salary), COUNT(employee_id)
    FROM employee
    WHERE months * salary = (SELECT MAX(months * salary) FROM employee)
```