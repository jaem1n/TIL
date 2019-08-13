# LEETCODE
## 197. Rising Temperature
```SQL
SELECT w2.id as Id
FROM weather as w1, weather as w2
WHERE w2.RecordDate = DATE_ADD(w1.RecordDate, INTERVAL 1 DAY)
AND w1.temperature < w2.temperature
;
```
