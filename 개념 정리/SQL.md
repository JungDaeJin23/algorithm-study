# SQL
## w3Schools
https://www.w3schools.com/mysql/exercise.asp?filename=exercise_select1

<>는 다르다를 의미한다. != ex) where A <> B
### 틀린 문제
[Select3](https://www.w3schools.com/mysql/exercise.asp?filename=exercise_select3)
Select all the different values from the Country column in the Customers table.
solution
The SELECT DISTINCT statement is used to return only distinct (different) values.
Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

[Where2 & NOT](https://www.w3schools.com/mysql/exercise.asp?filename=exercise_where2)
NOT 사용법

[Insert1](https://www.w3schools.com/mysql/exercise.asp?filename=exercise_insert1)
Insert Data Only in Specified Columns. 명시안된 column에는 null이 채워진다.

[Update1](https://www.w3schools.com/mysql/exercise.asp?filename=exercise_update1)
update  set 

set뒤에 여러 데이터는 ,로 구분 

[function average](https://www.w3schools.com/mysql/exercise.asp?filename=exercise_functions4)
문제 잘 읽기

[Like](https://www.w3schools.com/mysql/exercise.asp?filename=exercise_like1)
패턴 공부
There are two wildcards often used in conjunction with the LIKE operator:

The percent sign (%) represents zero, one, or multiple characters
The underscore sign (_) represents one, single character

LIKE Operator	Description
WHERE CustomerName LIKE 'a%'	Finds any values that start with "a"
WHERE CustomerName LIKE '%a'	Finds any values that end with "a"
WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position
WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position
WHERE CustomerName LIKE 'a_%'	Finds any values that start with "a" and are at least 2 characters in length
WHERE CustomerName LIKE 'a__%'	Finds any values that start with "a" and are at least 3 characters in length
WHERE ContactName LIKE 'a%o'	Finds any values that start with "a" and ends with "o"


alias: 별명
Aliases are used to give a table, or a column in a table, a temporary name.

Aliases are often used to make column names more readable.

An alias only exists for the duration of that query.

An alias is created with the AS keyword.


[JOIN](https://www.w3schools.com/mysql/mysql_join.asp)
SELECT *
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

[JOIN2](https://www.w3schools.com/mysql/exercise.asp?filename=exercise_join2)
Choose the correct JOIN clause to select all records from the two tables where there is a match in both tables.
양쪽 테이블 모두에서 만족하는 => 해석 실수. 

[JOIN3](https://www.w3schools.com/mysql/exercise.asp?filename=exercise_join3)
Choose the correct JOIN clause to select all the records from the Customers table plus all the matches in the Orders table.
-> order 테이블 안에서, 커스토머 테이블은 plus all the matches(전부)

Group BY 다음 조건에 맞게 그룹 지어라

The MySQL HAVING Clause
The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.
HAVING Syntax
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);


### 미학습
Self Join
UNION
Having 이후로 쭉 DB까지


## Programmers
https://programmers.co.kr/learn/challenges?tab=sql_practice_kit

