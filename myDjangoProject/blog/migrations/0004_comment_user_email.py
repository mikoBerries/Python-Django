# Generated by Django 4.2.3 on 2023-08-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]