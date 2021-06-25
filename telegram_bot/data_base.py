import psycopg2

class Postgres(object):
    def __init__(self, db_name, user, pswd):
        try:
            self.connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=pswd,
                host="localhost"
            )

            self.cursor = self.connection.cursor()
        except psycopg2.OperationalError:
            print("Wrong Database credentials!")
            exit()
        self.order = [
            "Name",
            "Pictures",
            "Price"
        ]

    def create_table_breakfast(self):
        cmd = """CREATE TABLE breakfast(
            id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            image TEXT,
            price INT
        );"""
        
        self.cursor.execute(cmd)
        self.connection.commit()

    def get_list_of_tables(self):
        cmd = "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
        self.cursor.execute(cmd)
        return [table[0] for table in self.cursor.fetchall()]
        
    def breakfast_insert_data(self, data):
        cmd = f"""INSERT INTO breakfast(
            name,
            image,
            price)
        VALUES {data};"""
        
        self.cursor.execute(cmd)
        self.connection.commit()
    
    def end(self):
        self.connection.close()