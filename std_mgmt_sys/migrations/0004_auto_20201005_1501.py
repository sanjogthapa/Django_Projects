# Generated by Django 3.1.1 on 2020-10-05 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('std_mgmt_sys', '0003_auto_20201005_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorials',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='std_mgmt_sys.teachers'),
        ),
    ]
