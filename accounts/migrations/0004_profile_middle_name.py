# Generated by Django 2.2.17 on 2021-01-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_account_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=40, verbose_name='Middle Name'),
        ),
    ]
