# Generated by Django 5.0.6 on 2024-06-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='user_photo/default.png', upload_to='user_photos'),
        ),
    ]
