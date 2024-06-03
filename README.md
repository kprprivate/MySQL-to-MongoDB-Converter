# MySQL to MongoDB Converter

## Description
This project provides a Python script to migrate data from a MySQL database to MongoDB. The script reads data from a MySQL database and inserts it into MongoDB, handling data type conversions where necessary.

## Features
- Connects to MySQL and MongoDB databases.
- Fetches all tables and their data from MySQL.
- Inserts data into corresponding MongoDB collections.
- Handles `decimal.Decimal` to `float` conversion for compatibility with MongoDB.

## Prerequisites
- Python 3.x
- MySQL server
- MongoDB server