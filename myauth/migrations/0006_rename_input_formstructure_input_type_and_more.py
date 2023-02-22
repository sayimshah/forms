# Generated by Django 4.1.5 on 2023-02-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0005_formvalues'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formstructure',
            old_name='input',
            new_name='input_type',
        ),
        migrations.RemoveField(
            model_name='formstructure',
            name='action',
        ),
        migrations.AddField(
            model_name='formstructure',
            name='is_required',
            field=models.BooleanField(default=False),
        ),
    ]