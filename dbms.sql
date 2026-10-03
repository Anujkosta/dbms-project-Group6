DROP DATABASE IF EXISTS retail_db;
CREATE DATABASE retail_db;
USE retail_db;

-- ==========================================
-- 1. CORE ENTITIES (The Nouns) - 7 Tables
-- ==========================================
CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100),
    description VARCHAR(255)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    stock_quantity INT,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50)
);

CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY,
    company_name VARCHAR(100),
    contact_phone VARCHAR(20)
);

CREATE TABLE Shippers (
    shipper_id INT PRIMARY KEY,
    company_name VARCHAR(100),
    support_email VARCHAR(100)
);

-- NEW: Manage the internal staff handling the store
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role VARCHAR(50)
);

-- NEW: Manage promotional discounts
CREATE TABLE Coupons (
    coupon_id INT PRIMARY KEY,
    code VARCHAR(20) UNIQUE,
    discount_percentage DECIMAL(5, 2),
    valid_until DATE
);

-- ==========================================
-- 2. ASSOCIATIVE ENTITIES (The Verbs) - 7 Tables
-- ==========================================
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    coupon_id INT, -- NEW: Links order to a discount
    order_date DATE,
    status VARCHAR(20),
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (coupon_id) REFERENCES Coupons(coupon_id)
);

CREATE TABLE Order_Items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Inventory_Restock (
    restock_id INT PRIMARY KEY,
    product_id INT,
    supplier_id INT,
    restock_date DATE,
    quantity_received INT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Shipments (
    shipment_id INT PRIMARY KEY,
    order_id INT,
    shipper_id INT,
    ship_date DATE,
    tracking_number VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (shipper_id) REFERENCES Shippers(shipper_id)
);

CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    rating INT,
    review_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- NEW: Separates the financial transaction from the order record
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_date DATE,
    payment_method VARCHAR(50),
    amount_paid DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- NEW: Links customers with employees for help requests
CREATE TABLE Support_Tickets (
    ticket_id INT PRIMARY KEY,
    customer_id INT,
    employee_id INT,
    issue_description VARCHAR(255),
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);