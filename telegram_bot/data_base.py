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


    def create_table_breakfast(self):
        cmd = """CREATE TABLE breakfast(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            image TEXT,
            price INT
        );"""
        
        self.cursor.execute(cmd)
        self.connection.commit()

    def create_table_pizza_40_cm(self):
        cmd = """CREATE TABLE pizza_40_cm(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            image TEXT,
            price INT
        );"""
        
        self.cursor.execute(cmd)
        self.connection.commit()

    def create_table_rolly(self):
        cmd = """CREATE TABLE rolly(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            image TEXT,
            price INT
        );"""
        
        self.cursor.execute(cmd)
        self.connection.commit()
    
    def create_table_salaty(self):
        cmd = """CREATE TABLE salaty(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            image TEXT,
            price INT
        );"""
        
        self.cursor.execute(cmd)
        self.connection.commit()

    def create_table_zakuski(self):
        cmd = """CREATE TABLE zakuski(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            image TEXT,
            price INT
        );"""
        
        self.cursor.execute(cmd)
        self.connection.commit()

    def create_table_shares(self):
        cmd = """CREATE TABLE shares(
            id SERIAL PRIMARY KEY,
            title VARCHAR,
            image TEXT,
            description TEXT
        );"""
        
        self.cursor.execute(cmd)
        self.connection.commit()

    def create_table_about(self):
        cmd = """CREATE TABLE about(
            id SERIAL PRIMARY KEY,
            description TEXT
        );"""
        
        self.cursor.execute(cmd)
        self.connection.commit()
    
    def create_table_jobs(self):
        cmd = """CREATE TABLE jobs(
            id SERIAL PRIMARY KEY,
            title VARCHAR(15),
            description TEXT
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
            price
            )
        VALUES {data};"""
        self.cursor.execute(cmd)
        self.connection.commit()
    
    def pizza_40_cm_insert_data(self, data):
        cmd = f"""INSERT INTO pizza_40_cm(
            name,
            image,
            price
            )
        VALUES {data};"""
        self.cursor.execute(cmd)
        self.connection.commit()
    
    def rolly_insert_data(self, data):
        cmd = f"""INSERT INTO rolly(
            name,
            image,
            price
            )
        VALUES {data};"""
        self.cursor.execute(cmd)
        self.connection.commit()
    
    def salaty_insert_data(self, data):
        cmd = f"""INSERT INTO salaty(
            name,
            image,
            price
            )
        VALUES {data};"""
        self.cursor.execute(cmd)
        self.connection.commit()

    def zakuski_insert_data(self, data):
        cmd = f"""INSERT INTO zakuski(
            name,
            image,
            price
            )
        VALUES {data};"""
        self.cursor.execute(cmd)
        self.connection.commit()
    
    def shares_insert_data(self, data):
        cmd = f"""INSERT INTO shares(
            title,
            image,
            description
            )
        VALUES {data};"""
        self.cursor.execute(cmd)
        self.connection.commit()
    
    def about_insert_data(self, data):
        cmd = f"""INSERT INTO about(
            description
            )
        VALUES {data};"""
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def jobs_insert_data(self, data):
        cmd = f"""INSERT INTO jobs(
            title,
            description
            )
        VALUES {data};"""
        self.cursor.execute(cmd)
        self.connection.commit()

    
    """ def get_subscription(self, status = True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM subscriptions WHERE status = ?")
 """

    def end(self):
        self.cursor.close()
        self.connection.close()