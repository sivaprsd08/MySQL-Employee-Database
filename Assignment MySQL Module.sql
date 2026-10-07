--  E-COMMERCE CUSTOMER CHURN ANALYSIS
--  ==================================

--   PART 1: DATABASE 
--   ================

USE ecomm;

-- To View records
SELECT *
FROM customer_churn
LIMIT 10;

-- To Count customers
SELECT COUNT(*) AS total_customers
FROM customer_churn;

-- To View table 
DESCRIBE customer_churn;

-- PART 2: IDENTIFY MISSING VALUES
--  ===============================

SELECT
    COUNT(*) - COUNT(WarehouseToHome) AS WarehouseToHome_NULL,
    COUNT(*) - COUNT(HourSpendOnApp) AS HourSpendOnApp_NULL,
    COUNT(*) - COUNT(OrderAmountHikeFromlastYear) AS OrderAmountHike_NULL,
    COUNT(*) - COUNT(DaySinceLastOrder) AS DaySinceLastOrder_NULL,
    COUNT(*) - COUNT(Tenure) AS Tenure_NULL,
    COUNT(*) - COUNT(CouponUsed) AS CouponUsed_NULL,
    COUNT(*) - COUNT(OrderCount) AS OrderCount_NULL
FROM customer_churn;

--   PART 3: CALCULATE MEANS FOR NUMERIC MISSING VALUES
--   ===================================================

SELECT
    AVG(WarehouseToHome) AS avg_WarehouseToHome,
    AVG(HourSpendOnApp) AS avg_HourSpendOnApp,
    AVG(OrderAmountHikeFromlastYear) AS avg_OrderAmountHike,
    AVG(DaySinceLastOrder) AS avg_DaySinceLastOrder
FROM customer_churn;

--   PART 4: HANDLE MISSING VALUES USING MEAN
--   ========================================

SET SQL_SAFE_UPDATES = 0;

-- WarehouseToHome
UPDATE customer_churn
SET WarehouseToHome = (
    SELECT ROUND(AVG(WarehouseToHome))
    FROM (
        SELECT WarehouseToHome
        FROM customer_churn
        WHERE WarehouseToHome IS NOT NULL
    ) AS temp
)
WHERE WarehouseToHome IS NULL;

-- HourSpendOnApp
UPDATE customer_churn
SET HourSpendOnApp = (
    SELECT ROUND(AVG(HourSpendOnApp))
    FROM (
        SELECT HourSpendOnApp
        FROM customer_churn
        WHERE HourSpendOnApp IS NOT NULL
    ) AS temp
)
WHERE HourSpendOnApp IS NULL;

-- OrderAmountHikeFromlastYear
UPDATE customer_churn
SET OrderAmountHikeFromlastYear = (
    SELECT ROUND(AVG(OrderAmountHikeFromlastYear))
    FROM (
        SELECT OrderAmountHikeFromlastYear
        FROM customer_churn
        WHERE OrderAmountHikeFromlastYear IS NOT NULL
    ) AS temp
)
WHERE OrderAmountHikeFromlastYear IS NULL;

-- DaySinceLastOrder
UPDATE customer_churn
SET DaySinceLastOrder = (
    SELECT ROUND(AVG(DaySinceLastOrder))
    FROM (
        SELECT DaySinceLastOrder
        FROM customer_churn
        WHERE DaySinceLastOrder IS NOT NULL
    ) AS temp
)
WHERE DaySinceLastOrder IS NULL;

-- Verify

SELECT
    COUNT(*) - COUNT(WarehouseToHome) AS WTH_NULL,
    COUNT(*) - COUNT(HourSpendOnApp) AS APP_NULL,
    COUNT(*) - COUNT(OrderAmountHikeFromlastYear) AS HIKE_NULL,
    COUNT(*) - COUNT(DaySinceLastOrder) AS LASTORDER_NULL
FROM customer_churn;

--   PART 5: FIND MODE VALUES
--   =======================

-- Mode of Tenure
SELECT
    Tenure,
    COUNT(*) AS frequency
FROM customer_churn
WHERE Tenure IS NOT NULL
GROUP BY Tenure
ORDER BY frequency DESC
LIMIT 1;

-- Mode of CouponUsed
SELECT
    CouponUsed,
    COUNT(*) AS frequency
FROM customer_churn
WHERE CouponUsed IS NOT NULL
GROUP BY CouponUsed
ORDER BY frequency DESC
LIMIT 1;

-- Mode of OrderCount
SELECT
    OrderCount,
    COUNT(*) AS frequency
FROM customer_churn
WHERE OrderCount IS NOT NULL
GROUP BY OrderCount
ORDER BY frequency DESC
LIMIT 1;

--   PART 6: HANDLE MISSING VALUES USING MODE
--   ========================================

UPDATE customer_churn
SET Tenure = 1
WHERE Tenure IS NULL;

UPDATE customer_churn
SET CouponUsed = 1
WHERE CouponUsed IS NULL;

UPDATE customer_churn
SET OrderCount = 2
WHERE OrderCount IS NULL;

-- Verify

