# Generated by Django 4.2.2 on 2023-06-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_mymodel_description_remove_mymodel_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='field1',
            field=models.TextField(),
        ),
    ]
