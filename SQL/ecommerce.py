import csv
import os

os.makedirs('Data', exist_ok=True)

def write_csv(filename, headers, rows):
    filepath = os.path.join('Data', filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

print("Writing 17 static records for 14 tables...")

# 1. Categories (17 rows)
categories = [
    [1, 'Electronics', 'Tech gadgets and devices'], [2, 'Apparel', 'Clothing and fashion'],
    [3, 'Home & Garden', 'Furniture and outdoor'], [4, 'Sports', 'Athletic gear'],
    [5, 'Beauty', 'Cosmetics and skincare'], [6, 'Books', 'Fiction and academics'],
    [7, 'Automotive', 'Car accessories'], [8, 'Toys', 'Childrens games'],
    [9, 'Groceries', 'Daily essentials and food'], [10, 'Health', 'Vitamins and supplements'],
    [11, 'Office', 'Stationery and supplies'], [12, 'Pet Supplies', 'Food and accessories for pets'],
    [13, 'Music', 'Instruments and vinyls'], [14, 'Movies', 'DVDs and Blu-rays'],
    [15, 'Video Games', 'Consoles and PC games'], [16, 'Baby', 'Diapers and baby care'],
    [17, 'Industrial', 'Heavy machinery and tools']
]
write_csv('categories.csv', ['category_id', 'category_name', 'description'], categories)

# 2. Products (17 rows)
products = [
    [1, 'Mechanical Keyboard', 4500.00, 50, 1], [2, 'Cotton Hoodie', 1200.00, 30, 2],
    [3, 'Desk Lamp', 800.00, 20, 3], [4, 'Yoga Mat', 600.00, 100, 4],
    [5, 'Vitamin C Serum', 450.00, 60, 5], [6, 'Database Concepts 6th Ed', 950.00, 15, 6],
    [7, 'Car Dashboard Camera', 3200.00, 25, 7], [8, 'Lego Star Wars', 5400.00, 10, 8],
    [9, 'Organic Green Tea', 350.00, 200, 9], [10, 'Whey Protein 1kg', 2200.00, 45, 10],
    [11, 'Ergonomic Chair', 8500.00, 12, 11], [12, 'Dog Chew Toy', 250.00, 150, 12],
    [13, 'Acoustic Guitar', 6500.00, 8, 13], [14, 'Inception Blu-Ray', 799.00, 40, 14],
    [15, 'PlayStation 5 Controller', 5990.00, 35, 15], [16, 'Baby Stroller', 4500.00, 18, 16],
    [17, 'Power Drill 800W', 2800.00, 22, 17]
]
write_csv('products.csv', ['product_id', 'name', 'price', 'stock_quantity', 'category_id'], products)

# 3. Customers (17 rows)
customers = [
    [1, 'Aarav', 'Sharma', 'aarav.s@example.com', 'Bhopal'], [2, 'Priya', 'Singh', 'priya.s@example.com', 'Indore'],
    [3, 'Rohan', 'Gupta', 'rohan.g@example.com', 'Bangalore'], [4, 'Neha', 'Verma', 'neha.v@example.com', 'Chennai'],
    [5, 'Aditya', 'Rao', 'aditya.r@example.com', 'Mumbai'], [6, 'Kavya', 'Nair', 'kavya.n@example.com', 'Kochi'],
    [7, 'Arjun', 'Patel', 'arjun.p@example.com', 'Ahmedabad'], [8, 'Sneha', 'Reddy', 'sneha.r@example.com', 'Hyderabad'],
    [9, 'Vikram', 'Iyer', 'vikram.i@example.com', 'Pune'], [10, 'Ananya', 'Desai', 'ananya.d@example.com', 'Surat'],
    [11, 'Rahul', 'Jain', 'rahul.j@example.com', 'Jaipur'], [12, 'Meera', 'Joshi', 'meera.j@example.com', 'Lucknow'],
    [13, 'Siddharth', 'Bose', 'siddharth.b@example.com', 'Kolkata'], [14, 'Pooja', 'Menon', 'pooja.m@example.com', 'Trivandrum'],
    [15, 'Karan', 'Malhotra', 'karan.m@example.com', 'Delhi'], [16, 'Divya', 'Pillai', 'divya.p@example.com', 'Coimbatore'],
    [17, 'Ishaan', 'Choudhury', 'ishaan.c@example.com', 'Guwahati']
]
write_csv('customers.csv', ['customer_id', 'first_name', 'last_name', 'email', 'city'], customers)

# 4. Suppliers (17 rows)
suppliers = [
    [1, 'TechSource India', '9876543210'], [2, 'Global Fabrics', '8765432109'],
    [3, 'Woodland Furnishings', '7654321098'], [4, 'FitGear Manufacturing', '6543210987'],
    [5, 'Glow Cosmetics Labs', '5432109876'], [6, 'Oxford Print Press', '4321098765'],
    [7, 'AutoParts Hub', '3210987654'], [8, 'Joyful Toys Ltd', '2109876543'],
    [9, 'FreshFarms Wholesale', '1098765432'], [10, 'VitalHealth Supps', '9988776655'],
    [11, 'OfficePro Essentials', '8877665544'], [12, 'HappyPets Co', '7766554433'],
    [13, 'Melody Instruments', '6655443322'], [14, 'CineMagic Distributors', '5544332211'],
    [15, 'GamerZone Hardware', '4433221100'], [16, 'TinyTots Care', '3322110099'],
    [17, 'BuildRight Tools', '2211009988']
]
write_csv('suppliers.csv', ['supplier_id', 'company_name', 'contact_phone'], suppliers)

# 5. Shippers (17 rows)
shippers = [
    [1, 'FastTrack Logistics', 'support@fasttrack.in'], [2, 'SafeDrop Couriers', 'help@safedrop.in'],
    [3, 'BlueDart Express', 'care@bluedart.in'], [4, 'Delhivery', 'support@delhivery.com'],
    [5, 'Ecom Express', 'customercare@ecom.in'], [6, 'XpressBees', 'help@xpressbees.in'],
    [7, 'India Post', 'support@indiapost.gov.in'], [8, 'FedEx India', 'india@fedex.com'],
    [9, 'DHL Supply Chain', 'support@dhl.in'], [10, 'Shadowfax', 'contact@shadowfax.in'],
    [11, 'Gati KWE', 'customerservice@gati.com'], [12, 'DTDC', 'support@dtdc.com'],
    [13, 'Ekart Logistics', 'cs@ekart.com'], [14, 'Amazon Shipping', 'help@amazon.in'],
    [15, 'DotZot', 'support@dotzot.in'], [16, 'WowExpress', 'care@wowexpress.in'],
    [17, 'Professional Couriers', 'info@tpc.in']
]
write_csv('shippers.csv', ['shipper_id', 'company_name', 'support_email'], shippers)

# 6. Employees (17 rows)
employees = [
    [1, 'Ramesh', 'Kumar', 'Store Manager'], [2, 'Anita', 'Deshmukh', 'Support Agent'],
    [3, 'Suresh', 'Patel', 'Warehouse Lead'], [4, 'Manoj', 'Tiwari', 'Inventory Clerk'],
    [5, 'Geeta', 'Phogat', 'Logistics Coordinator'], [6, 'Deepak', 'Singh', 'Support Agent'],
    [7, 'Sunita', 'Rao', 'HR Manager'], [8, 'Rajesh', 'Khanna', 'IT Administrator'],
    [9, 'Kavita', 'Krishnan', 'Marketing Lead'], [10, 'Amit', 'Shah', 'Sales Associate'],
    [11, 'Neha', 'Sharma', 'Support Agent'], [12, 'Vinod', 'Kamble', 'Warehouse Staff'],
    [13, 'Pooja', 'Hegde', 'Data Analyst'], [14, 'Tarun', 'Gill', 'Support Agent'],
    [15, 'Simran', 'Kaur', 'Accounts Manager'], [16, 'Ajay', 'Devgan', 'Security Head'],
    [17, 'Alia', 'Bhatt', 'Social Media Executive']
]
write_csv('employees.csv', ['employee_id', 'first_name', 'last_name', 'role'], employees)

# 7. Coupons (17 rows)
coupons = [
    [1, 'WELCOME10', 10.00, '2026-12-31'], [2, 'FESTIVE20', 20.00, '2026-11-15'],
    [3, 'DIWALI25', 25.00, '2026-10-30'], [4, 'NEWYEAR15', 15.00, '2027-01-05'],
    [5, 'SUMMER5', 5.00, '2027-05-31'], [6, 'WINTER10', 10.00, '2026-12-25'],
    [7, 'FREESHIP', 100.00, '2026-10-15'], [8, 'TECH15', 15.00, '2026-11-01'],
    [9, 'FASHION20', 20.00, '2026-10-20'], [10, 'HOME10', 10.00, '2026-10-25'],
    [11, 'SPORTS5', 5.00, '2026-11-10'], [12, 'BEAUTY12', 12.00, '2026-11-05'],
    [13, 'BOOKS10', 10.00, '2026-10-18'], [14, 'AUTO15', 15.00, '2026-11-20'],
    [15, 'TOYS20', 20.00, '2026-11-14'], [16, 'GROCERY5', 5.00, '2026-10-10'],
    [17, 'VIPMEMBER30', 30.00, '2027-12-31']
]
write_csv('coupons.csv', ['coupon_id', 'code', 'discount_percentage', 'valid_until'], coupons)

# 8. Orders (17 rows)
orders = [
    [101, 1, 1, '2026-10-01', 'Shipped', 4500.00], [102, 2, '', '2026-10-01', 'Pending', 1200.00],
    [103, 3, 2, '2026-10-02', 'Delivered', 800.00], [104, 4, '', '2026-10-02', 'Shipped', 600.00],
    [105, 5, 3, '2026-10-03', 'Cancelled', 450.00], [106, 6, '', '2026-10-03', 'Delivered', 950.00],
    [107, 7, 4, '2026-10-04', 'Shipped', 3200.00], [108, 8, '', '2026-10-04', 'Pending', 5400.00],
    [109, 9, 5, '2026-10-05', 'Delivered', 350.00], [110, 10, '', '2026-10-05', 'Shipped', 2200.00],
    [111, 11, 6, '2026-10-06', 'Pending', 8500.00], [112, 12, '', '2026-10-06', 'Delivered', 250.00],
    [113, 13, 7, '2026-10-07', 'Shipped', 6500.00], [114, 14, '', '2026-10-07', 'Pending', 799.00],
    [115, 15, 8, '2026-10-08', 'Delivered', 5990.00], [116, 16, '', '2026-10-08', 'Shipped', 4500.00],
    [117, 17, 9, '2026-10-09', 'Pending', 2800.00]
]
write_csv('orders.csv', ['order_id', 'customer_id', 'coupon_id', 'order_date', 'status', 'total_amount'], orders)

# 9. Order_Items (17 rows)
order_items = [
    [1, 101, 1, 1, 4500.00], [2, 102, 2, 1, 1200.00],
    [3, 103, 3, 1, 800.00], [4, 104, 4, 1, 600.00],
    [5, 105, 5, 1, 450.00], [6, 106, 6, 1, 950.00],
    [7, 107, 7, 1, 3200.00], [8, 108, 8, 1, 5400.00],
    [9, 109, 9, 1, 350.00], [10, 110, 10, 1, 2200.00],
    [11, 111, 11, 1, 8500.00], [12, 112, 12, 1, 250.00],
    [13, 113, 13, 1, 6500.00], [14, 114, 14, 1, 799.00],
    [15, 115, 15, 1, 5990.00], [16, 116, 16, 1, 4500.00],
    [17, 117, 17, 1, 2800.00]
]
write_csv('order_items.csv', ['item_id', 'order_id', 'product_id', 'quantity', 'unit_price'], order_items)

# 10. Inventory_Restock (17 rows)
restocks = [
    [1, 1, 1, '2026-09-01', 100], [2, 2, 2, '2026-09-02', 50],
    [3, 3, 3, '2026-09-03', 40], [4, 4, 4, '2026-09-04', 150],
    [5, 5, 5, '2026-09-05', 80], [6, 6, 6, '2026-09-06', 30],
    [7, 7, 7, '2026-09-07', 45], [8, 8, 8, '2026-09-08', 25],
    [9, 9, 9, '2026-09-09', 300], [10, 10, 10, '2026-09-10', 60],
    [11, 11, 11, '2026-09-11', 20], [12, 12, 12, '2026-09-12', 200],
    [13, 13, 13, '2026-09-13', 15], [14, 14, 14, '2026-09-14', 60],
    [15, 15, 15, '2026-09-15', 55], [16, 16, 16, '2026-09-16', 35],
    [17, 17, 17, '2026-09-17', 40]
]
write_csv('inventory_restock.csv', ['restock_id', 'product_id', 'supplier_id', 'restock_date', 'quantity_received'], restocks)

# 11. Shipments (17 rows)
shipments = [
    [1, 101, 1, '2026-10-02', 'TRK1001'], [2, 103, 2, '2026-10-03', 'TRK1002'],
    [3, 104, 3, '2026-10-03', 'TRK1003'], [4, 106, 4, '2026-10-04', 'TRK1004'],
    [5, 107, 5, '2026-10-05', 'TRK1005'], [6, 109, 6, '2026-10-06', 'TRK1006'],
    [7, 110, 7, '2026-10-06', 'TRK1007'], [8, 112, 8, '2026-10-07', 'TRK1008'],
    [9, 113, 9, '2026-10-08', 'TRK1009'], [10, 115, 10, '2026-10-09', 'TRK1010'],
    [11, 116, 11, '2026-10-09', 'TRK1011'], [12, 101, 12, '2026-10-03', 'TRK1012'],
    [13, 103, 13, '2026-10-04', 'TRK1013'], [14, 104, 14, '2026-10-05', 'TRK1014'],
    [15, 106, 15, '2026-10-06', 'TRK1015'], [16, 107, 16, '2026-10-07', 'TRK1016'],
    [17, 109, 17, '2026-10-08', 'TRK1017']
]
write_csv('shipments.csv', ['shipment_id', 'order_id', 'shipper_id', 'ship_date', 'tracking_number'], shipments)

# 12. Reviews (17 rows)
reviews = [
    [1, 1, 1, 5, '2026-10-05'], [2, 2, 2, 4, '2026-10-06'],
    [3, 3, 3, 5, '2026-10-07'], [4, 4, 4, 3, '2026-10-08'],
    [5, 5, 5, 4, '2026-10-09'], [6, 6, 6, 5, '2026-10-10'],
    [7, 7, 7, 2, '2026-10-11'], [8, 8, 8, 4, '2026-10-12'],
    [9, 9, 9, 5, '2026-10-13'], [10, 10, 10, 4, '2026-10-14'],
    [11, 11, 11, 5, '2026-10-15'], [12, 12, 12, 3, '2026-10-16'],
    [13, 13, 13, 4, '2026-10-17'], [14, 14, 14, 5, '2026-10-18'],
    [15, 15, 15, 4, '2026-10-19'], [16, 16, 16, 5, '2026-10-20'],
    [17, 17, 17, 4, '2026-10-21']
]
write_csv('reviews.csv', ['review_id', 'product_id', 'customer_id', 'rating', 'review_date'], reviews)

# 13. Payments (17 rows)
payments = [
    [1, 101, '2026-10-01', 'Credit Card', 4500.00], [2, 102, '2026-10-01', 'UPI', 1200.00],
    [3, 103, '2026-10-02', 'Net Banking', 800.00], [4, 104, '2026-10-02', 'Debit Card', 600.00],
    [5, 105, '2026-10-03', 'UPI', 450.00], [6, 106, '2026-10-03', 'Credit Card', 950.00],
    [7, 107, '2026-10-04', 'Net Banking', 3200.00], [8, 108, '2026-10-04', 'Debit Card', 5400.00],
    [9, 109, '2026-10-05', 'UPI', 350.00], [10, 110, '2026-10-05', 'Credit Card', 2200.00],
    [11, 111, '2026-10-06', 'Net Banking', 8500.00], [12, 112, '2026-10-06', 'UPI', 250.00],
    [13, 113, '2026-10-07', 'Credit Card', 6500.00], [14, 114, '2026-10-07', 'Debit Card', 799.00],
    [15, 115, '2026-10-08', 'UPI', 5990.00], [16, 116, '2026-10-08', 'Net Banking', 4500.00],
    [17, 117, '2026-10-09', 'Credit Card', 2800.00]
]
write_csv('payments.csv', ['payment_id', 'order_id', 'payment_date', 'payment_method', 'amount_paid'], payments)

# 14. Support_Tickets (17 rows)
tickets = [
    [1, 1, 2, 'Keyboard switches sticking', 'Open'], [2, 2, 6, 'Wrong size hoodie received', 'Closed'],
    [3, 3, 11, 'Lamp arrived broken', 'In Progress'], [4, 4, 14, 'Late delivery', 'Closed'],
    [5, 5, 2, 'Serum seal was broken', 'Open'], [6, 6, 6, 'Pages missing from book', 'In Progress'],
    [7, 7, 11, 'Camera not recording', 'Closed'], [8, 8, 14, 'Missing lego pieces', 'Open'],
    [9, 9, 2, 'Tea tastes stale', 'Closed'], [10, 10, 6, 'Protein tub dented', 'In Progress'],
    [11, 11, 11, 'Chair wheels missing', 'Open'], [12, 12, 14, 'Dog toy tore instantly', 'Closed'],
    [13, 13, 2, 'Guitar string snapped', 'In Progress'], [14, 14, 6, 'Blu-ray case cracked', 'Closed'],
    [15, 15, 11, 'Controller drift issue', 'Open'], [16, 16, 14, 'Stroller wheel jammed', 'In Progress'],
    [17, 17, 2, 'Drill battery not charging', 'Closed']
]
write_csv('support_tickets.csv', ['ticket_id', 'customer_id', 'employee_id', 'issue_description', 'status'], tickets)

print("Success! Generated 17 hardcoded records for all 14 files.")