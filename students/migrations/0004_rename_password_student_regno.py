# Generated by Django 5.1.1 on 2024-09-09 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0003_remove_request_document_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="password",
            new_name="regno",
        ),
    ]
