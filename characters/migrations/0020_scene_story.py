# Generated by Django 4.2.6 on 2023-10-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0019_scene_int_ext_scene_timeofday'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='story',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='scene_images/'),
        ),
    ]