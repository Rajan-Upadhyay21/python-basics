# ---------------------------------------------------------
# Program: Singleton Pattern Basic Example
# Description:
# This program demonstrates a simple singleton design pattern.
# ---------------------------------------------------------

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print("Are both objects the same?", db1 is db2)
