# Database Normalization – E-Commerce Management System

## 1. Introduction

Normalization is a database design technique used to organize data into tables properly[cite: 18].

The main goals of normalization are:
- Reduce data redundancy (duplicate data)[cite: 18]
- Avoid data inconsistency[cite: 18]
- Prevent insertion, deletion, and update anomalies[cite: 18]
- Improve database structure[cite: 18]
- Maintain data integrity[cite: 18]

In this E-Commerce Management System, normalization is applied to tables such as:
- Customers
- Products
- Categories
- Orders
- Order_Items
- Payments
- Shipments

---

# 2. Unnormalized Form (UNF)

Before normalization, a table may contain multiple values in a single column[cite: 18].

### Example

| Order_ID | Customer_Name | Products |
|----------|---------------|----------|
| 101 | Aarav | Mechanical Keyboard, Wireless Mouse |

Here, the `Products` column contains multiple values[cite: 18]. 

This makes searching, updating, and managing data difficult[cite: 18]. Therefore, we need to normalize the table[cite: 18].

---

# 3. First Normal Form (1NF)

A table is in **First Normal Form (1NF)** when:
1. Each column contains atomic (single) values[cite: 18].
2. There are no repeating groups[cite: 18].
3. Each row is uniquely identifiable[cite: 18].

### Before 1NF

| Order_ID | Customer_Name | Products |
|----------|---------------|----------|
| 101 | Aarav | Mechanical Keyboard, Wireless Mouse |

The `Products` column contains multiple values[cite: 18].

### After 1NF

| Order_ID | Customer_Name | Product |
|----------|---------------|---------|
| 101 | Aarav | Mechanical Keyboard |
| 101 | Aarav | Wireless Mouse |

Now every cell contains only one value[cite: 18]. Therefore, the table satisfies **1NF**[cite: 18].

---

# 4. Second Normal Form (2NF)

A table is in **Second Normal Form (2NF)** when:
1. It is already in 1NF[cite: 18].
2. It has no partial dependency[cite: 18].

### What is Partial Dependency?
Partial dependency occurs when a non-key attribute depends on only part of a composite primary key[cite: 18].

### Example
Consider an Order Items table:

| Order_ID | Product_ID | Quantity | Product_Name |
|----------|------------|----------|--------------|
| 101 | P01 | 1 | Mechanical Keyboard |
| 102 | P02 | 2 | Desk Lamp |

Suppose:
**Primary Key = (Order_ID, Product_ID)**[cite: 18]

But:
- `Quantity` depends on both `Order_ID` and `Product_ID`.
- `Product_Name` depends only on `Product_ID`[cite: 18].

Therefore, there is partial dependency[cite: 18].

### Solution
Separate the tables[cite: 18].

### Product Table
| Product_ID | Product_Name |
|------------|--------------|
| P01 | Mechanical Keyboard |
| P02 | Desk Lamp |

### Order_Items Table
| Order_ID | Product_ID | Quantity |
|----------|------------|----------|
| 101 | P01 | 1 |
| 102 | P02 | 2 |

Now non-key attributes do not depend on only part of a composite key[cite: 18]. Therefore, the database is in **2NF**[cite: 18].

---

# 5. Third Normal Form (3NF)

A table is in **Third Normal Form (3NF)** when:
1. It is already in 2NF[cite: 18].
2. There is no transitive dependency[cite: 18].

### What is Transitive Dependency?
A transitive dependency occurs when:
**A → B → C**[cite: 18]

For example:
- `Order_ID` determines `Customer_ID`[cite: 18]
- `Customer_ID` determines `Customer_City`[cite: 18]

Therefore:
**Order_ID → Customer_ID → Customer_City**[cite: 18]

The `Customer_City` indirectly depends on `Order_ID`[cite: 18].

### Example

| Order_ID | Customer_ID | Customer_City |
|----------|-------------|---------------|
| 101 | C01 | Bhopal |
| 102 | C02 | Indore |

