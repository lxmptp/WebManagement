# Generated by Django 3.0.2 on 2020-01-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20200116_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='level',
            field=models.CharField(choices=[('J', 'JUNIOR'), ('M', 'MIDDLE'), ('S', 'SENIOR')], default='J', max_length=1),
            preserve_default=False,
        ),
    ]
