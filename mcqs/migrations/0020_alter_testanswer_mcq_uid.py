# Generated by Django 4.2.14 on 2024-09-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0019_testsession_selections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testanswer',
            name='mcq_uid',
            field=models.UUIDField(),
        ),
    ]