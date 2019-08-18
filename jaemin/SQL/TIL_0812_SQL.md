# LeetCode 문제풀이

## 180번
```SQL
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM `Logs` AS l1
    INNER JOIN `Logs` AS l2 ON l2.Id = l1.Id +1 and l2.Num = l1.Num
    INNER JOIN `Logs` AS l3 ON l3.Id = l1.Id +2 and l3.Num = l1.Num
```

## 184번
```SQL
SELECT df.Department AS Department, e.name AS Employee, e.salary as Salary
FROM (SELECT d.name AS Department, d.id AS ID, MAX(salary) AS Salary
      FROM employee AS e
        INNER JOIN department AS d on e.departmentid = d.id
      GROUP BY d.name) AS df
    INNER JOIN employee AS e ON e.departmentid = df.ID
WHERE e.salary = df.Salary
```

