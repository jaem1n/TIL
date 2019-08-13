## GROUP BY 데이터 요약

* 연습문제 1
OrderDetails 테이블을 사용해, Order별로 몇 개의 상품을 주문했는지 보여주세요.
``` SQL
SELECT OrderID, 
SUM(Quantity) as SUMMATION
FROM OrderDetails
GROUP BY OrderID
;
```

* 연습문제 2
Products 테이블을 참조해, 공급하는 물건들의 평균 가격이 비싼 Supplier 다섯 업체와 평균 가격을 출력하세요.

``` SQL
SELECT SupplierID, AVG(Price)
FROM Products
GROUP BY SupplierID
ORDER BY AVG(Price) DESC
LIMIT 5
;
```

* 연습문제 3
Products 테이블을 참조해, 공급하는 물건들의 평균 가격이 40 이상인 업체와 평균 가격을 출력하세요.
``` SQL
SELECT SupplierID, AVG(Price)
FROM Products
GROUP BY SupplierID
ORDER BY AVG(Price) DESC
HAVING AVG(Price) > 40
;
```

# JOIN
## INNER JOIN
1. OrderID 10248번에는 몇 가지 종류의 상품이 들어있나요? 상품들의 총 갯수는 어떻게 되나요? Orders, OrderDetails 테이블을 이용해 알아보세요.
```SQL
SELECT O.OrderID, D.ProductID, D.Quantity
FROM Orders AS O
INNER JOIN OrderDetails AS D ON O.OrderID = D.OrderID
WHERE O.OrderID = 10248
;
```

2. OrderID 10249번에는 어떤 상품들이 들어있나요? 상품명을 출력하세요.
```SQL
SELECT D.OrderID, P.ProductID, P.ProductName
FROM OrderDetails AS D
INNER JOIN Products AS P ON D.ProductID = P.ProductID
WHERE D.OrderID = 10249
;
```

3. OrderID 10249번에 들어있는 상품들의 총 가격은 얼마인가요?
4. OrderID 10249번에 들어있는 상품명, 납품한 업체 이름, 업체가 소속된 국가를 모두 출력하세요.

## LEFT JOIN
1. 그렇다면, 가입은 했지만 한 번도 주문을 하지 않은 고객이 또 있는지 어떻게 확인 할 수 있을까요?
```SQL
SELECT C.CustomerID, C.CustomerName
FROM Customers AS C
LEFT JOIN Orders AS O ON C.CustomerID = O.CustomerID
WHERE O.CustomerID IS null
;
```

2. 가입은 했지만, 한 번도 주문을 하지 않은 고객은 총 몇 명인가요?
```SQL
SELECT COUNT(C.CustomerID)
FROM Customers AS C
LEFT JOIN Orders AS O ON C.CustomerID = O.CustomerID
WHERE O.CustomerID IS null
;
```

3. 주문을 한 번도 성사시키지 못 한 직원이 있나요?
```SQL
SELECT E.FirstName, E.LastName, E.Notes
FROM Employees AS E
LEFT JOIN Orders AS O ON E.EmployeeID = O.EmployeeID
WHERE O.OrderID is null
;
```
