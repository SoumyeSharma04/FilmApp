# Generated by Django 4.2.6 on 2023-10-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0016_scene_extras_scene_hair_makeup_scene_key_props_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenedurationremark',
            name='lenscs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scenedurationremark',
            name='notescs',
            field=models.TextField(blank=True, null=True),
        ),
    ]