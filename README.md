#  E-Commerce Retail Database System

A comprehensive, strictly normalized E-Commerce Database System built using Python and MySQL. 
The project provides a fully structured 14-table schema to manage retail operations, complete with automated triggers, explicit cursors, and transaction auditing directly within the MySQL database. 🛠️💻

##  Features

*  Manage customers and internal employees
*  Manage product inventory and supplier restocks
*  Track shipments and order statuses
*  Process payments and promotional coupons
*  Manage customer support tickets and product reviews
*  Strictly normalized to 3NF to eliminate data redundancy
*  Run complex multi-table SQL `SELECT` joins and aggregations
*  Execute automated `AFTER UPDATE` Triggers for transparent data auditing
*  Execute `BEFORE INSERT` Triggers with User-Defined Exceptions
*  Utilize explicit PL/SQL Cursors for automated batch price adjustments

##  Technologies Used

*  Python
*  MySQL
*  MySQL Workbench (for ERD generation and PL/SQL execution)

##  Installation & Setup

1. **Initialize the Database:**
   Open MySQL Workbench and execute the DDL script to generate the 14 tables:
    ```SQL
   SOURCE path/to/Schema/schema.sql;

**Generate the Data (Optional):**
    If you wish to regenerate the raw CSV data files, run the provided Python script:
    ```Bash
    python SQL/ecommerce.py

2. **Seed the Database:**
    Populate the tables with the hardcoded relational data:
    ```SQL
    SOURCE path/to/SQL/seed_data.sql;

3. **Execute Business Logic:**
    Run the advanced stored procedures, triggers, and views located in SQL/queries.sql to test the database constraints and automation.


    Save both files in VS Code. To finalize your GitHub repository, open your terminal and run:
    ```Bash
    git add Schema/Schema.md README.md
    git commit -m "docs: add comprehensive 14-table schema dictionary and project readme"
    git push    
