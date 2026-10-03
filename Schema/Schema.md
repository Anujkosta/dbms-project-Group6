# E-Commerce Retail System - Database Schema

🔗 1. Categories
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| category_id | INT | Primary Key |
| category_name | VARCHAR(100) | — |
| description | VARCHAR(255) | — |

🔗 2. Products
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| product_id | INT | Primary Key |
| name | VARCHAR(100) | — |
| price | DECIMAL(10, 2) | — |
| stock_quantity | INT | — |
| category_id | INT | Foreign Key |

🔗 3. Customers
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| customer_id | INT | Primary Key |
| first_name | VARCHAR(50) | — |
| last_name | VARCHAR(50) | — |
| email | VARCHAR(100) | UNIQUE |
| city | VARCHAR(50) | — |

🔗 4. Suppliers
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| supplier_id | INT | Primary Key |
| company_name | VARCHAR(100) | — |
| contact_phone | VARCHAR(20) | — |

🔗 5. Shippers
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| shipper_id | INT | Primary Key |
| company_name | VARCHAR(100) | — |
| support_email | VARCHAR(100) | — |

🔗 6. Employees
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| employee_id | INT | Primary Key |
| first_name | VARCHAR(50) | — |
| last_name | VARCHAR(50) | — |
| role | VARCHAR(50) | — |

🔗 7. Coupons
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| coupon_id | INT | Primary Key |
| code | VARCHAR(20) | UNIQUE |
| discount_percentage | DECIMAL(5, 2)| — |
| valid_until | DATE | — |

🔗 8. Orders
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| order_id | INT | Primary Key |
| customer_id | INT | Foreign Key |
| coupon_id | INT | Foreign Key |
| order_date | DATE | — |
| status | VARCHAR(20) | — |
| total_amount | DECIMAL(10, 2) | — |

🔗 9. Order_Items
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| item_id | INT | Primary Key |
| order_id | INT | Foreign Key |
| product_id | INT | Foreign Key |
| quantity | INT | — |
| unit_price | DECIMAL(10, 2) | — |

🔗 10. Inventory_Restock
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| restock_id | INT | Primary Key |
| product_id | INT | Foreign Key |
| supplier_id | INT | Foreign Key |
| restock_date | DATE | — |
| quantity_received | INT | — |

🔗 11. Shipments
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| shipment_id | INT | Primary Key |
| order_id | INT | Foreign Key |
| shipper_id | INT | Foreign Key |
| ship_date | DATE | — |
| tracking_number | VARCHAR(50) | — |

🔗 12. Reviews
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| review_id | INT | Primary Key |
| product_id | INT | Foreign Key |
| customer_id | INT | Foreign Key |
| rating | INT | — |
| review_date | DATE | — |

🔗 13. Payments
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| payment_id | INT | Primary Key |
| order_id | INT | Foreign Key |
| payment_date | DATE | — |
| payment_method | VARCHAR(50) | — |
| amount_paid | DECIMAL(10, 2) | — |

🔗 14. Support_Tickets
| Attribute | Data Type | Key |
| :--- | :--- | :--- |
| ticket_id | INT | Primary Key |
| customer_id | INT | Foreign Key |
| employee_id | INT | Foreign Key |
| issue_description | VARCHAR(255) | — |
| status | VARCHAR(20) | — |