# LeetCode 문제풀이

## 175번 
```SQL
SELECT FirstName, LastName, City, State
FROM Person AS p
    LEFT JOIN Address AS a ON p.PersonId = a.PersonId
```

## 181번
```SQL
SELECT e1.Name AS Employee
FROM Employee AS e1
    LEFT JOIN Employee AS e2 ON e1.ManagerID = e2.ID
WHERE e1.Salary > e2.Salary
```

## 182번
```SQL
SELECT Email AS Email
FROM Person
GROUP BY Email
HAVING COUNT(Id)>=2
```

## 183번
```SQL
SELECT c.Name AS Customers 
FROM Customers as c
    LEFT JOIN Orders as o ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL
```