SELECT문 함수
* 개수: COUNT()
* 합계: SUM()
* 평균: AVG()
* 최대값: MAX()
* 최소값: MIN()
* 소수점 반올림: ROUND(SUM(LAT_N),2) -> LAT_N의 합계 값을 소수점 세번째 자리에서 반올림해서 소수점 두자리로 만들어라

```SQL
SELECT round(sum(lat_n),2) as lat, round(sum(long_w),2) as lon
FROM station
```
