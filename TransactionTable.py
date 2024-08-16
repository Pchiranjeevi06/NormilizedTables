class TransactionTable:
    def __init__(self, cursor):
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("SHOW TABLES LIKE 'Transactions'")
        
        if not self.cursor.fetchall():
            self.cursor.execute("""
                CREATE TABLE Transactions (
                    order_id INT PRIMARY KEY,
                    customer_id INT,
                    product_id INT,
                    product_name VARCHAR(100),
                    product_category VARCHAR(50),
                    payment_type VARCHAR(20),
                    qty INT,
                    price DECIMAL(10, 2),
                    datetime DATETIME,
                    ecommerce_website_name VARCHAR(100),
                    payment_txn_id VARCHAR(50),
                    payment_txn_success CHAR(1),
                    failure_reason VARCHAR(100),
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                );
            """)
            print("Table 'Transactions' created successfully")
        else:
            print("Table 'Transactions' already exists")

    def insert_transactions(self, transactions):
        for transaction in transactions:
            self.cursor.execute(
                """INSERT INTO Transactions (order_id, customer_id, product_id, product_name, product_category, 
                payment_type, qty, price, datetime, ecommerce_website_name, payment_txn_id, payment_txn_success, failure_reason) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    transaction['order_id'], transaction['customer_id'], transaction['product_id'],
                    transaction['product_name'], transaction['product_category'], transaction['payment_type'],
                    transaction['qty'], transaction['price'], transaction['datetime'],
                    transaction['ecommerce_website_name'], transaction['payment_txn_id'],
                    transaction['payment_txn_success'], transaction['failure_reason']
                )
            )
