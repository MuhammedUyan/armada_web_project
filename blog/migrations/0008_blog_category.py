# Generated by Django 5.0.3 on 2024-03-12 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]