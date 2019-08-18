# LeetCode 문제풀이

## 596번
```SQL
SELECT class AS class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student)>=5
```

## 595번
```SQL
SELECT name, population, area
FROM World
WHERE area > 3000000 
OR population > 25000000
```

## 620번
```SQL
SELECT id, movie, description, rating
FROM cinema
WHERE MOD(ID,2)=1 
-- WHERE ID%2=1 로도 쓸 수 있음
AND NOT description = 'boring'
ORDER BY rating DESC
```

## 197번
```SQL
-- 방법1.
SELECT w2.Id AS Id
FROM Weather AS w1, -- w1: 어제 날짜
     Weather AS w2  -- w2: 오늘 날짜 (출력할 것)
WHERE w2.RecordDate = DATE_ADD(w1.RecordDate, INTERVAL 1 DAY)
-- WHERE DATEDIFF(w2.RecordDate, w1.RecordDate)=1 로도 쓸 수 있음 (w2 날짜와 w1 날짜 차이가 1일 때)
AND w2.Temperature > w1.Temperature

-- 방법2.
SELECT w2.Id
FROM Weather AS w2
     INNER JOIN Weather AS w1 ON w2.RecordDate = DATE_ADD(w1.RecordDate, INTERVAL 1 DAY)
WHERE w2.Temperature > w1.Temperature
```


