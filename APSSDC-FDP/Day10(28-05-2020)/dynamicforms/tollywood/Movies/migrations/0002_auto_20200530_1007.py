# Generated by Django 3.0.3 on 2020-05-30 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='noofworkers',
            field=models.IntegerField(),
        ),
    ]