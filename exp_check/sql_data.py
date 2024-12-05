import sqlite3 as sql
import pathlib
import datetime
import time

main_table = "food_data"
meta_table = "meta_data"

new_database_script = f"""
    CREATE TABLE {main_table}(food, date added, expiration date);
    CREATE TABLE {meta_table}(key, value);
    INSERT INTO {meta_table} VALUES('last write time', 0);
    INSERT INTO {meta_table} VALUES('last read time', 0);
"""

update_write_cmd = (
    f"UPDATE {meta_table} SET value = ? "
    "WHERE key='last write time'"
)
update_read_cmd = (
    f"UPDATE {meta_table} SET value = ? "
    "WHERE key='last read time'"
)
insert_cmd = f"INSERT INTO {main_table} VALUES(?, ?, ?)"
delete_cmd = f"DELETE FROM {main_table} where food=?"
get_all_cmd = f"SELECT * from {main_table}"
get_meta_cmd = f"SELECT * from {meta_table}"

date_format = "%Y%m%d%H%M"

def get_now():
    return datetime.datetime.now().strftime(date_format)

class SQLiteDB():
    def __init__(self, path):
        self.path = path
        if not pathlib.Path(path).is_file():
            self.reset(path)
        
        self.connection = sql.connect(path)
        self.cursor = self.connection.cursor()


    def __del__(self):
        # save changes before closing
        self.connection.commit()
        self.connection.close()

    def reset(self):
        with open(self.path, 'w') as f:
            pass
        
        connection = sql.connect(self.path)
        cursor = connection.cursor()
        now = get_now()
        cursor.executescript(new_database_script)
        cursor.execute(update_read_cmd, (now,))
        cursor.execute(update_write_cmd, (now,))
        connection.commit()
        connection.close()

        self.connection = sql.connect(path)
        self.cursor = self.connection.cursor()


    def add_row(self, food:str, date_added, expiration_date):
        self.cursor.execute(insert_cmd, (food, date_added, expiration_date))
        self.cursor.execute(update_write_cmd, (get_now(),))
        self.connection.commit()

    def delete_row(self, food:str):
        self.cursor.execute(delete_cmd, (food,))
        self.cursor.execute(update_write_cmd, (get_now(),))
        self.connection.commit()
    
    def to_list(self):
        self.cursor.execute(get_all_cmd)
        return self.cursor.fetchall()
    
    def meta_to_list(self):
        self.cursor.execute(get_meta_cmd)
        return self.cursor.fetchall()

if __name__ == "__main__":
    path = "food_data.db"
    db = SQLiteDB(path)
    db.reset()
    print(db.to_list(), db.meta_to_list())
    db.add_row("cheese", get_now(), get_now())
    print(db.to_list(), db.meta_to_list())
    db.delete_row("cheese")
    print(db.to_list(), db.meta_to_list())
    
