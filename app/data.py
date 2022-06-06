import random
import pandas as pd

from app import db
from app.models import Book, Library, Item


def fill_with_libraries():
    data = [
        dict(
            name='Российская государственная библиотека для молодёжи',
            street='Покровка',
            building='12'
        ),
        dict(
            name='Библиотека иностранной литературы имени Рудомино',
            street='Моросейка',
            building='48a'
        ),
        dict(
            name='Центральная библиотека имени Добролюбова',
            street='пр-т Вернадского',
            building='86c1'
        )
    ]

    for i in data:
        lib = Library(**i, city='Москва', state='Москва', latitude=55.055, longitude=37.611)
        db.session.add(lib)

    db.session.commit()

def fill_with_books(n=50):
    data = pd.read_excel('/data/chitaigorod.xlsm')[:10000]

    data = data[data['Описание'].notna()]
    sample = data.sample(n=n)
    for i in range(n):
        item = sample.iloc[i]

        book = Book(
            name=item['Название'],
            author=item['Автор'],
            published=item['Издательство'],
            category=random.choice(['художественная', 'нон-фикшен', 'техническая']),
            description=item['Описание']
        )
        db.session.add(book)

    db.session.commit()

def fill_with_items(n=50):
    for book in range(n):
        libs = random.choices(list(range(3)), k=2)
        for lib in libs:
            item = Item(book=book, library=lib)
            db.session.add(item)

    db.session.commit()


def fill_with_data():
    fill_with_libraries()
    fill_with_books(100)
    fill_with_items(100)