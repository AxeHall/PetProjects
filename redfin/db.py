import psycopg2


class Postgres(object):
    def __init__(self, db_name, user, pswd) -> None:
        super().__init__()
        try:
            self.connection = psycopg2.connect(
                dbname=db_name, user=user, password=pswd, host="localhost"
            )

            self.cursor = self.connection.cursor()
        except psycopg2.OperationalError:
            print("Wrong Database credentials!")
            exit()

        self.order = [
            "List Price",
            "Price/Sq.Ft.",
            "Est. Mo. Payment",
            "Buyer's Brokerage Commission",
            "HOA Dues",
            "Status",
            "Time on Redfin",
            "Property Type",
            "Year Built",
            "Style",
            "Community",
            "Lot Size",
            "MLS#",
            "beds",
            "baths",
            "address",
        ]

    def create_table(self):
        cmd = """CREATE TABLE redfin_data(
            id SERIAL PRIMARY KEY, 
            list_price INT, 
            pricesqqft INT, 
            est_mo_payment INT, 
            buyers_crokerage_compensation VARCHAR(12), 
            hoa_dues VARCHAR(50), 
            status VARCHAR(50), 
            time_on_redfin VARCHAR(50), 
            property_type VARCHAR(100), 
            year_built INT, 
            style VARCHAR(50), 
            community VARCHAR(80), 
            lot_size VARCHAR(50), 
            mls VARCHAR(50), 
            beds VARCHAR(20), 
            baths VARCHAR(20), 
            address VARCHAR(100)
        );"""

        self.cursor.execute(cmd)
        self.connection.commit()

    def get_list_of_tables(self):
        cmd = "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
        self.cursor.execute(cmd)
        return [table[0] for table in self.cursor.fetchall()]

    def insert_data(self, data):
        cmd = f"""INSERT INTO redfin_data(
            list_price, 
            pricesqqft, 
            est_mo_payment, 
            buyers_crokerage_compensation, 
            hoa_dues, 
            status, 
            time_on_redfin, 
            property_type, 
            year_built, 
            style, 
            community, 
            lot_size, 
            mls, 
            beds, 
            baths, 
            address) 
        VALUES {data};"""
        self.cursor.execute(cmd)
        self.connection.commit()

    def end(self):
        self.connection.close()
