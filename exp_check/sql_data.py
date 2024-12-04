import sqlite3 as sql

def create(path:str):
    with open(path, 'w') as f:
        pass
    
    connection = sql.connect(path)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE food_data(food, date added, expiration date)")
    cursor.execute("CREATE TABLE meta_data(key, value)")
    cursor.execute("INSERT INTO meta_data VALUES('last write time', 20241201)")
    cursor.execute("INSERT INTO meta_data VALUES('last read time', 20241201)")
    connection.commit()

def add_row(path, food:str, date_added, expiration_date):
    connection = sql.connect(path)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO food_data VALUES(?, ?, ?)", 
        (food, date_added, expiration_date)
    )
    connection.commit()

def delete_row(path, food:str):
    connection = sql.connect(path)
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM food_data where food='{food}'")
    connection.commit()
    
def to_string(path):
    connection = sql.connect(path)
    cursor = connection.cursor()
    # cursor.execute(".headers on")

    cursor.execute("SELECT * from food_data")
    return cursor.fetchall() 

if __name__ == "__main__":
    path = "food_data.db"
    create(path)
    print(to_string(path))
    add_row(path, "cheese", 393939, 390393402)
    print(to_string(path))
    delete_row(path, "cheese")
    print(to_string(path))
    
