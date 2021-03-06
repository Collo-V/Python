# Generated by Django 3.2.2 on 2021-05-26 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('user_num', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.regusers')),
                ('airtime', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('bundles', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('bonga', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sms', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('okoa_limit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('okoa_taken', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('okoa_bal', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('mpesa', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
    ]