Here:
`Order_ID → Customer_ID`[cite: 18]
and
`Customer_ID → Customer_City`[cite: 18]

So:
`Order_ID → Customer_City`[cite: 18]

This is a transitive dependency[cite: 18].

### Solution
Separate the Customer and Order information[cite: 18].

### Customers Table
| Customer_ID | Customer_City |
|-------------|---------------|
| C01 | Bhopal |
| C02 | Indore |

### Orders Table
| Order_ID | Customer_ID |
|----------|-------------|
| 101 | C01 |
| 102 | C02 |

Now the transitive dependency is removed[cite: 18]. Therefore, the tables satisfy **3NF**[cite: 18].

---

# 6. Boyce-Codd Normal Form (BCNF)

BCNF is a stronger version of 3NF[cite: 18]. 

A table is in **BCNF** when:
> For every functional dependency X → Y, X must be a super key[cite: 18].

In simple words:
**Every determinant must be a candidate key.**[cite: 18]

### Example
Consider an Inventory Restock table:

| Restock_ID | Supplier_ID | Warehouse_Zone |
|------------|-------------|----------------|
| R101 | S01 | Zone_A |
| R102 | S02 | Zone_B |

Suppose:
- A supplier only delivers to one specific warehouse zone.
- `Supplier_ID → Warehouse_Zone`[cite: 18]

If `Supplier_ID` is not a candidate key of this table, then the table violates BCNF[cite: 18].

### Solution
Separate the information[cite: 18].

### Supplier Table
| Supplier_ID | Warehouse_Zone |
|-------------|----------------|
| S01 | Zone_A |
| S02 | Zone_B |

### Inventory_Restock Table
| Restock_ID | Supplier_ID |
|------------|-------------|
| R101 | S01 |
| R102 | S02 |

This removes the dependency problem[cite: 18]. Therefore, the database satisfies **BCNF**[cite: 18].

---

# 7. Fourth Normal Form (4NF)

4NF deals with **multivalued dependencies**[cite: 18].

A table is in **Fourth Normal Form (4NF)** when:
1. It is already in BCNF[cite: 18].
2. It has no unwanted multivalued dependencies[cite: 18].

### Example
Suppose a product can have multiple:
- Available Colors
- Available Sizes

Consider:

| Product_ID | Color | Size |
|------------|-------|------|
| P01 | Black | Medium |
| P01 | Black | Large |
| P01 | White | Medium |
| P01 | White | Large |

Here, colors and sizes are independent of each other[cite: 18]. This creates unnecessary combinations[cite: 18].

### Solution
Separate them into two tables[cite: 18].

### Product Colors
| Product_ID | Color |
|------------|-------|
| P01 | Black |
| P01 | White |

### Product Sizes
| Product_ID | Size |
|------------|------|
| P01 | Medium |
| P01 | Large |

Now the multivalued dependency is removed[cite: 18]. Therefore, the tables satisfy **4NF**[cite: 18].

---

# 8. Normalization Applied to E-Commerce Management System

The E-Commerce Management System is divided into 14 properly normalized tables[cite: 18].

## Categories
| Attribute | Description |
|-----------|-------------|
| category_id | Primary Key |
| category_name | Name of the category |
| description | Category details |

## Products
| Attribute | Description |
|-----------|-------------|
| product_id | Primary Key |
| name | Name of the product |
| price | Selling price |
| stock_quantity | Current inventory |
| category_id | Foreign Key |

## Customers
| Attribute | Description |
|-----------|-------------|
| customer_id | Primary Key |
| first_name | Customer first name |
| last_name | Customer last name |
| email | Unique email |
| city | Customer location |

## Suppliers
| Attribute | Description |
|-----------|-------------|
| supplier_id | Primary Key |
| company_name | Supplier business name |
| contact_phone | Contact number |

## Shippers
| Attribute | Description |
|-----------|-------------|
| shipper_id | Primary Key |
| company_name | Logistics company name |
| support_email | Contact email |

