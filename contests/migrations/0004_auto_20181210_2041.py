# Generated by Django 2.1.2 on 2018-12-10 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_contest_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='is_active',
            new_name='status',
        ),
    ]
