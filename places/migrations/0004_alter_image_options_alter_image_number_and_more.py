# Generated by Django 4.2 on 2023-05-07 16:46

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
    ]