## Employees
| Attribute | Description |
|-----------|-------------|
| employee_id | Primary Key |
| first_name | Employee first name |
| last_name | Employee last name |
| role | Job title |

## Coupons
| Attribute | Description |
|-----------|-------------|
| coupon_id | Primary Key |
| code | Unique discount code |
| discount_percentage| Discount amount |
| valid_until | Expiration date |

## Orders
| Attribute | Description |
|-----------|-------------|
| order_id | Primary Key |
| customer_id | Foreign Key |
| coupon_id | Foreign Key |
| order_date | Date placed |
| status | Current status |
| total_amount | Order total |

## Order_Items
| Attribute | Description |
|-----------|-------------|
| item_id | Primary Key |
| order_id | Foreign Key |
| product_id | Foreign Key |
| quantity | Items purchased |
| unit_price | Price at purchase |

## Inventory_Restock
| Attribute | Description |
|-----------|-------------|
| restock_id | Primary Key |
| product_id | Foreign Key |
| supplier_id | Foreign Key |
| restock_date | Date received |
| quantity_received | Amount added |

## Shipments
| Attribute | Description |
|-----------|-------------|
| shipment_id | Primary Key |
| order_id | Foreign Key |
| shipper_id | Foreign Key |
| ship_date | Dispatch date |
| tracking_number | Tracking ID |

## Reviews
| Attribute | Description |
|-----------|-------------|
| review_id | Primary Key |
| product_id | Foreign Key |
| customer_id | Foreign Key |
| rating | Star rating (1-5) |
| review_date | Date submitted |

## Payments
| Attribute | Description |
|-----------|-------------|
| payment_id | Primary Key |
| order_id | Foreign Key |
| payment_date | Date processed |
| payment_method | Mode of payment |
| amount_paid | Total paid |

## Support_Tickets
| Attribute | Description |
|-----------|-------------|
| ticket_id | Primary Key |
| customer_id | Foreign Key |
| employee_id | Foreign Key |
| issue_description | Customer complaint |
| status | Ticket status |

---

# 9. Benefits of Normalization

Normalization provides several advantages to our E-Commerce Management System[cite: 18].

### 1. Reduces Data Redundancy
The same customer, product, or supplier information does not need to be stored repeatedly[cite: 18].

### 2. Prevents Update Anomaly
If a customer's address changes, it only needs to be updated in one place (the Customers table)[cite: 18].

### 3. Prevents Insertion Anomaly
New categories or products can be added without requiring unrelated order information[cite: 18].

### 4. Prevents Deletion Anomaly
Deleting a canceled order will not accidentally delete important customer or product information[cite: 18].

### 5. Improves Data Integrity
Relationships between customers, orders, products, and shipments are maintained using primary and foreign keys[cite: 18].

### 6. Makes Database Maintenance Easier
Data is divided into logically related tables, making the database easier to manage[cite: 18].

---

# 10. Normalization Summary

| Normal Form | Main Requirement | E-Commerce Example |
|-------------|------------------|--------------------|
| 1NF | Atomic values | Separate multiple products in an order[cite: 18] |
| 2NF | Remove partial dependency | Separate product details from order items[cite: 18] |
| 3NF | Remove transitive dependency | Separate customer city from the order table[cite: 18] |
| BCNF | Every determinant must be a candidate key | Separate supplier zone assignment[cite: 18] |
| 4NF | Remove multivalued dependencies | Separate product colors and sizes[cite: 18] |

---

# 11. Conclusion

Normalization helps us design a well-structured E-Commerce Management Database[cite: 18].

The database is divided into related tables such as[cite: 18]:
- Customers
- Products
- Orders
- Order_Items
- Employees
- Shipments
- Payments

By applying 1NF, 2NF, 3NF, BCNF, and 4NF, we reduce redundancy, avoid data anomalies, maintain data integrity, and make the database easier to manage[cite: 18].

Thus, normalization provides an efficient and reliable structure for the E-Commerce Management System[cite: 18].
