# Generated by Django 5.0.6 on 2024-07-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_comment_post_date_comment_post_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_body',
            field=models.TextField(help_text='Enter your comment'),
        ),
    ]
