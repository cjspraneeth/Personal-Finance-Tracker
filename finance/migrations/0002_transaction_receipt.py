# Generated by Django 5.1.1 on 2024-10-06 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='receipt',
            field=models.FileField(blank=True, null=True, upload_to='receipts/'),
        ),
    ]
