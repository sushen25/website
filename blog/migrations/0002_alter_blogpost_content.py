# Generated by Django 3.2 on 2021-06-14 12:36

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]