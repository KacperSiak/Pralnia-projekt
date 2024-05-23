# Generated by Django 4.2.11 on 2024-05-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
