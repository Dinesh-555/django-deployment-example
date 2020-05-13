import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','leveltwoassign.settings')
import django
django.setup()
from apptwo.models import Users
from faker import Faker
fakegen=Faker()
def pop(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = fakegen.email()
        user = Users.objects.get_or_create(first_name=fake_firstname,
                                           last_name=fake_lastname,
                                           email=fake_email)
if __name__=='__main__':
    print("Populating Database!")
    pop(20)
    print("Populating Complete!")