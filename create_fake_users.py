import random
import sys
from faker import Faker


def create_fake_users(n):
    """Generate fake users."""
    faker = Faker()
    lst = []
    for i in range(n):
        minilst = [faker.name(), random.randint(19,30), faker.address().replace('\n', ', '), faker.phone_number(), faker.email()]
        lst.append(minilst)
    return lst

create_fake_users(4)