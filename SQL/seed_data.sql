-- 1. Core Entities
INSERT INTO Categories VALUES 
(1, 'Electronics', 'Tech gadgets and devices'), 
(2, 'Apparel', 'Clothing and fashion');

INSERT INTO Products VALUES 
(1, 'Mechanical Keyboard', 4500.00, 50, 1), 
(2, 'Wireless Mouse', 1500.00, 100, 1), 
(3, 'Cotton Hoodie', 1200.00, 30, 2);

INSERT INTO Customers VALUES 
(1, 'Aarav', 'Sharma', 'aarav@example.com', 'Bhopal'), 
(2, 'Priya', 'Singh', 'priya@example.com', 'Indore');

INSERT INTO Suppliers VALUES (1, 'TechSource India', '9876543210');
INSERT INTO Shippers VALUES (1, 'FastTrack Logistics', 'support@fasttrack.in');
INSERT INTO Employees VALUES (1, 'Rohan', 'Gupta', 'Support Agent');
INSERT INTO Coupons VALUES (1, 'WELCOME10', 10.00, '2026-12-31');

-- 2. Associative Entities
INSERT INTO Orders VALUES 
(101, 1, 1, '2026-10-01', 'Shipped', 4050.00), 
(102, 2, NULL, '2026-10-02', 'Pending', 1200.00);

INSERT INTO Order_Items VALUES 
(1, 101, 1, 1, 4500.00), 
(2, 102, 3, 1, 1200.00);

INSERT INTO Inventory_Restock VALUES (1, 1, 1, '2026-09-15', 50);
INSERT INTO Shipments VALUES (1, 101, 1, '2026-10-02', 'TRK998877');
INSERT INTO Reviews VALUES (1, 1, 1, 5, '2026-10-03');
INSERT INTO Payments VALUES (1, 101, '2026-10-01', 'Credit Card', 4050.00);
INSERT INTO Support_Tickets VALUES (1, 2, 1, 'Where is my hoodie?', 'Open');