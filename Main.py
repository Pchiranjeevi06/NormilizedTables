import mysql.connector
import json

from Customers import CustomersTable 
from OrdersTable import OrdersTable
from ProductsTable import ProductsTable
from OrdersTableItems import OrderItemsTable
from Payments import PaymentsTable

# from TransactionTable import TransactionTable 


def Conn():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Chiru@2002',
        database='RevaturePro'
    )

def ExecuteTables():
    T1 = CustomersTable(cursor)
    T1.create_table()
    T1.insert_customers(customers)

    T2 = OrdersTable(cursor)
    T2.create_table()
    T2.insert_order(transactions)
    
    
    T3=ProductsTable(cursor)
    T3.create_table()
    T3.insert_product(transactions)

    T4 = OrderItemsTable(cursor)
    T4.create_table()
    T4.insert_order_items(transactions)

    T5 = PaymentsTable(cursor)
    T5.create_table()
    T5.insert_payment(transactions)

# ------------- Start Execution --------------------------------
with open('D:\Python\P0\customers.json', 'r') as json_file1:
    customers = json.load(json_file1)

with open('D:\Python\P0\\transaction_logs.json', 'r') as json_file2:
    transactions = json.load(json_file2)

try:
    MYDB = Conn()
    cursor = MYDB.cursor()

    # ExecuteTables()

    MYDB.commit()  # Ensure changes are committed


    query = input("Enter SQL query:")
    cursor.execute(query)

    # Fetch and display results
    results = cursor.fetchall()
    x = 0
    for row in results:
        if x < 10:
            print(row)  # Adjust this based on the structure of your results
        else:
            break
        x += 1

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    MYDB.close()