SELECT
    COUNT(*) - COUNT(Tenure) AS Tenure_NULL,
    COUNT(*) - COUNT(CouponUsed) AS Coupon_NULL,
    COUNT(*) - COUNT(OrderCount) AS Order_NULL
FROM customer_churn;

--   PART 7: OUTLIER REMOVAL
--   =======================

-- Identify WarehouseToHome outliers
SELECT *
FROM customer_churn
WHERE WarehouseToHome > 100;

-- Delete outliers
DELETE FROM customer_churn
WHERE WarehouseToHome > 100;

-- Verify customer count after outlier removal
SELECT COUNT(*) AS total_customers
FROM customer_churn;

--   PART 8: STANDARDIZE CATEGORICAL VALUES
--   =======================================

-- Standardize PreferredLoginDevice
UPDATE customer_churn
SET PreferredLoginDevice = 'Mobile Phone'
WHERE PreferredLoginDevice = 'Phone';

-- Standardize PreferredOrderCat
UPDATE customer_churn
SET PreferedOrderCat = 'Mobile Phone'
WHERE PreferedOrderCat = 'Mobile';

-- Standardize PreferredPaymentMode
UPDATE customer_churn
SET PreferredPaymentMode = 'Cash on Delivery'
WHERE PreferredPaymentMode = 'COD';

UPDATE customer_churn
SET PreferredPaymentMode = 'Credit Card'
WHERE PreferredPaymentMode = 'CC';

-- Verify

SELECT
    PreferredPaymentMode,
    COUNT(*) AS count
FROM customer_churn
GROUP BY PreferredPaymentMode;

--   PART 9: RENAME COLUMNS
--   ========================

ALTER TABLE customer_churn
RENAME COLUMN PreferedOrderCat TO PreferredOrderCat;

ALTER TABLE customer_churn
RENAME COLUMN HourSpendOnApp TO HoursSpentOnApp;

--   PART 10: CREATE COMPLAINT STATUS
--   ================================

ALTER TABLE customer_churn
ADD COLUMN ComplaintReceived VARCHAR(3);

UPDATE customer_churn
SET ComplaintReceived =
    CASE
        WHEN Complain = 1 THEN 'Yes'
        ELSE 'No'
    END;

-- Verify

SELECT
    Complain,
    ComplaintReceived,
    COUNT(*) AS count
FROM customer_churn
GROUP BY Complain, ComplaintReceived;

--   PART 11: CREATE CHURN STATUS
--   ==============================

ALTER TABLE customer_churn
ADD COLUMN ChurnStatus VARCHAR(10);

UPDATE customer_churn
SET ChurnStatus =
    CASE
        WHEN Churn = 1 THEN 'Churned'
        ELSE 'Active'
    END;

-- Verify

SELECT
    Churn,
    ChurnStatus,
    COUNT(*) AS count
FROM customer_churn
GROUP BY Churn, ChurnStatus;

-- PART 12: DROP ORIGINAL COLUMNS
--   ==============================

ALTER TABLE customer_churn
DROP COLUMN Churn,
DROP COLUMN Complain;

--   PART 13: CUSTOMER CHURN ANALYSIS
--   ==================================

-- Q1. Count of active and churned customers 

SELECT
    ChurnStatus,
    COUNT(*) AS CustomerCount
FROM customer_churn
GROUP BY ChurnStatus;


-- Q2. Average tenure and total cashback of churned customers 

SELECT
    ROUND(AVG(Tenure), 2) AS AverageTenure,
    SUM(CashbackAmount) AS TotalCashback
FROM customer_churn
WHERE ChurnStatus = 'Churned';

-- Q3. Percentage of churned customers who complained 

SELECT
    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN ComplaintReceived = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS ComplaintPercentage
FROM customer_churn
WHERE ChurnStatus = 'Churned';

-- Q4. City tier with highest churned Laptop & Accessory customers 

SELECT
    CityTier,
    COUNT(*) AS CustomerCount
FROM customer_churn
WHERE ChurnStatus = 'Churned'
  AND PreferredOrderCat = 'Laptop & Accessory'
GROUP BY CityTier
ORDER BY CustomerCount DESC
LIMIT 1;

-- Q5. Most preferred payment mode among active customers 

SELECT
    PreferredPaymentMode,
    COUNT(*) AS CustomerCount
FROM customer_churn
WHERE ChurnStatus = 'Active'
GROUP BY PreferredPaymentMode
ORDER BY CustomerCount DESC
LIMIT 1;

-- Q6. Total order amount hike for single customers preferring Mobile Phone 

SELECT
    SUM(OrderAmountHikeFromlastYear) AS TotalOrderAmountHike
FROM customer_churn
WHERE MaritalStatus = 'Single'
  AND PreferredOrderCat = 'Mobile Phone';

-- Q7. Average number of devices registered by UPI users 

SELECT
    ROUND(AVG(NumberOfDeviceRegistered), 2) AS AverageDevices
FROM customer_churn
WHERE PreferredPaymentMode = 'UPI';

-- Q8. City tier with the highest number of customers 

SELECT
    CityTier,
    COUNT(*) AS CustomerCount
