# Generated by Django 3.1.1 on 2020-10-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std_mgmt_sys', '0007_assignments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
                ('submit', models.ManyToManyField(to='std_mgmt_sys.Books')),
            ],
        ),
    ]
