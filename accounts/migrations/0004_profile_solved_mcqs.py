# Generated by Django 4.2.14 on 2024-08-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0011_alter_mcq_correct_option_alter_mcq_difficulty_and_more'),
        ('accounts', '0003_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='solved_mcqs',
            field=models.ManyToManyField(related_name='solved_by', to='mcqs.mcq'),
        ),
    ]