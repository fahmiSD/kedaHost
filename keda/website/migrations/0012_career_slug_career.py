# Generated by Django 4.1.6 on 2023-02-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_blog_slug_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='slug_career',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
