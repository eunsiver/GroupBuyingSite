# Generated by Django 4.0.4 on 2022-05-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
