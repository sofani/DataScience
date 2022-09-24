-- SQL More 
-- Dr. Cohen - acohen@uwf.edu
-- This is a gentle introduction to SQL clauses
-- *****************************************************
-- This indicates to the server which database to use
USE AdventureWorks;
-- Pull info about user, server, and more
SELECT SUSER_NAME() as loginName,
USER_NAME() as userName,
GETDATE() as currentLocalTime,
@@SERVERNAME as serverName
-- SELECT --
SELECT *
FROM Production.Product;
-- How many Products?
SELECT count(*) as nbrProducts
FROM Production.Product;
-- Display the Product Categories
SELECT *
FROM Production.ProductCategory;
-- Display the Product SubCategories
SELECT *
FROM Production.ProductSubcategory;
-- Display Top n or Percentage
SELECT TOP 10 *
FROM Production.Product;
SELECT TOP 20 PERCENT *
FROM Production.Product;
-- Select the smallest or largest value of a column
SELECT MIN(p.Size) SmallestSize
FROM Production.Product p
WHERE SizeUnitMeasureCode = 'CM';
SELECT MAX(p.DaysToManufacture) as LongestManufactured
FROM Production.Product p;
SELECT DaysToManufacture
FROM Production.Product
WHERE MakeFlag = 0;
SELECT AVG(Cast(DaysToManufacture as float)) as AvgDaysToManufacture
FROM Production.Product
WHERE MakeFlag = 1;
-- WHERE --
-- Find the number of subcategory product where the categoryID is 2
SELECT count(*) as nbrSubCategoryPrdct
FROM Production.ProductSubcategory
WHERE ProductCategoryID =4;
-- Find the number of subcategory product where the categoryID is 2 or 3
SELECT * 
FROM Production.ProductSubcategory
WHERE ProductCategoryID = 2 OR ProductCategoryID = 3;
-- Display the number of subcategory product where the categoryID is not 2
SELECT *
FROM Production.ProductSubcategory
WHERE NOT ProductCategoryID = 2;
-- Look for NULL value
SELECT count(*)
FROM Production.Product
WHERE Color IS NULL;
-- Look for NOT NULL value
SELECT count(*)
FROM Production.Product
WHERE Color IS NOT NULL;
--- ORDER BY ---
-- Ascending order
SELECT *
FROM Production.Product
ORDER BY Name;
-- Descending order
SELECT *
FROM Production.Product
ORDER BY Name DESC;
-- Order by name then by product number
SELECT *
FROM Production.Product
ORDER BY ProductNumber, Name;
-- GROUP BY --
-- How many subcategories are per product category?
SELECT count(ProductSubcategoryID) nbrsubcat,ProductCategoryID
  FROM Production.ProductSubcategory 
  GROUP BY ProductCategoryID;
SELECT SalesOrderID, SUM(OrderQty) as NbrItemsOrdered, SUM(UnitPrice) as 
TotalAmountOrdered
FROM Sales.SalesOrderDetail
WHERE SalesOrderID=43659
GROUP BY SalesOrderID;
-- JOINS --
--INNER: returns records that have matching in both tables
--LEFT: returns all records from the left table, and matched records from the right table
--RIGHT: returns all records from the right table, and matched records from the  left table
--FULL: returns all records when there is a match in either left or right table
-- INNER 
SELECT count(*)
FROM Sales.SalesOrderDetail sod
INNER JOIN Production.Product p
ON sod.ProductID = p.ProductID;
-- LEFT 
SELECT count(*)
FROM Production.Product
LEFT JOIN Sales.SalesOrderDetail 
ON Sales.SalesOrderDetail.ProductID = Production.Product.ProductID;
-- RIGHT 
SELECT *
FROM Production.Product
RIGHT JOIN Sales.SalesOrderDetail 
ON Sales.SalesOrderDetail.ProductID = Production.Product.ProductID;
-- FULL 
SELECT count(*)
FROM Production.Product
FULL JOIN Sales.SalesOrderDetail 
ON Sales.SalesOrderDetail.ProductID = Production.Product.ProductID;
-- Subqueries
-- Are queries that are nested inside of another query or statement. 
-- Find the employees who have more vacation than the average
SELECT e.BusinessEntityID, e.LoginID, e.JobTitle, e.VacationHours
FROM HumanResources.Employee e
WHERE e.VacationHours > AVG(e.VacationHours); -- Error!!!!
--Solution
SELECT e.BusinessEntityID, e.LoginID, e.JobTitle, e.VacationHours
FROM HumanResources.Employee e
WHERE e.VacationHours > (SELECT
    AVG(VacationHours)
    FROM HumanResources.Employee)
-- Make more sense to pull the employees who have more vacation than the average of their Job Title
SELECT e.JobTitle, e.VacationHours
FROM HumanResources.Employee e
INNER JOIN (
    SELECT JobTitle, AVG(VacationHours) as avghourTitlejob
    FROM HumanResources.Employee 
    GROUP BY JobTitle) as subq
     on e.JobTitle = subq.JobTitle
     WHERE e.VacationHours > subq.avghourTitlejob;


