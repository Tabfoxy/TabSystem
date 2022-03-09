import pymysql

class DataBase:
    def __init__(self):
        pass
    
    def connection_database(self):
        try:
            self.connection = pymysql.connect(
                host = '127.0.0.1',
                port = 3306,
                user = 'root',
                password = '',
                database = 'rolebot',
                cursorclass = pymysql.cursors.DictCursor
            )
        except Exception:
            print ("Error connecting to")
    
    def create_table(self):
        self.connection_database()
        with self.connection.cursor() as cursor:
            create_table = "CREATE TABLE nicknames (id int AUTO_INCREMENT, user_id varchar(32), chat_id varchar(32), nickname varchar(32), PRIMARY KEY (id))"
            cursor.execute(create_table)
            print("Ахуеть чел, таблицу нахуярили")
    
    def create_nickname(self, nickname, chat_id, user_id):
        self.connection_database()
        with self.connection.cursor() as cursor:
            insert_database = f"INSERT INTO nicknames SET user_id='{user_id}', chat_id='{chat_id}', nickname='{nickname}';"
            cursor.execute(insert_database)
            self.connection.commit()
    
    def check_database(self, chat_id, user_id):
        self.connection_database()
        user_id = str(user_id)
        chat_id = str(chat_id)
        with self.connection.cursor() as cursor:
            select_data = "SELECT * FROM nicknames"
            cursor.execute(select_data)
            rows = cursor.fetchall()
            for i in rows:
                if i.get("user_id") == user_id and i.get("chat_id") == chat_id:
                    return "Есть"
                else:
                    return "Нет"


    
    def delete_nickname(self, user_id):
        self.connection_database()
        with self.connection.cursor() as cursor:
            delete_data = f"DELETE FROM nicknames WHERE user_id = '{user_id}';"
            cursor.execute(delete_data)
            self.connection.commit()

    
    def get_nick(self, chat_id, user_id):
        self.connection_database()
        user_id = str(user_id)
        chat_id = str(chat_id)
        with self.connection.cursor() as cursor:
            select_data = "SELECT * FROM nicknames"
            cursor.execute(select_data)
            rows = cursor.fetchall()
            for i in rows:
                if i.get("user_id") == user_id and i.get("chat_id") == chat_id:
                    return i.get("nickname")

