# Generated by Django 3.2.3 on 2021-06-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(max_length=255),
        ),
    ]