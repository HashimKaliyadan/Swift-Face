# Generated by Django 5.1.4 on 2025-01-12 16:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Student',
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-id'], 'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='user_student',
        ),
    ]