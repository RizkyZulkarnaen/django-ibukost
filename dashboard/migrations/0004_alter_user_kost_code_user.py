# Generated by Django 4.2.5 on 2023-10-21 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_data_kost_code_kost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_kost',
            name='code_user',
            field=models.IntegerField(),
        ),
    ]
