# Generated by Django 2.2.3 on 2019-08-02 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20190802_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='Nickname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='group.Participate'),
        ),
    ]