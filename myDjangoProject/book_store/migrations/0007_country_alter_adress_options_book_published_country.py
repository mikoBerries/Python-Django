# Generated by Django 4.2.3 on 2023-08-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0006_adress_alter_book_author_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='adress',
            options={'verbose_name_plural': 'adress entires'},
        ),
        migrations.AddField(
            model_name='book',
            name='published_country',
            field=models.ManyToManyField(null=True, to='book_store.country'),
        ),
    ]
