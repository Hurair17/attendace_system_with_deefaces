# Generated by Django 4.1.3 on 2022-11-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0003_saveimage_name_alter_saveimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveimage',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
