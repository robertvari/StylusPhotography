from django.shortcuts import render
import random
from datetime import datetime

from faker import Faker
fake = Faker()


def create_photo():
    categories = ['nature', 'cities', 'wedding', 'people']

    category = random.choice(categories)
    title = fake.sentence()
    description = fake.text()

    return {
        "title": title,
        "category": category,
        "image": f"https://source.unsplash.com/800x600/?{category}{random.randint(1, 1000)}",
        "description": description,
        "creation_date": datetime.now()
    }


def gallery_view(request):
    photos = [create_photo() for i in range(30)]
    return render(request, 'gallery/gallery_home.html', {"photos": photos})
