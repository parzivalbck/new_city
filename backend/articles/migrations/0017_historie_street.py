# Generated by Django 4.2.1 on 2023-06-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_historie_delete_history_alter_new_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='historie',
            name='street',
            field=models.CharField(max_length=300, null=True),
        ),
    ]