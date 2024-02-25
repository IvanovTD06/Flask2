import faker

def people():
    for i in range(10):
        fake = faker.Faker("ru_RU")
        fake = fake.profile()
        print(fake)
        with open("./files/people.txt", "w", encoding="utf8") as text:
            for i in range(10):
                print(fake.name().split(), sep=",", file=text)

people()
