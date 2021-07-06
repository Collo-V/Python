# Generated by Django 3.2.2 on 2021-06-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_statement_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='statement',
            name='code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
