import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

from first_app.models import User
from faker import Faker

def main():
    fake_gen = Faker()

    try:
        for i in range(50):
            first_name_gen = fake_gen.first_name()
            last_name_gen = fake_gen.last_name()
            email_gen = fake_gen.email()

            user_generated = User.objects.get_or_create(first_name=first_name_gen, 
                                    last_name=last_name_gen, 
                                    email=email_gen)[0]
            user_generated.save()
        
    except:
        return False

    return True



if __name__ == '__main__':
    print('Populating fake data')
    try:
        status = main()
        if not status:
            raise RuntimeError()
        print('Data populated successfully')
    except:
        print('Failed to populate fake data')


#kush
#Django13