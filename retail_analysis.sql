CREATE DATABASE retail_analysis;
USE retail_analysis;
CREATE TABLE retail (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate VARCHAR(50),
    UnitPrice DOUBLE,
    CustomerID VARCHAR(20),
    Country VARCHAR(100),
    Revenue DOUBLE,
    Month VARCHAR(20),
    Day VARCHAR(20)
);
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cleaned_retail.csv'
INTO TABLE retail
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(InvoiceNo, StockCode, Description, Quantity, InvoiceDate,
 UnitPrice, CustomerID, Country, Revenue, Month, Day);
 SELECT COUNT(*) FROM retail;
 SELECT
    Month,
    ROUND(SUM(Revenue),2) AS Total_Revenue
FROM retail
GROUP BY Month
ORDER BY Total_Revenue DESC;
SELECT
    Description,
    ROUND(SUM(Revenue),2) AS Revenue
FROM retail
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10;
SELECT
    Country,
    ROUND(SUM(Revenue),2) AS Revenue
FROM retail
GROUP BY Country
ORDER BY Revenue DESC;
SELECT
    CustomerID,
    ROUND(SUM(Revenue),2) AS Total_Spent
FROM retail
WHERE CustomerID <> ''
GROUP BY CustomerID
ORDER BY Total_Spent DESC
LIMIT 10;
SELECT
    Description,
    ROUND(SUM(Revenue),2) AS Revenue,
    RANK() OVER (
        ORDER BY SUM(Revenue) DESC
    ) AS Product_Rank
FROM retail
GROUP BY Description;