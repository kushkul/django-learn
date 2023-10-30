import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice_project.settings')

import django
django.setup()

# Faker
import random
from second_app.models import Topic, AccessRecord, Webpage
from faker import Faker

fakegen = Faker()

topic_list = ['Social', 'Travel', 'Education', 'News', 'Media']

def add_topic(topic_list):
    t = Topic.objects.get_or_create(top_name=random.choice(topic_list))[0]
    t.save()
    return t


def populate(N=10):

    for iteration in range(N):
        top = add_topic(topic_list)

        # Creating fake data
        fake_name = fakegen.name()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        webpge = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        acc_rcd = AccessRecord.objects.get_or_create(name=webpge, date=fake_date)[0]
        
    return


if __name__=='__main__':
    print('Generating data')
    populate(25)
    print('Data generated successfully')
