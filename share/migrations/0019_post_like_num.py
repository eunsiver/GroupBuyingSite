# Generated by Django 4.0.3 on 2022-05-26 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0018_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
