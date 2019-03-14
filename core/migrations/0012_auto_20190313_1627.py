# Generated by Django 2.1.7 on 2019-03-13 20:27

from django.db import migrations
from django.conf import settings
import os.path
import csv
from django.core.files import File
from django.utils.text import slugify

def load_book_data(apps, schema_editor):
    pass
#     """ Read a CSV file full of free online books and insert them into the database. """
#     Book = apps.get_model('core', 'Book')
#     datapath = os.path.join(settings.BASE_DIR, 'initial_data')
#     datafile = os.path.join(datapath, 'class_list_of_books.csv')
#     with open(datafile) as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             #set book_title so that you can only add books that have not already been added
#             book_title = row['title']
#             if Book.objects.filter(title=book_title).count():
#                 return
#             #but if the title isnt there then make a new book
#             # the first part of the Book() tells what field to put it in
#             #the second part is the value to put in that field
#             book = Book(
#                 title=row['title'],
#                 author=row['author'],
#                 description=row['description'],
#                 access_online=row['access_online'],
#                 book_category=row['book_category'],
#                 slug=slugify(row['title']),
#             )
#             book.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190313_1146'),
    ]

    operations = [migrations.RunPython(load_book_data)]
