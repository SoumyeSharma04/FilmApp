# Generated by Django 4.2.6 on 2023-10-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0015_alter_scenedurationremark_scene_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='extras',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='hair_makeup',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='key_props',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='picture_vechiles',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='production',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='props',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='prosthetics',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='set_dressing',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='sfx',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='special_equipments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='special_professionals',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='vfx',
            field=models.TextField(blank=True, null=True),
        ),
    ]
