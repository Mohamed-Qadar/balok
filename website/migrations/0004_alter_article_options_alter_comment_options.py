# Generated by Django 4.0 on 2022-03-29 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]
