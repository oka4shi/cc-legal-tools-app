# Generated by Django 2.2.13 on 2020-10-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("licenses", "0008_license_title_english"),
    ]

    operations = [
        migrations.AddField(
            model_name="legalcode",
            name="html",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="legalcode",
            name="title",
            field=models.TextField(
                blank=True,
                default="",
                help_text="License title in this language, e.g. 'Attribution-NonCommercial-NoDerivs 3.0 Unported'",
            ),
        ),
    ]
