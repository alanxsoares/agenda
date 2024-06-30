# Generated by Django 5.0.6 on 2024-06-28 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contato", "0005_alter_contato_img"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="contato",
            name="criador",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="contato",
            name="img",
            field=models.ImageField(
                default="imgs/1.png", upload_to="images/%Y/%m", verbose_name=" "
            ),
        ),
        migrations.AlterField(
            model_name="contato",
            name="sobrenome",
            field=models.CharField(max_length=50, verbose_name="Sobrenome"),
        ),
    ]
