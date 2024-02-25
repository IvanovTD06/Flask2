import faker

def people():
    for i in range(10):
        fake = faker.Faker("ru_RU")
        fake = fake.profile()
        print(fake)
        text = open("./files/people.txt").write(fake)
people()
