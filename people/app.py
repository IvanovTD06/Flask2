import faker
from flask import Flask
from flask import render_template
import psycopg2
from psycopg2.errors import OperationalError


app = Flask(__name__)

def create_connection(db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection


def execute(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

@app.route("/")
def home():
    DB_connector = create_connection("postgres", "student", "123456", "localhost", "5432")
    query = '''CREATE TABLE IF NOT exists public.flask2
                ("name" VARCHAR primary key);
            '''
    execute(DB_connector, query)
    

    return render_template("index.html", name = "Hello")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/peopl")
def people():
    DB_connector = create_connection("postgres", "student", "123456", "localhost", "5432")
    for i in range(10):
        fake = faker.Faker("ru_RU")
        fake = fake.profile()
        print(fake)
        query = f'''INSERT INTO public.flask2 data ({fake.name})'''
        execute(DB_connector, query)




