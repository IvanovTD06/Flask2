import faker
from my_app import app

@app.route("/people")
def FAKER():
    for i in range(10):
        fake = faker.Faker("ru_RU")
        fake = fake.profile()
        text = open("./files/people.txt").write(fake)
