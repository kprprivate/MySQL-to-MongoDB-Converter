import pymysql
import pymongo
from decimal import Decimal

# MySQL connection details
mysql_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': 'TESTDATABASE'
}

uri = "mongodb+srv://USER:PSW@SERVER/?retryWrites=true&w=majority&appName=appName"

# MongoDB connection details
mongo_client = pymongo.MongoClient()
mongo_db = mongo_client["TESTDATABASE"]


def convert_decimal_to_float(data):
    if isinstance(data, dict):
        return {k: convert_decimal_to_float(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_decimal_to_float(i) for i in data]
    elif isinstance(data, Decimal):
        return float(data)
    else:
        return data


def fetch_mysql_data():
    connection = pymysql.connect(**mysql_config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    data = {}
    for table in tables:
        table_name = table['Tables_in_' + mysql_config['database']]
        cursor.execute(f"SELECT * FROM `{table_name}`")  # Escape table name with backticks
        rows = cursor.fetchall()
        data[table_name] = rows

    cursor.close()
    connection.close()
    return data


def insert_into_mongodb(data):
    for table_name, rows in data.items():
        collection = mongo_db[table_name]
        if rows:
            rows = convert_decimal_to_float(rows)
            collection.insert_many(rows)


def main():
    mysql_data = fetch_mysql_data()
    insert_into_mongodb(mysql_data)
    print("Data migration from MySQL to MongoDB completed successfully.")


if __name__ == "__main__":
    main()
