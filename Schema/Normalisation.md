# Database Normalization (3NF)

This E-Commerce database has been strictly normalized up to the Third Normal Form (3NF) to ensure data integrity, eliminate redundancy, and optimize query performance.

## First Normal Form (1NF)
* **Atomicity:** All attributes contain single, indivisible values. For example, the `Customers` table separates `first_name` and `last_name` rather than using a single combined name string.
* **Unique Identification:** Every table has a clearly defined Primary Key (e.g., `product_id`, `order_id`) to uniquely identify each record.

## Second Normal Form (2NF)
* **Full Functional Dependency:** The database is in 1NF, and all non-key attributes are fully dependent on the primary key. 
* **Associative Entities:** Tables like `Order_Items` use a surrogate primary key (`item_id`) while maintaining foreign keys to `Orders` and `Products`, ensuring that attributes like `quantity` and `unit_price` depend entirely on that specific transaction, not partially on the product or the order alone.

## Third Normal Form (3NF)
* **No Transitive Dependencies:** All non-primary-key attributes depend strictly on the primary key and nothing else. 
* **Example:** In the `Orders` table, we store the `customer_id` rather than the customer's `city` or `email`. The customer's details are stored in the `Customers` table. If a customer changes their city, it is updated in one place (the `Customers` table) without requiring updates across thousands of historical orders.