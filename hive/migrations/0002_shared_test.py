# Generated by Django 4.2.14 on 2024-10-18 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mcqs', '0024_alter_bookmark_created_at'),
        ('hive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shared_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_uid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_tests', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_tests', to=settings.AUTH_USER_MODEL)),
                ('test_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcqs.testsession')),
            ],
        ),
    ]