FROM customer_churn
GROUP BY CityTier
ORDER BY CustomerCount DESC
LIMIT 1;

-- Q9. Gender with the highest total coupon usage 

SELECT
    Gender,
    SUM(CouponUsed) AS TotalCoupons
FROM customer_churn
GROUP BY Gender
ORDER BY TotalCoupons DESC
LIMIT 1;

-- Q10. Customer count and maximum app usage by preferred order category 

SELECT
    PreferredOrderCat,
    COUNT(*) AS CustomerCount,
    MAX(HoursSpentOnApp) AS MaxHoursSpent
FROM customer_churn
GROUP BY PreferredOrderCat;

-- Q11. Total orders placed by Credit Card users having maximum satisfaction score 

SELECT
    SUM(OrderCount) AS TotalOrderCount
FROM customer_churn
WHERE PreferredPaymentMode = 'Credit Card'
  AND SatisfactionScore = (
      SELECT MAX(SatisfactionScore)
      FROM customer_churn
  );

-- Q12. Average satisfaction score of customers who received complaints 

SELECT
    ROUND(AVG(SatisfactionScore), 2) AS AverageSatisfaction
FROM customer_churn
WHERE ComplaintReceived = 'Yes';

-- Q13. Count of customers using more than 5 coupons, grouped by preferred order category 

SELECT
    PreferredOrderCat,
    COUNT(*) AS CustomerCount
FROM customer_churn
WHERE CouponUsed > 5
GROUP BY PreferredOrderCat
ORDER BY CustomerCount DESC;

-- Q14. Top 3 preferred order categories based on average cashback 

SELECT
    PreferredOrderCat,
    ROUND(AVG(CashbackAmount), 2) AS AverageCashback
FROM customer_churn
GROUP BY PreferredOrderCat
ORDER BY AverageCashback DESC
LIMIT 3;

-- Q15. Payment modes with average tenure approximately 10 months and more than 500 total orders

SELECT
    PreferredPaymentMode,
    ROUND(AVG(Tenure), 2) AS AverageTenure,
    SUM(OrderCount) AS TotalOrders
FROM customer_churn
GROUP BY PreferredPaymentMode
HAVING ROUND(AVG(Tenure)) = 10
   AND SUM(OrderCount) > 500;

-- Q16. Categorize customers based on warehouse distance and compare churn status

SELECT
    CASE
        WHEN WarehouseToHome <= 5
            THEN 'Very Close Distance'
        WHEN WarehouseToHome <= 10
            THEN 'Close Distance'
        WHEN WarehouseToHome <= 15
            THEN 'Moderate Distance'
        ELSE 'Far Distance'
    END AS DistanceCategory,
    ChurnStatus,
    COUNT(*) AS CustomerCount
FROM customer_churn
GROUP BY DistanceCategory, ChurnStatus;

-- Q17. Married customers from CityTier 1 with order count above average

SELECT *
FROM customer_churn
WHERE MaritalStatus = 'Married'
  AND CityTier = 1
  AND OrderCount > (
      SELECT AVG(OrderCount)
      FROM customer_churn
  );

-- PART 14: CUSTOMER RETURNS TABLE
--   ===============================

CREATE TABLE customer_returns (
    ReturnID INT PRIMARY KEY,
    CustomerID INT,
    ReturnDate DATE,
    RefundAmount INT
);

-- Insert return records

INSERT INTO customer_returns
(
    ReturnID,
    CustomerID,
    ReturnDate,
    RefundAmount
)
VALUES
(1001, 50022, '2023-01-01', 2130),
(1002, 50316, '2023-01-23', 2000),
(1003, 51099, '2023-02-14', 2290),
(1004, 52321, '2023-03-08', 2510),
(1005, 52928, '2023-03-20', 3000),
(1006, 53749, '2023-04-17', 1740),
(1007, 54206, '2023-04-21', 3250),
(1008, 54838, '2023-04-30', 1990);

-- View return records

SELECT *
FROM customer_returns;

--   PART 15: JOIN CUSTOMER RETURNS WITH CUSTOMER CHURN DATA
--   ======================================================

SELECT
    r.ReturnID,
    r.CustomerID,
    r.ReturnDate,
    r.RefundAmount,

    c.Tenure,
    c.PreferredLoginDevice,
    c.CityTier,
    c.WarehouseToHome,
    c.PreferredPaymentMode,
    c.Gender,
    c.HoursSpentOnApp,
    c.NumberOfDeviceRegistered,
    c.PreferredOrderCat,
    c.SatisfactionScore,
    c.MaritalStatus,
    c.NumberOfAddress,
    c.OrderAmountHikeFromlastYear,
    c.CouponUsed,
    c.OrderCount,
    c.DaySinceLastOrder,
    c.CashbackAmount,
    c.ComplaintReceived,
    c.ChurnStatus

FROM customer_returns AS r
INNER JOIN customer_churn AS c
    ON r.CustomerID = c.CustomerID
WHERE c.ChurnStatus = 'Churned'
  AND c.ComplaintReceived = 'Yes';

-- END