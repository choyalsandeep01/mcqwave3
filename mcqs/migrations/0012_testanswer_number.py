# Generated by Django 4.2.14 on 2024-08-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0011_alter_mcq_correct_option_alter_mcq_difficulty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testanswer',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
