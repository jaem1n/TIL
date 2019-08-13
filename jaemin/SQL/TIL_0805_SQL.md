# ORDER BY : 데이터 정렬

```SQL
SELECT *
FROM Customers
ORDER BY CustomerID  --오름차순으로 정렬 (ASC 써도 되고 안 써도 됨)
;

SELECT *
FROM Customers
ORDER BY CustomerID DESC  -- 내림차순으로 정렬
LIMIT 1  -- 위에서부터 n줄만 보여주기
;

SELECT name
FROM Customers
ORDER BY LEFT(name,3)
WHERE LEFT(name,3) = ’Sam’ -- Sam으로 시작하는 값 뽑아내기
;
```

ORDER BY 조건 2개 주기 
<br>: ORDER BY a,b (a로 먼저 정렬하고 a로도 안되면 b로 정렬)

WHERE문에는 AND나 OR을 사용할 수 있는 반면 ORDER BY에는 , 를 사용

<br>

# GROUP BY : 데이터 요약

GROUP BY 에 들어가는 컬럼은 SELECT 에 무조건 들어가야 한다!

HAVING : GROUP BY 한 후에 조건 주기

```SQL
-- 연습문제 2. Products 테이블을 참조해, 공급하는 물건들의 평균 가격이 비싼 Supplier 다섯 업체와 평균 가격을 출력하세요.

SELECT SupplierID, AVG(Price)
FROM Products
GROUP BY SupplierID
ORDER BY AVG(Price) DESC
LIMIT 5


-- 연습문제 3. Products 테이블을 참조해, 공급하는 물건들의 평균 가격이 40 이상인 업체와 평균 가격을 출력하세요.

SELECT SupplierID, AVG(Price)
FROM Products
GROUP BY SupplierID
HAVING AVG(Price) >= 40
```

<br>

# JOIN : 테이블 합쳐서 보기

### INNER JOIN : 양쪽에 데이터가 다 있는 행만 보여줌

```SQL
SELECT * 
FROM Orders AS o
    INNER JOIN Customers AS c ON o.CustomerID = c.CustomerID
    -- 두개의 테이블을 하나로 붙임 ON 공통컬럼
;


-- OrderID 10248번에는 몇 가지 종류의 상품이 들어있나요? 상품들의 총 갯수는 어떻게 되나요? Orders, OrderDetails 테이블을 이용해 알아보세요.

SELECT COUNT(ProductID), SUM(Quantity)  
-- 한쪽 테이블에만 있는 컬럼이므로 테이블 이름 안 써줘도 됨
FROM Orders AS o
	INNER JOIN OrderDetails AS od ON o.OrderID = od.OrderID
WHERE o.OrderID='10248' 
-- od.OrderID로 써도 같은 결과. 10248에 따옴표 안 해도 결과.
```

<br>

### LEFT JOIN : 왼쪽 기준으로 합쳐서 보여줌. 오른쪽 테이블에서 온 빈 값은 Null로 표시. (<-> RIGHT JOIN)

```SQL
-- 가입은 했지만 한 번도 주문을 하지 않은 고객이 또 있는지 어떻게 확인 할 수 있을까요?

SELECT c.CustomerID, CustomerName
FROM Customers as c
	LEFT JOIN Orders as o ON c.CustomerID = o.CustomerID
    -- left table: c / right table: o
WHERE OrderID is null
-- null 일 때는 = 대신 is 를 씀
```




