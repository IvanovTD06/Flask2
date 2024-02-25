import faker

from my_app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/people")
def people():
    for i in range(10):
        fake = faker.Faker("ru_RU")
        fake = fake.profile()
        print(fake)
        with open("./files/people.txt", "w", encoding="utf8") as text:
            for i in range(10):
                print(fake, sep=",", file=text)

