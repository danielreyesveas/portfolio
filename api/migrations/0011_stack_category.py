# Generated by Django 2.2.19 on 2021-03-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210314_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]