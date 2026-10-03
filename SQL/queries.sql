-- ==============================================================================
-- UNIT 4 & EXP 11: COMPLEX JOINS, AGGREGATIONS & SUBQUERIES[cite: 8, 12, 13]
-- ==============================================================================

-- 1. Display customers and total amount spent, sorted descending (Group By / Order By)
SELECT c.first_name, c.last_name, SUM(o.total_amount) as lifetime_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY lifetime_spent DESC;

-- 2. Nested Subquery: Find the product(s) with the highest price
SELECT name, price 
FROM Products 
WHERE price = (SELECT MAX(price) FROM Products);

-- ==============================================================================
-- UNIT 4: VIEWS & DATA INDEPENDENCE[cite: 8]
-- ==============================================================================

-- Create a View for security/data hiding (hides sensitive customer emails/cities)
CREATE VIEW Active_Orders_View AS
SELECT o.order_id, o.order_date, o.status, c.first_name
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
WHERE o.status IN ('Pending', 'Shipped');

-- ==============================================================================
-- EXPERIMENT 5: TRANSPARENT AUDIT SYSTEM TRIGGER[cite: 11]
-- ==============================================================================
-- Requirement: Keep track of records being updated, storing original details.

-- First, create the audit table
CREATE TABLE Audit_Products (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    old_price DECIMAL(10,2),
    operation VARCHAR(10),
    audit_date DATE
);

DELIMITER //
-- Second, create the trigger to automatically populate the audit table
CREATE TRIGGER Product_Audit_Update
AFTER UPDATE ON Products
FOR EACH ROW
BEGIN
    IF OLD.price != NEW.price THEN
        INSERT INTO Audit_Products (product_id, old_price, operation, audit_date)
        VALUES (OLD.product_id, OLD.price, 'UPDATE', CURDATE());
    END IF;
END //
DELIMITER ;

-- ==============================================================================
-- EXPERIMENT 10: TRIGGER WITH USER DEFINED ERROR[cite: 12]
-- ==============================================================================
-- Requirement: Trigger that raises an error message and blocks INSERT/UPDATE.

DELIMITER //
CREATE TRIGGER Prevent_Negative_Stock
BEFORE INSERT ON Products
FOR EACH ROW
BEGIN
    IF NEW.stock_quantity < 0 THEN
        -- MySQL equivalent of RAISE_APPLICATION_ERROR
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'User Defined Error: Stock quantity cannot be negative!';
    END IF;
END //
DELIMITER ;

-- ==============================================================================
-- EXPERIMENT 8 & 9: STORED PROCEDURES AND FUNCTIONS[cite: 12]
-- ==============================================================================
-- Requirement: Procedure that accepts an ID and returns details.

DELIMITER //
CREATE PROCEDURE GetEmployeeDetails(IN emp_input INT)
BEGIN
    SELECT first_name, last_name, role 
    FROM Employees 
    WHERE employee_id = emp_input;
END //
DELIMITER ;

-- Requirement: Stored Function to calculate discounted price
DELIMITER //
CREATE FUNCTION CalculateDiscount(original_price DECIMAL(10,2), discount_percent DECIMAL(5,2))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE final_price DECIMAL(10,2);
    SET final_price = original_price - (original_price * (discount_percent / 100));
    RETURN final_price;
END //
DELIMITER ;

-- ==============================================================================
-- UNIT 5 & EXPERIMENT 4: EXPLICIT CURSORS & EXCEPTION HANDLING[cite: 8, 11, 12]
-- ==============================================================================
-- Requirement: Use explicit cursor to loop through rows and flag issues.

DELIMITER //
CREATE PROCEDURE Check_Critical_Stock()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE p_name VARCHAR(100);
    DECLARE p_stock INT;
    
    -- 1. Declare the explicit cursor
    DECLARE cur_stock CURSOR FOR SELECT name, stock_quantity FROM Products;
    
    -- 2. Declare exception handler for when rows run out
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- 3. Open cursor
    OPEN cur_stock;
    
    read_loop: LOOP
        FETCH cur_stock INTO p_name, p_stock;
        
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Business Logic: Flag products that are dangerously low
        IF p_stock < 15 THEN
            SELECT CONCAT('CRITICAL WARNING: ', p_name, ' is below minimum stock levels.') AS Alert;
        END IF;
        
    END LOOP;
    
    -- 4. Close cursor
    CLOSE cur_stock;
END //
DELIMITER ;