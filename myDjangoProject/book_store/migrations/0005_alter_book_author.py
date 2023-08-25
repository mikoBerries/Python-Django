# Generated by Django 4.2.3 on 2023-08-25 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0004_author_alter_book_rating_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bboks', to='book_store.author'),
        ),
    ]
