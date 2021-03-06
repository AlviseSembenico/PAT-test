# Generated by Django 2.2.4 on 2019-08-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PAT', '0002_auto_20190805_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='result',
            field=models.IntegerField(choices=[(1, 'Pass'), (2, 'Fail')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='revision',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
