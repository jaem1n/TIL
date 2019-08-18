# HackerRank 문제풀이

## The Report
```SQL
-- 1번째 방법
SELECT 
    (CASE WHEN g.grade>7 THEN s.Name ELSE 'NULL' END), g.Grade, s.Marks 
    -- THEN 뒤에는 하나의 컬럼만 가능 (연산이 들어가는 컬럼도 가능) 
FROM Students AS s
    INNER JOIN Grades AS g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC, s.Name, s.Marks

-- 2번째 방법
SELECT
    IF(g.grade >=8, s.name, null), g.grade, s.marks
    -- IF(조건, TRUE일 때 출력값, FALSE일 때 출력값)
FROM Students AS s
    INNER JOIN Grades AS g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC, s.Name, s.Marks
```

## Symmetric Pairs
```SQL
-- 1번째 방법
SELECT f1.x, f1.y
FROM Functions as f1, Functions as f2
WHERE f1.x IN(f2.y) 
    AND f2.x IN(f1.y)
    AND f1.x < f1.y
    
UNION 

SELECT X, Y
FROM Functions
WHERE X=Y
GROUP BY X, Y
HAVING COUNT(X)>1 

ORDER BY X

-- 2번째 방법
SELECT F1.X, F1.Y
FROM Functions AS F1
   INNER JOIN Functions AS F2
WHERE F1.X IN(F2.Y) AND F1.Y IN (F2.X)
GROUP BY F1.X, F1.Y
HAVING COUNT(F1.X)>1 OR F1.X<F1.Y
ORDER BY F1.X
```