import faker
from my_app import app

@app.route("/people")
def FAKER():
    fake = faker.Faker("ru_RU")
    fake.profile
    text = open("./files/people.txt").write(fake)
