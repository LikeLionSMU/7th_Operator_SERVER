# Generated by Django 2.2.3 on 2019-07-31 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_auto_20190731_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participate',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
    ]