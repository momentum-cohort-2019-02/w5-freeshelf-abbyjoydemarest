# Generated by Django 2.1.7 on 2019-03-13 20:38

from django.db import migrations
import slugger.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190313_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=slugger.fields.AutoSlugField(populate_from='title', unique=True),
        ),
    ]
