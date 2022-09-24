-- SQL project -  TFDS Course \
--*************************************\
-- Important: CAP4756 section students should only answer questions 1 to 4 \
-- Use your database\
use sbm26;
-- Code here:\
--Exercise 1
--1. Create a table in your database named Grade\
--2. Add variables: CourseID, Score, Semester\
create table Grade (
    Id int not null primary key identity(1,1),  -- primary key as a unique identifier for a record(row) in a table  --
	CourseId Varchar(40) not null, --A variable length string between 1 and 65535 characters in length which does not accept null--
	Score float, --score is a float
	Semester text -- semester with test variable
);
-- 3. Populate the table with fake data - at least 3 rows.\
--Using sql statement insert for adding new records to these tables
insert into Grade values('stat 5990', '98.95', 'fall 2022')

insert into Grade values('cap 5756', '94.95', 'summer 2022')

insert into Grade values('mat 5760', '90.95', 'spring 2022')

insert into Grade values('com 6162', '97.95', 'winter 2022')

-- Select everything from the table\
--Select statement to retrieve records from tables
select * from Grade;
--Drop the table 
drop table Grade;



--Use AdventureWorks database \
use AdventureWorks;
-- Exercise 2
--2. Write a query to list the SalesOrderID, SalesOrderDetailID, ProductID, 
--OrderQty from SalesOrderDetail table\

select SalesOrderID, SalesOrderDetailID, ProductID, OrderQty
from Sales.SalesOrderDetail;


--Exercise 3
--3. Write a query to list the SalesOrderID, TerritoryID from SalesOrderHeader 
--table.\

select SalesOrderID, TerritoryID
from Sales.SalesOrderHeader;



-- Exercise 4
--4. Write a query to list the name of the Product, ProductID, OrderQty \
-- and SalesOrderId by joining Product and SalesOrderDetail Tables\
select p.Name, p.ProductID, s.OrderQty, s.SalesOrderId
from production.Product as p
inner join sales.SalesOrderDetail as s on p.ProductID = s.ProductID;

--Exercise 5
--5. Write a query to list the name of the Product, ProductID, Total OrderQty by 
--ProductID\-- by joining Product and SalesOrderDetail Tables\

select p.Name, p.ProductID , sum(OrderQty) as SumTotal
from Production.Product as p
 inner join sales.SalesOrderDetail as s  on p.ProductID = s.ProductID
group by p.ProductID, p.Name

--Exercise 6
--6. Pick a SalesOrderID from SalesOrderDetail table and find the total OrderQty 
--and Average UnitPrice\

select SalesOrderID , sum(OrderQty) as TotalSum , avg(UnitPrice) as Average  
from sales.SalesOrderDetail
group by SalesOrderID

